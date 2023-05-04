import classes.Board as Board

def main():

    board = Board.Board(15, 15)
    board.generate_board(10)
    board.calculate_adjacent_bombs()
    board.print_board()



main()