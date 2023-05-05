import random
from collections import deque

class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [['~' for _ in range(cols)] for _ in range(rows)]
        self.playBoard = [['o' for _ in range(cols)] for _ in range(rows)]
        self.bomb_locations = set()
        self.flag_locations = set()
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def generate_board(self, n):
        # generate n bomb locations
        while len(self.bomb_locations) < n:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            self.bomb_locations.add((y, x))

        for y, x in self.bomb_locations:
            self.board[y][x] = '*'

    def is_bomb(self, row, col):
        return self.board[row][col] == '*'

    def is_unrevealed(self, row, col):
        return self.board[row][col] == '~'

    def get_adjacent_tiles(self, row, col):
        adjacent_tiles = []
        for d_row, d_col in self.directions:
            adj_row, adj_col = row + d_row, col + d_col
            if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                adjacent_tiles.append((adj_row, adj_col))
        return adjacent_tiles

    def calculate_adjacent_bombs(self):
        for row, col in self.bomb_locations:
            for adj_row, adj_col in self.get_adjacent_tiles(row, col):
                if not self.is_bomb(adj_row, adj_col):
                    if self.is_unrevealed(adj_row, adj_col):
                        self.board[adj_row][adj_col] = str(1)
                    else:
                        self.board[adj_row][adj_col] = str(int(self.board[adj_row][adj_col]) + 1)

    def dig_tile(self, row, col):
        if self.is_bomb(row, col):
            return 0
    
        tiles_to_reveal = deque([(row, col)])
        while tiles_to_reveal:
            curr_row, curr_col = tiles_to_reveal.popleft()
    
            if not self.is_unrevealed(curr_row, curr_col):
                continue
            
            if self.board[curr_row][curr_col].isdigit():
                self.playBoard[curr_row][curr_col] = self.board[curr_row][curr_col]
                continue
            
            self.playBoard[curr_row][curr_col] = '~'
    
            for adj_row, adj_col in self.get_adjacent_tiles(curr_row, curr_col):
                if not self.is_bomb(adj_row, adj_col):
                    if self.is_unrevealed(adj_row, adj_col):
                        tiles_to_reveal.append((adj_row, adj_col))
                

    def print_board(self):
        print('X', end=' ')
        for i in range(self.cols):
            print(i, end=' ')
        print()

        for i, row in enumerate(self.board):
            print(i, end=' ')
            print(' '.join(row))

    def print_play_board(self):
        print('X', end=' ')
        for i in range(self.cols):
            print(i, end=' ')
        print()

        for i, row in enumerate(self.playBoard):
            print(i, end=' ')
            print(' '.join(row))

    def reset_board(self):
        self.board = [['~' for _ in range(self.cols)] for _ in range(self.rows)]