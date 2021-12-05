from piece import Piece
class Board:

    def __init__(self, width, height):
        self.playboard = [[0 for i in range(0, width)] for i in range(0, height)]
        self.playboard[width//2] = Piece(width//2,height//2,0)
        self.playboard[width // 2] = Piece(width // 2, height // 2, 0)