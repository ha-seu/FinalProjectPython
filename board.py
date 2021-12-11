from piece import Piece


class Board:

    def __init__(self, width, height):
        """Initialization of the board by defining its width and height. The middle four pieces are laid down in the middle.

        :param width: the width of the board
        :param height: the height of the board
        :type width, height: int
        """
        self.width = width
        self.height = height
        self.playboard = [[Piece(0) for i in range(0, width)] for i in range(0, height)]
        self.playboard[height // 2 - 1][width // 2].change_color(1)
        self.playboard[height // 2][width // 2 - 1].change_color(1)
        self.playboard[height // 2][width // 2].change_color(2)
        self.playboard[height // 2 - 1][width // 2 - 1].change_color(2)

    def __str__(self):
        """Override for the string method, prints a board with grid markers and W and B for the pieces
        :rtype: String
        :return board: A String with formatting to print a text based board
        """
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

    def check_move(self, coord, color):
        """Check if a coordinate is valid, find pieces to flip, then executes the move
        :param coord: The coordinate of the piece that is being attempted to be placed
        :param color: The color of the player putting the piece
        :type coord: list
        :type color: int
        :return list of the pieces to flip
        :rtype list
        """
        x = int(coord[0])-1
        y = int(coord[1])-1
        list_flip = [[y, x]]
        # make sure the new piece can't "over ride" a piece and must be on a blank
        if not self.playboard[y][x].color == 0:
            return list_flip

        # check in all 8 directions from the coordinate to check for pieces to flip.
        for i in [-1, 0, 1]:
            for j in [-1, 0 , 1]:
                try:
                    test_flip = []
                    for k in range(1,max(self.width, self.height)):
                        if self.playboard[y+i*k][x+j*k].color == color:
                            list_flip.extend(test_flip)
                        elif not self.playboard[y+i*k][x+j*k].color == color and not self.playboard[y+i*k][x+j*k].color == 0:
                            test_flip.append((y+i*k, x+j*k))
                        else:
                            break
                except IndexError: # exception for when the index goes to the board's edge
                    pass
        return list_flip

    def do_move(self, list_flip, color):
        if list_flip:
            for i, j in list_flip:
                self.playboard[i][j].color = color
            return 1
        else:
            return 0

    def count_pieces(self, color):
        """Returns the count of blanks on the board
        :param color: color of the piece to count
        :type: int
        :rtype: int
        :return: count of the blank pieces on the board
        """
        count = 0
        for i in range(self.height):
            for k in range(self.width):
                if self.playboard[i][k].color == color:
                    count += 1
        return count

    def count_valid_moves(self, color):
        """Returns the count of valid moves
        :param color: color you want to count the number of valid moves
        :type int
        :rtype: list
        :return: list of possible moves
        """
        valid_moves = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.playboard[y][x].color == 0:
                    if len(self.check_move([x+1, y+1], color)) > 1:
                        valid_moves.append([x+1, y+1])
        return valid_moves
