from brain_games.helpers import random_num

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d <= n / 2:
        if n % d == 0:
            return False
        d += 1
    return True


def game_task():
    random_number = random_num()
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
