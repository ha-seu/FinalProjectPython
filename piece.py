class Piece:

    # Initialization of the piece class taking the x and y coordinates as color data (0 = blank, 1 = black, 2 = white)
    def __init__(self, color):
        self.color = color

    # Return the color of the piece "B" for Black, "W" for White
    def piece_color(self):
        if self.color == 1:
            return "B"
        if self.color == 2:
            return "W"
        if self.color == 0:
            return " "

    # Change the color of the piece depending on what the inputted color is. Used for changing blanks to a certain color
    def change_color(self, color):
        if color == 2:
            self.color = 2
        if color == 1:
            self.color = 1

    # "Flip" a piece between black and white
    def flip(self):
        if self.color == 1:
            self.color = 2
        else:
            self.color = 1

