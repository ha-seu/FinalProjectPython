from piece import Piece
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.playboard = [[Piece(0) for i in range(0, width)] for i in range(0, height)]
        self.playboard[height // 2 - 1][width // 2].change_black()
        self.playboard[height // 2][width // 2 - 1].change_black()
        self.playboard[height // 2][width // 2].change_white()
        self.playboard[height // 2 - 1][width // 2 - 1].change_white()

    def __str__(self):
        board = ""
        for i in range(self.width+1):
            board += str(i)+"|"
        board += "\n"
        for k in range(self.height):
            board += str(k+1)+"|"
            for j in range(self.width):
                board += str(self.playboard[k][j].piece_color())+"|"
            board += "\n"
        return board

    def valid_move(self, coord, color):
        x = int(coord[0])-1
        y = int(coord[2])-1
        # left check
        if x > 2:
            if self.playboard[y][x-1].color != color and self.playboard[y][x-1].color != 0:
                if self.playboard[y][x-2].color == color:
                    return True
        # right check
        if x < self.width-1:
            if self.playboard[y][x+1].color != color and self.playboard[y][x+1].color !=0:
                if self.playboard[y][x+2].color == color:
                    return True

    #def do_move(self, coord, color):