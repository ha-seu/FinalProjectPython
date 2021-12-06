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
        list_of_valid = []
        # left check
        if x > 1 and self.playboard[y][x-1] != color and self.playboard[y][x-1].color != 0:
            for i in range(x-2,0,-1):
                if self.playboard[y][i].color == color:
                    list_of_valid += [y, i]
        return list_of_valid

    def do_move(self, coord, color, direction):
        x = int(coord[0]) - 1
        y = int(coord[2]) - 1
        if color == 1:
            self.playboard[direction[0]][direction[1]].change_black()
            self.playboard[y][x].change_black()
        if color == 2:
            self.playboard[direction[0]][direction[1]].change_white()
            self.playboard[y][x].change_white()