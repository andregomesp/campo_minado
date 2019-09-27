import random


class Board:
    bombMap = {}
    recursive_map = {}
    cached_zero_map = {}
    zero_map = {}
    number_of_rows = 0
    number_of_clicks = 0

    def check_adjacent(self, key):
        adjacent_bombs = 0
        clickX, clickY = int(key[0]), int(key[1])
        for numberX in range (-1, 2):
            if (numberX == -1 and clickX == 0) or (numberX == 1 and clickX == self.number_of_rows -1):
                continue
            for numberY in rage(-1, 2):
                if zero_map[str(numberX)+str(numberY)] is not None or (numberY == -1 and clickY == 0) or (numberY == 1 and clickY == self.number_of_rows -1):
                    continue
                if self.bombMap[str(numberX)+str(numberY)] is not None:
                    adjacent_bombs += 1
        if adjacent_bombs == 0:
            zero_map[key] = 1
        return adjacent_bombs

    def check_square(self, key):
        self.number_of_clicks += 1
        result = None
        if self.bombMap[key] is not None:
            result = "boom"
        else:
            if self.number_of_clicks == number_of_rows ** 2:
                result = "winner"
            else:
                number = self.check_adjacent(key)
        return str(number)

    def populate_map(self, number_of_rows, number_of_bombs):
        self.number_of_rows = number_of_rows
        for bomb in range(0, number_of_bombs):
        while True:
            x, y = str(random.randint(0, number_of_rows))
            coord: str = x + y
            if self.bombMap[coord] is None:
                self.bombMap[coord] = 1
                break

    def reset_board(self):
        self.bombMap = {}

    def reset_recursive_map(self):
        self.recursive_map = {}
