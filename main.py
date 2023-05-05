import classes.Board as Board

def main():

    board = Board.Board(10, 10)
    board.generate_board(1)
    board.calculate_adjacent_bombs()
    board.dig_tile(5, 5)
    board.print_board()
    print("\n")
    board.print_play_board()
    

main()