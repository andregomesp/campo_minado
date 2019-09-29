from client.views.campo_minado_negocio import CampoMinado
import json
import sys
import os


def menu():
    print(" ___________________________________________ ")
    print("|                                           |")
    print("|           ###################             |")
    print("|           #   CAMPO MINADO  #             |")
    print("|           ###################             |")
    print("|                                           |")
    print("|                                           |")
    print("|           1) Iniciar Novo Jogo            |")
    print("|                                           |")
    if os.path.isfile("campoMinado.json"):
        print("|           2) Continuar Jogo               |")
        print("|                                           |")
    print("|           3) Sair                         |")
    print("|                                           |")
    print("|                                           |")
    print("|           ###################             |")
    print("|           #   CAMPO MINADO  #             |")
    print("|           ###################             |")
    print("|___________________________________________|")

def pegaValores():
    os.system("cls")
    print("#############################################")
    print("#                                           #")
    print("#  O TABULEIRO DO CAMPO MINADO SERÁ DE NxN  #")
    print("#       (3,3) (4,4) (5,5) (6,6) (7,7)       #")
    print("#                                           #")
    print("#############################################")
    linhaColuna  = int(input("\n\nDigite o número de linhas e colunas do seu tabuleiro: "))
    input("\n\nCarregando jogo ... Pressione Enter para continuar: ")
    os.system("cls")
    return linhaColuna

def fimDeJogo():
    os.system("cls")
    print("#############################################")
    print("#                                           #")
    print("#             BOOOOOOOM EXPLODIU!           #")
    print("#               TENTE NOVAMENTE             #")
    print("#                                           #")
    print("#############################################")
    escolha = str(input("\n\nDeseja jogar novamente(S/N)? "))
    if(escolha != "s" and escolha != "S"):
        if(escolha != "n" and escolha != "N"):
            input("\n\nDigite S OU N! ... Pressione Enter para continuar: ")
        else:
            os.system("cls")
            sys.exit(0)
    return 

def vitoria(self):
    os.system("cls")
    print("#############################################")
    print("#                                           #")
    print("#             PARABÉNS VOCÊ VENCEU!         #")
    print("#               JOGUE NOVAMENTE             #")
    print("#                                           #")
    print("#############################################")
    print("\n\n\n")
    cm.imprimeTabulerio()
    escolha = str(input("\n\nDeseja jogar novamente(S/N)? "))
    if(escolha != "s" and escolha != "S"):
        if(escolha != "n" and escolha != "N"):
            input("\n\nDigite S OU N! ... Pressione Enter para continuar: ")
        else:
            os.system("cls")
            sys.exit(0)
    return 

def carregarJogo(self):
        arquivo_campoMinado_json = open('campoMinado.json','r')
        dados = json.load(arquivo_campoMinado_json)
        cm.carregaDados(dados)
        arquivo_campoMinado_json.close() 
        iniciaJogo(cm)

def iniciaJogo(self):
    if cm.verificaJogada():
        os.system("cls")
        print(cm.localizacaoBombas)
        cm.imprimeTabulerio()
        try:
            linha = int(input("\nPosição da linha :"))
        except:
            input("\nOpção inválida! Pressione ENTER")
            iniciaJogo(cm)
        try:
            coluna = int(input("\nPosição da coluna :"))
        except:
            input("\nOpção inválida! Pressione ENTER")
            iniciaJogo(cm)
        teste = int(cm.jogar(linha,coluna))
        if teste == -1:
            fimDeJogo()
        elif teste == 0:
            input("\n\nCoordenadas inválidas! Insira valores aceitáveis ... Pressione Enter para continuar: ")
            iniciaJogo(cm)
        elif teste == 2:
            vitoria(cm)
        else:
            iniciaJogo(cm)

if __name__ == "__main__":
    cm = CampoMinado()
    testa = True
    while testa:
        os.system("cls")
        menu()
        opcao = int(input("\n\nDigite a opção desejada: "))
        if opcao == 1:
            linhaColuna = pegaValores()
            cm.novoJogo(linhaColuna,linhaColuna)
            iniciaJogo(cm)
        elif opcao == 2:
            carregarJogo(cm)
        elif opcao == 3:
            input("\nFinalizando jogo ... Pressione Enter para continuar")
            os.system("cls")
            sys.exit(0)
        else:
            print("\nOpção inválida! Selecione uma das opções disponíveis")
            input("\nPressione ENTER para continuar")
            os.system("cls")
        
