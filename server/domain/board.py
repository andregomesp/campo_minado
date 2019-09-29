import random


class Board:
    bombMap = {}
    number_of_rows = 0
    number_of_clicks = 0

    def check_adjacent(self, key):
        adjacent_bombs = 0
        key_str = str(key)
        if len(key_str) < 5:
            return None
        click_x, click_y = int(key_str[2]), int(key_str[3])
        for numberX in range(-1, 2):
            if (numberX == -1 and click_x == 0) or (numberX == 1 and click_x == self.number_of_rows -1):
                continue
            for numberY in range(-1, 2):
                if (numberY == -1 and click_y == 0) or (numberY == 1 and click_y == self.number_of_rows -1):
                    continue
                if str(click_x + numberX)+str(click_y + numberY) in self.bombMap:
                    adjacent_bombs += 1
        return adjacent_bombs

    def check_square(self, key):
        self.number_of_clicks += 1
        if len(str(key)) < 4:
            return None
        result = None
        if key in self.bombMap:
            result = "boom"
        else:
            if self.number_of_clicks == (self.number_of_rows ** 2) - len(self.bombMap):
                result = "winner"
            else:
                result = self.check_adjacent(key)
        return str(result)

    def populate_map(self, number_of_rows, number_of_bombs):
        self.number_of_rows = number_of_rows
        for bomb in range(0, number_of_bombs):
            while True:
                x, y = str(random.randint(0, number_of_rows)), str(random.randint(0, number_of_rows))
                coord: str = x + y
                if coord not in self.bombMap:
                    self.bombMap[coord] = 1
                    break

    def reset_board(self):
        self.bombMap = {}