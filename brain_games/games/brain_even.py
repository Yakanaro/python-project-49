from brain_games.helpers import is_even, random_num

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(num):
    return is_even(num)


def game_task():
    question = random_num()
    correct_answer = str(even(question))
    return question, correct_answer
