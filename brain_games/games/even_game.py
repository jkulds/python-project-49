from random import randint

from brain_games.games.base_game import run_game

MIN_NUM = 1
MAX_NUM = 100


def even_game() -> None:
    run_game('Answer "yes" if the number is even, otherwise answer "no".',
             process_even_question)


def process_even_question() -> (str, str):
    number = randint(MIN_NUM, MAX_NUM)

    result = 'yes' if number % 2 == 0 else 'no'
    question = str(number)

    return result, question
