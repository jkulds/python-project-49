from random import randint

from brain_games.games.base_game import run_game

MIN_NUM = 7
MAX_NUM = 100


def prime_game() -> None:
    run_game('Answer "yes" if given number is prime. Otherwise answer "no".',
             process_prime_question)


def process_prime_question() -> (str, str):
    number = randint(MIN_NUM, MAX_NUM)

    question = str(number)
    result = 'yes' if is_prime(number) else 'no'

    return result, question


def is_prime(n: int) -> bool:
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True
