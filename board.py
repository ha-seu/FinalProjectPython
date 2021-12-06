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

    def valid_check(self, coord):
        same_count = 0
        other_count = 0
        for i in range(self.width):
            if self.playboard[coord[1]][i].color == self.playboard[coord[1]][coord[0]].color:
                same_count +=1
            if self.playboard[coord[1]][i].color != self.playboard[coord[1]][coord[0]].color and self.playboard[coord[1]][i].color != 0:
                other_count +=1
        if(same_count>2 and other_count:

