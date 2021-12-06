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
            for i in range(x + 2,self.width-1):
                if self.playboard[y][i].color == color:
                    list_of_valid += [[y, i, 1]]
        # top-right check
        if x < self.width-2 and y > 1 and self.playboard[y-1][x+1] != color and self.playboard[y-1][x+1].color != 0:
            for i in range(2, min(self.width-x, y)):
                if self.playboard[y-i][x+i].color == color:
                    list_of_valid += [[i, i, 2]]
        # top check
        if y > 1 and self.playboard[y-1][x] != color and self.playboard[y-1][x].color != 0:
            for i in range(y - 2, 0, -1):
                if self.playboard[i][x].color == color:
                    list_of_valid += [[i, x, 3]]
        # top-left check
        if x > 1 and y > 1 and self.playboard[y-1][x-1] != color and self.playboard[y-1][x-1].color != 0:
            for i in range(2, min(x, y)):
                if self.playboard[y-i][x-i].color == color:
                    list_of_valid += [[i, i, 4]]
        # left check
        if x > 1 and self.playboard[y][x-1] != color and self.playboard[y][x-1].color != 0:
            for i in range(x - 2, 0, -1):
                if self.playboard[y][i].color == color:
                    list_of_valid += [[y, i, 5]]
        # bottom-left check
        if x > 1 and y < self.height-2 and self.playboard[y+1][x-1] != color and self.playboard[y+1][x-1].color != 0:
            for i in range(2, min(x, self.height-y)):
                if self.playboard[y+i][x-i].color == color:
                    list_of_valid += [[i, i, 6]]
        # bottom check
        if y < self.height-2 and self.playboard[y+1][x] != color and self.playboard[y+1][x].color != 0:
            for i in range(y + 2, self.height-1):
                if self.playboard[i][x].color == color:
                    list_of_valid += [[i, x, 7]]
        # bottom-right check
        if x < self.width-2 and y < self.height-2 and self.playboard[y+1][x+1] != color and self.playboard[y+1][x+1].color != 0:
            for i in range(2, min(self.height-x, self.height-y)):
                if self.playboard[y+i][x+i].color == color:
                    list_of_valid += [[i, i, 8]]


        return list_of_valid

    def do_move(self, coord, direction):
        x = int(coord[0]) - 1
        y = int(coord[2]) - 1
        for i in direction:
            # right flip
            if i[2] == 1:
                for k in range(x, i[1]):
                    if self.playboard[y][k].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[y][k].flip()
                self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
            # top-right flip
            if i[2] == 2:
                for k in range(1, i[1]):
                    if self.playboard[y-k][x+k].color != self.playboard[y-i[0]][x+i[1]].color:
                        self.playboard[y-k][x+k].flip()
                self.playboard[y][x].change_color(self.playboard[y-i[0]][x+i[1]].color)
            # top flip
            if i[2] == 3:
                for k in range(i[0], y):
                    if self.playboard[k][x].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[k][x].flip()
                self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
            # top-left flip
            if i[2] == 4:
                for k in range(1, i[1]):
                    if self.playboard[y-k][x-k].color != self.playboard[y-i[0]][x-i[1]].color:
                        self.playboard[y-k][x-k].flip()
                self.playboard[y][x].change_color(self.playboard[y-i[0]][x-i[1]].color)
            # left flip
            if i[2] == 5:
                for k in range(i[1], x):
                    if self.playboard[y][k].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[y][k].flip()
                self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
            # bottom-left flip
            if i[2] == 6:
                for k in range(1, i[1]):
                    if self.playboard[y+k][x-k].color != self.playboard[y+i[0]][x-i[1]].color:
                        self.playboard[y+k][x-k].flip()
                self.playboard[y][x].change_color(self.playboard[y+i[0]][x-i[1]].color)
            # bottom flip
            if i[2] == 7:
                for k in range(y, i[0]):
                    if self.playboard[k][x].color != self.playboard[i[0]][i[1]].color:
                        self.playboard[k][x].flip()
                self.playboard[y][x].change_color(self.playboard[i[0]][i[1]].color)
            # bottom-right flip
            if i[2] == 8:
                for k in range(1, i[1]):
                    if self.playboard[y+k][x+k].color != self.playboard[y+i[0]][x+i[1]].color:
                        self.playboard[y+k][x+k].flip()
                self.playboard[y][x].change_color(self.playboard[y+i[0]][x+i[1]].color)