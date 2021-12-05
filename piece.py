class Piece:
    black = 0
    white = 0
    # Initilization of the piece class taking the x and y coordinates as color data (0 = black, 1 = white)
    def __init__(self, color):
        self.x = x
        self.y = y
        self.color = color
        if color == 0:
            Piece.black += 1
        if color == 1:
            Piece.white += 1

