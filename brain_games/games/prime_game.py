from random import randint

from brain_games.games.base_game import run_game


def prime_game(user_name: str) -> None:
    run_game(user_name,
             'Answer "yes" if given number is prime. Otherwise answer "no".',
             process_prime_question)


def process_prime_question() -> str:
    MIN_NUM = 7
    MAX_NUM = 100
    n = randint(MIN_NUM, MAX_NUM)

    LOW = 0
    HIGH = 10
    EDGE = 4
    N_EDFE = 30
    is_prime_needed = randint(LOW, HIGH) > EDGE and n > N_EDFE
    if is_prime_needed:
        while True:
            if is_prime(n):
                break
            n -= 1

    print("Question:", n)

    return 'yes' if is_prime(n) else 'no'


def is_prime(n: int) -> bool:
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True
