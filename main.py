from board import Board
from piece import Piece

width = int(input("How wide would you like the board to be? Enter Width\n"))
height = int(input("How tall would you like the board to be? Enter Height\n"))
board = Board(width, height)
print(board)
print(Piece.blank)
#while(Piece.black > 0 and Piece.white > 0 and Piece.blank > 0):
print("Black, it is your turn.")
coord = input("Enter your coordinate selection in x,y format.\n")
board.valid_check(coord)