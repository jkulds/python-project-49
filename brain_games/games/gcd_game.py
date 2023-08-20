from random import randint

from brain_games.games.base_game import run_game


def gcd_game(user_name: str) -> None:
    run_game(user_name,
             "Find the greatest common divisor of given numbers.",
             process_gcd_question)


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def process_gcd_question() -> int:
    MIN_NUM = 1
    MAX_NUM = 100
    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    result = gcd(a, b)

    print("Question:", a, b)

    return result
