import prompt
from brain_games.games.game_logic import play_game
from brain_games.games.brain_even import even, RULES_EVEN


def main():
    play_game(even, RULES_EVEN, 3)


if __name__ == '__main__':
    main()
