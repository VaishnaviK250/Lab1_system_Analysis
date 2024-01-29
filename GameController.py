from GameBoard import GameBoard
from Player import Player

class GameController:
    def __init__(self, player_count=2):
        self.players = [Player(i) for i in range(player_count)]
        self.current_player_index = 0
        self.board = GameBoard()
        self.game_over = False

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"\nPlayer {current_player.player_id + 1}'s turn.")
        self.board.display_board()

        index1 = int(input('Enter the index for tile 1: '))
        index2 = int(input('Enter the index for tile 2: '))

        if self.board.is_match(index1, index2):
            print("It's a match!")
            current_player.increase_score()
            self.board.update_board(index1, index2)
        else:
            print('Not a match!')

        self.switch_player()

    def check_game_end(self):
        if all(c.isupper() for c in self.board.board):
            self.game_over = True
            self.declare_winner()

    def declare_winner(self):
        highest_score = max(player.score for player in self.players)
        winners = [player.player_id + 1 for player in self.players if player.score == highest_score]

        if len(winners) == 1:
            print(f"\nPlayer {winners[0]} wins!")
        else:
            print("\nIt's a tie between players: " + ', '.join(map(str, winners)))
