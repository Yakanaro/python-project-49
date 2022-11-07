from random import randint

GAME_RULES = 'What number is missing in the progression?'


def game_task():
    start_progression = randint(1, 101)
    step = randint(3, 5)
    number_count = randint(5, 10)
    end_progression = start_progression + step * number_count
    progression = list(range(start_progression, end_progression, step))
    random_num = randint(0, number_count - 1)
    correct_answer = str(progression[random_num])
    progression[random_num] = '..'
    question = ''
    for number in progression:
        question += str(number) + " "
    question = str(question.strip())
    return question, correct_answer
