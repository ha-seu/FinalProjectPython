from board import Board
from piece import Piece

class Reversi:
    def __init__(self):
        self.width = int(input("How wide would you like the board to be? Enter Width\n"))
        self.height = int(input("How tall would you like the board to be? Enter Height\n"))
        self.board = Board(self.width, self.height)
        print(self.board)

    def play(self):
        while(Piece.black > 0 and Piece.white > 0 and Piece.blank > 0):
            print("Black, it is your turn.")
            coord = input("Enter your coordinate selection in x,y format.\n")
            while(not self.board.valid_move(coord, 1)):
                print("Invalid coordinate, please enter a valid placement")
                coord = input("Enter your coordinate selection in x,y format.\n")
            self.board.do_move(coord, self.board.valid_move(coord, 1))
            print(self.board)
            print("White, it is your turn.")
            coord = input("Enter your coordinate selection in x,y format.\n")
            while (not self.board.valid_move(coord, 2)):
                print("Invalid coordinate, please enter a valid placement")
                coord = input("Enter your coordinate selection in x,y format.\n")
            self.board.do_move(coord, self.board.valid_move(coord, 2))
            print(self.board)
