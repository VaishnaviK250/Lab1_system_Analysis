from GameController import GameController
def main():
    game_controller = GameController(player_count=2)

    while not game_controller.game_over:
        game_controller.play_turn()
        game_controller.check_game_end()

if __name__ == "__main__":
    main()

