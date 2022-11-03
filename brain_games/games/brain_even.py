import prompt
from brain_games.helpers import is_even

RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(num):
    return is_even(num)
