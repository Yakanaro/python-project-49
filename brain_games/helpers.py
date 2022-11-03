import random


def is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def random_num():
    return random.randint(1, 100)


def random_operation():
    operations = ['+', '-', '*']
    return operations[random.randint(1, 3)]
