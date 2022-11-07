from brain_games.helpers import random_num
from math import gcd

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def game_task():
    num1 = random_num()
    num2 = random_num()
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
