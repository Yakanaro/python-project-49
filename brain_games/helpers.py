import random


def is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def random_num():
    return random.randint(1, 100)
