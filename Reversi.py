from board import Board


class Reversi:


    def __init__(self):
        """Initialization of the game by asking the player the size of the board and printing it"""
        self.width = int(input("How wide would you like the board to be? Enter Width\n"))
        self.height = int(input("How tall would you like the board to be? Enter Height\n"))
        self.board = Board(self.width, self.height)
        print(self.board)


    def play(self):
        """Starts the game, with it looping until the finish conditions are met."""
        while self.game_valid(1):
            self.black_turn()
            print(self.board)
            if not self.game_valid(2):
                break
            self.white_turn()
            print(self.board)
        self.winner()

    def black_turn(self):
        """Runs through black's turn"""
        print("Black, it is your turn.")
        print("These are your possible moves: " + str(self.board.count_valid_moves(1)))
        coord = self.input_ask()
        while len(self.board.check_move(coord, 1))==1:
            print("Invalid coordinate, please enter a valid placement")
            coord = self.input_ask()
        self.board.do_move(self.board.check_move(coord, 1), 1)

    def white_turn(self):
        """Runs through white's turn"""
        print("White, it is your turn.")
        print("These are your possible moves: " + str(self.board.count_valid_moves(2)))
        coord = self.input_ask()
        while len(self.board.check_move(coord, 2)) == 1:
            print("Invalid coordinate, please enter a valid placement")
            coord = self.input_ask()
        self.board.do_move(self.board.check_move(coord, 2), 2)

    def winner(self):
        """Prints out a winner determined by the amount of pieces each player has"""
        if self.board.count_pieces(2) > self.board.count_pieces(1):
            print("White Wins!")
        if self.board.count_pieces(2) < self.board.count_pieces(1):
            print("Black Wins!")
        else:
            print("A tie!")


    def input_ask(self):
        """Ask for coordinate input, returns a list of two integers in x y format

        :rtype list
        :return coord_list: coordinates of inputted x and y
        """
        input_list = input("Enter your coordinate selection in x y format.\n")
        coord_list = input_list.split()
        for i in range(len(coord_list)):
            coord_list[i] = int(coord_list[i])
        return coord_list

    def game_valid(self, color):
        """Makes sure the game is still valid, terminates if no more black, white or blank pieces or if there are no
        more moves for the current player

        :param color
        :type int
        """
        if(self.board.count_pieces(2) > 0 and self.board.count_pieces(1) > 0 \
                and self.board.count_pieces(0) > 0 and len(self.board.count_valid_moves(color)) > 0):
            return True
        else:
            return False