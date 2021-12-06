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
        # up check
        if y > 2:
            if self.playboard[y-1][x].color != color and self.playboard[y-1][x].color !=0:
                if self.playboard[y-2][x].color == color:
                    return True
        # down check
        if y < self.height-1:
            if self.playboard[y+1][x].color != color and self.playboard[y+1][x].color !=0:
                if self.playboard[y+2][x].color == color:
                    return True
        # up-left check
        if x > 2 and y > 2:
            if self.playboard[y-1][x-1].color != color and self.playboard[y-1][x-1].color != 0:
                if self.playboard[y-1][x-2].color == color:
                    return True
        # up-right check
        if x < self.width-1 and y > 2:
            if self.playboard[y-1][x+1].color != color and self.playboard[y-1][x+1].color != 0:
                if self.playboard[y-1][x+2].color == color:
                    return True
        # down-right check
        if x < self.width-1 and y < self.height-1:
            if self.playboard[y+1][x+1].color != color and self.playboard[y+1][x+1].color != 0:
                if self.playboard[y+1][x+2].color == color:
                    return True
        # down-left check
        if x > 2 and y < self.height-1:
            if self.playboard[y+1][x-1].color != color and self.playboard[y+1][x-1].color != 0:
                if self.playboard[y+1][x-2].color == color:
                    return True
    def do_move(self, coord, color):
        x = int(coord[0]) - 1
        y = int(coord[2]) - 1
        if color == 1:
            self.playboard[y][x].change_white()
        if color == 2:
            self.playboard[y][x].change_black()