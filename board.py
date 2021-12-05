from piece import Piece
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.playboard = [[Piece(0) for i in range(0, width)] for i in range(0, height)]
        self.playboard[height // 2 - 1][width // 2] = Piece(1)
        self.playboard[height // 2][width // 2 - 1] = Piece(1)
        self.playboard[height // 2][width // 2] = Piece(2)
        self.playboard[height // 2 - 1][width // 2 - 1] = Piece(2)

    def __str__(self):
        board = ""
        for i in range(0, self.width+1):
            board += str(i)+"|"
        board += "\n"
        for k in range(0, self.height):
            board += str(k+1)+"|"
            for j in range(0, self.width):
                board += str(self.playboard[k][j].piece_color())+"|"
            board += "\n"



        return board