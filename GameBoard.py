import random
class GameBoard:
    def __init__(self):
        self.symbols = ['!', '@', '#', '$', '%']
        self.board = ['x'] * 10  
        self.shuffle_board()

    def shuffle_board(self):
        check = self.symbols * 2
        random.shuffle(check)
        self.board = check

    def display_board(self):
        print(' '.join(self.board))

    def is_match(self, index1, index2):
        return self.board[index1] == self.board[index2]

    def update_board(self, index1, index2):
        self.board[index1] = self.board[index1].upper()
        self.board[index2] = self.board[index2].upper()
