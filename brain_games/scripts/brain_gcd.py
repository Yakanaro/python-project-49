from brain_games.games.game_logic import play_game
from brain_games.games import brain_gcd


def main():
    play_game(brain_gcd, 3)


if __name__ == '__main__':
    main()