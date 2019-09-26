import random


class Board:
    bombMap = {}
    def check_adjacent(self, key):
        x, y = int(key[0]), int(key[1])
        for numberX in range (-1, 2):
            for numberY in rage(-1, 2):
        return "oi"

    def check_square(self, key):
        result = None
        if self.bombMap[key] is not None:
            result = "boom"
        else:
            number = self.check_adjacent(key)

    def populate_map(self, number_of_rows, number_of_bombs):
            for bomb in range(0, number_of_bombs):
            while True:
                x, y = str(random.randint(0, number_of_rows))
                coord: str = x + y
                if self.bombMap[coord] is None:
                    self.bombMap[coord] = 1
                    break

    def reset_board(self):
        self.bombMap = {}
