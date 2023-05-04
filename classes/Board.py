import random

class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [['~' for _ in range(cols)] for _ in range(rows)]
        self.bomb_locations = set()

    def generate_board(self, n):
        # generate n bomb locations
        while len(self.bomb_locations) < n:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            self.bomb_locations.add((y, x))

        for y, x in self.bomb_locations:
            self.board[y][x] = 'B'

    def calculate_adjacent_bombs(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for row, col in self.bomb_locations:
            for d_row, d_col in directions:
                adj_row, adj_col = row + d_row, col + d_col
                if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols and self.board[adj_row][adj_col] != 'B':
                    if(self.board[adj_row][adj_col] == '~'):
                        self.board[adj_row][adj_col] = str(1)
                    else:
                        self.board[adj_row][adj_col] = str(int(self.board[adj_row][adj_col]) + 1)


    def print_board(self):
        print('X', end=' ')
        for i in range(self.cols):
            print(i, end=' ')
        print()

        for i, row in enumerate(self.board):
            print(i, end=' ')
            print(' '.join(row))

    def reset_board(self):
        self.board = [['~' for _ in range(self.cols)] for _ in range(self.rows)]