class Piece:


    # Initilization of the piece class taking the x and y coordinates as color data (0 = blank, 1 = black, 2 = white)
    def __init__(self, color):
        self.color = color

    def piece_color(self):
        if self.color == 1:
            return "B"
        if self.color == 2:
            return "W"
        if self.color == 0:
            return " "

    def change_color(self, color):
        if color == 2:
            self.color = 2
        if color == 1:
            self.color = 1

    def flip(self):
        if self.color == 1:
            self.color = 2
        else:
            self.color = 1

