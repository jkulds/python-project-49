from random import choice, randint

from brain_games.games.base_game import run_game


def calc_game(user_name: str) -> None:
    run_game(user_name,
             "What is the result of the expression?",
             process_calc_question)


def process_calc_question() -> int:
    signs = ['+', '-', '*']
    sign = choice(signs)
    MIN_NUM = 3
    MAX_NUM = 10
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

    print("Question:", a, sign, b)

    return result
