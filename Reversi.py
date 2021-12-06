from board import Board


class Reversi:

    # Initialization of the game by asking the player the size of the board and printing it
    def __init__(self):
        self.width = int(input("How wide would you like the board to be? Enter Width\n"))
        self.height = int(input("How tall would you like the board to be? Enter Height\n"))
        self.board = Board(self.width, self.height)
        print(self.board)

    # Starts the game, with it looping until the finish conditions are met.
    def play(self):
        while self.board.count_white() > 0 and self.board.count_black() > 0 and self.board.count_blank() > 0:
            self.black_turn()
            print(self.board)
            if not(self.board.count_white() > 0 and self.board.count_black() > 0 and self.board.count_blank()) > 0:
                break
            self.white_turn()
            print(self.board)
        self.winner()

    # Runs through black's turn
    def black_turn(self):
        print("Black, it is your turn.")
        coord = self.input_ask()
        while not self.board.valid_move(coord, 1):
            print("Invalid coordinate, please enter a valid placement")
            coord = self.input_ask()
        self.board.do_move(coord, self.board.valid_move(coord, 1))

    # Runs through white's turn
    def white_turn(self):
        print("White, it is your turn.")
        coord = self.input_ask()
        while not self.board.valid_move(coord, 2):
            print("Invalid coordinate, please enter a valid placement")
            coord = self.input_ask()
        self.board.do_move(coord, self.board.valid_move(coord, 2))

    # Prints out a winner determined by the amount of pieces each player has
    def winner(self):
        if self.board.count_white() > self.board.count_black():
            print("White Wins!")
        if self.board.count_white() < self.board.count_black():
            print("Black Wins!")

    # Ask for coordinate input, returns a list of two integers in x y format
    def input_ask(self):
        input_list = input("Enter your coordinate selection in x y format.\n")
        coord_list = input_list.split()
        for i in range(len(coord_list)):
            coord_list[i] = int(coord_list[i])
        return coord_list
