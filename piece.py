class Piece:
    black = 0
    white = 0
    blank = 0
    # Initilization of the piece class taking the x and y coordinates as color data (0 = blank, 1 = black, 2 = white)
    def __init__(self, color):
        self.color = color
        if color == 1:
            Piece.black += 1
        if color == 2:
            Piece.white += 1
        if color == 0:
            Piece.blank += 1

    def piece_color(self):
        if self.color == 1:
            return "B"
        if self.color == 2:
            return "W"
        if self.color == 0:
            return " "

    def change_white(self):
        if self.color == 1:
            Piece.black -= 1
        if self.color == 0:
            Piece.blank -= 1
        Piece.white += 1
        self.color = 2

    def change_black(self):
        if self.color == 2:
            Piece.white -= 1
        if self.color == 0:
            Piece.blank -= 1
        Piece.black += 1
        self.color = 1

