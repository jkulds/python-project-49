from random import randint

from brain_games.games.base_game import run_game


def even_game(user_name: str) -> None:
    run_game(user_name,
             'Answer "yes" if the number is even, otherwise answer "no".',
             process_even_question)


def process_even_question() -> str:
    MIN_NUM = 1
    MAX_NUM = 100
    number = randint(MIN_NUM, MAX_NUM)
    print("Question:", number)
    result = 'yes' if number % 2 == 0 else 'no'
    return result
