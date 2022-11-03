import prompt
from brain_games.helpers import random_num
from brain_games.cli import welcome_user


def game_logic(question, correct_answer):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if correct_answer == user_answer:
        print('Correct!')
        return True
    else:
        print(
            f'{user_answer} is wrong answer ;(. Correct answer was "{correct_answer}"')
        return False


def play_game(game, rounds):
    name = welcome_user()
    print(game.GAME_RULES)
    count = 0
    while count != rounds:
        question, correct_answer = game.game_task()
        if game_logic(question, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
