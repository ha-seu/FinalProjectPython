from piece import Piece
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.playboard = [[Piece(0) for i in range(0, width)] for i in range(0, height)]
        self.playboard[height // 2 - 1][width // 2].change_color(1)
        self.playboard[height // 2][width // 2 - 1].change_color(1)
        self.playboard[height // 2][width // 2].change_color(2)
        self.playboard[height // 2 - 1][width // 2 - 1].change_color(2)

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
        # right check
        if x < self.width-2 and self.playboard[y][x+1] != color and self.playboard[y][x+1].color != 0:
            for i in range(x+2,self.width-1):
                if self.playboard[y][i].color == color:
                    list_of_valid += [[y, i, 1]]
        # left check
        if x > 1 and self.playboard[y][x-1] != color and self.playboard[y][x-1].color != 0:
            for i in range(x-2,0,-1):
                if self.playboard[y][i].color == color:
                    list_of_valid += [[y, i, 5]]

        return list_of_valid

    def do_move(self, coord, direction):
        x = int(coord[0]) - 1
        y = int(coord[2]) - 1
        for i in direction:
            # right flip
            if i[2] == 1:
                for k in range(x,i[1]):
                    if self.playboard[y][k].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[y][k].flip()
                    self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
            if i[2] == 5:
                for k in range(i[1],x):
                    if self.playboard[y][k].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[y][k].flip()
                    self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
