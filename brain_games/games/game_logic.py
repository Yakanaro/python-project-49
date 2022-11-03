import prompt
from brain_games.helpers import random_num
from brain_games.cli import welcome_user


def game_logic(func):
    num = random_num()
    right_answer = func(num)
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if right_answer == user_answer:
        print('Correct!')
        return True
    else:
        print(
            f'{user_answer} is wrong answer ;(. Correct answer was "{right_answer}"')
        return False


def play_game(func, rules, rounds):
    name = welcome_user()
    print(rules)
    count = 0
    while count != rounds:
        if game_logic(func):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
