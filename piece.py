class Piece:

    def __init__(self, color):
        """Initialization of the piece class

            :param color: color data (0 = blank, 1 = black, 2 = white)
            :type color: int
            """
        self.color = color

    def piece_color(self):
        """Return the color of the piece

        :rtype: char
        :return: " " for blank, "B" for black, "W" for white
        """
        if self.color == 1:
            return "B"
        if self.color == 2:
            return "W"
        if self.color == 0:
            return " "

    def change_color(self, color):
        """Change the color of the piece depending on what the inputted color is.

        :param color: color data (0 = blank, 1 = black, 2 = white)
        :type color: int
        """
        if color == 2:
            self.color = 2
        if color == 1:
            self.color = 1

    def flip(self):
        """Flip a piece between black and white"""
        if self.color == 1:
            self.color = 2
        else:
            self.color = 1

