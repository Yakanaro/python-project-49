from brain_games.helpers import random_num
import operator
import random

GAME_RULES = 'What is the result of the expression?'


def game_task():
    num1 = random_num()
    num2 = random_num()
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operator_symb = random.choice(list(operators))
    question = f"{num1} {operator_symb} {num2}"
    correct_answer = str(operators.get(operator_symb)(num1, num2))
    return question, correct_answer
