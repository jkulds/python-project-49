from random import choice, randint

from brain_games.games.base_game import run_game

MIN_NUM = 3
MAX_NUM = 10


def calc_game() -> None:
    run_game("What is the result of the expression?",
             process_calc_question)


def process_calc_question() -> (int, str):
    signs = ['+', '-', '*']
    sign = choice(signs)
    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    result = 0
    match sign:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    question = f"{a} {sign} {b}"

    return result, question
