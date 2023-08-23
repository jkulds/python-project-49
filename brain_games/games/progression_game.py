from random import randint
from brain_games.games.base_game import run_game

PROGRESSION_LENGTH = 10
WINDOWS_START = 3
MIN_NUM = 1
MAX_NUM = 5


def progression_game() -> None:
    run_game("What number is missing in the progression?",
             process_progression_question)


def process_progression_question() -> (int, str):
    progression_diff = randint(MIN_NUM, MAX_NUM)
    start_num = randint(MIN_NUM, MAX_NUM)
    result_index = randint(WINDOWS_START, PROGRESSION_LENGTH - WINDOWS_START)
    num_list = []
    result = 0
    for i in range(PROGRESSION_LENGTH):
        current = start_num + i * progression_diff
        if i == result_index:
            result = current
            num_list.append('..')
        else:
            num_list.append(current)

    question = " ".join(map(str, num_list))

    return result, question
