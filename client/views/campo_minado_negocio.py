from random import randint
import json
import os

from client.connection.connectionInterface import make_connection


class CampoMinado:
    
    def novoJogo(self,linha,coluna):
        self.linha = int(linha)
        self.coluna = int(coluna)
        self.jogadas = self.totalJogadas(linha, coluna)
        self.tabuleiro = self.iniciaTabuleiro(linha, coluna)
        self.localizacaoBombas = self.espalhaBombas(linha,coluna)
    
    def qtdBombas(self):
        qtdBombas = int((self.linha*self.coluna)/4 + 1)
        return qtdBombas

    def espalhaBombas(self, linha, coluna):
        qtdBombas = self.qtdBombas()
        localizacaoBombas = []
        while qtdBombas > 0:
            local = (randint(0,linha - 1), randint(0,coluna-1)) 
            if local not in localizacaoBombas:
                localizacaoBombas.append(local)
                qtdBombas -= 1
        return localizacaoBombas

    def iniciaTabuleiro(self,linha,coluna):
        return [[str('&') for i in range(coluna)] for j in range(linha)]

    def totalJogadas(self,linha,coluna):
        return (linha*coluna) - self.qtdBombas()

    def verificaJogada(self):
        verifica = False
        if self.jogadas > 0:
            verifica = True
        return verifica

    def imprimeTabulerio(self):
        for pos in self.tabuleiro:
            print(str(pos))
            
    def validaCoordenadas(self, linha, coluna):
        verifica = False;
        if linha in range(0, self.linha) and coluna in range(0, self.coluna):
            verifica = True
        return verifica
    
    def verificaCoordenadas(self,coordenada):
        verifica = False;
        if coordenada in self.localizacaoBombas:
            verifica = True
        return verifica
    
    def contaBombas(self, linha, coluna):
        bombas = 0
        for x in range(linha-1, linha+2,1):
            for y in range(coluna-1, coluna+2,1):
                posicao = (x,y)
                if posicao in self.localizacaoBombas:
                    bombas += 1
        return str(bombas)
    
    def contaVizinhos(self):
        for i in self.localizacaoBombas:
            vizinhos = []
            for x in range(i[0] - 1, i[0]+2):
                for y in range(i[1]-1, i[1]+2):
                    posicao = (x,y)
                    if x > 0 and x < self.linha and y>0 and y < self.coluna:
                        if posicao not in self.localizacaoBombas:
                            vizinhos.append(posicao)
            tam = len(vizinhos)
            marcardor = 0
            for k in vizinhos:
                if self.tabuleiro[k[0]][k[1]] != '&':
                    marcardor += 1
            if marcardor == tam:
                self.tabuleiro[i[0]][i[1]] = str('!')
    
    def jogar(self, linha, coluna):
        linha = int(linha)
        coluna = int(coluna)

        if not self.validaCoordenadas(linha, coluna):
            return 0
        
        if (linha, coluna) in self.localizacaoBombas:
            self.jogadas = 0
            os.remove("campoMinado.json")
            return -1
        message = (str(linha) + str(coluna)).encode()
        self.tabuleiro[linha][coluna] = str(make_connection([message]))
        # self.tabuleiro[linha][coluna] = str(self.contaBombas(linha, coluna))
        self.jogadas -=1
        if self.jogadas == 0:
            self.contaVizinhos()
            os.remove("campoMinado.json")
            return 2
        self.salvarJogo()
        return 1
    
    def salvarJogo(self):
        estadoAtual = {
            'linha':self.linha,
            'coluna':self.coluna,
            'tabuleiro':self.tabuleiro,
            'jogadas':self.jogadas,
            'bombas':tuple(self.localizacaoBombas)
        }
        estadoAtual = json.dumps(estadoAtual,indent = 5, sort_keys=False)
        arquivo_campoMinado_json = open('campoMinado.json','w')
        arquivo_campoMinado_json.write(estadoAtual)
        arquivo_campoMinado_json.close()
    
    def carregaDados(self,dados):
        self.linha = dados['linha']
        self.coluna = dados['coluna']
        self.jogadas = dados['jogadas']
        self.tabuleiro = dados['tabuleiro']
        bombas = []
        for x in dados['bombas']:
            bombas.append(tuple(x))
        self.localizacaoBombas = bombas