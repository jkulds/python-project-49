from random import randint, choice

import prompt


def welcome_user() -> str:
    user = prompt.string("May I have your name? ")
    print("Hello, " + user)
    return user


def even_game(user_name: str) -> None:
    run_game(user_name,
             'Answer "yes" if the number is even, otherwise answer "no".',
             process_even_question)


def calc_game(user_name: str) -> None:
    run_game(user_name,
             "What is the result of the expression?",
             process_calc_question)


def gcd_game(user_name: str) -> None:
    run_game(user_name,
             "Find the greatest common divisor of given numbers.",
             process_gcd_question)


def progression_game(user_name: str) -> None:
    run_game(user_name,
             "What number is missing in the progression?",
             process_progression_question)


def prime_game(user_name: str) -> None:
    run_game(user_name,
             'Answer "yes" if given number is prime. Otherwise answer "no".',
             process_prime_question)


def process_prime_question() -> str:
    n = randint(6, 100)

    is_prime_needed = randint(0, 10) > 4 and n > 30
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


def process_calc_question() -> int:
    signs = ['+', '-', '*']
    sign = choice(signs)
    min_num = 3
    max_num = 10
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
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


def is_answer_correct(answer, result) -> bool:
    if answer == result:
        print("Correct!")
        return True

    return False


def process_even_question() -> str:
    number = randint(1, 100)
    print("Question:", number)
    result = 'yes' if number % 2 == 0 else 'no'
    return result


def run_3_loop_game(user_name, print_question_and_get_lap_result):
    count = 3
    i = 0

    while i < count:
        result = str(print_question_and_get_lap_result())

        answer_message = "Your answer: "

        answer = prompt.string(answer_message)

        if answer == result:
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'.")
            print(f"Let's try again, {user_name}")
            break

    if i == count:
        print(f"Congratulations, {user_name}!")


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def process_gcd_question() -> int:
    min_num = 1
    max_num = 100
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
    result = gcd(a, b)

    print("Question:", a, b)

    return result


def process_progression_question() -> int:
    progression_length = 10
    windows_start = 3
    min_num = 1
    max_num = 5
    progression_diff = randint(min_num, max_num)
    start_num = randint(min_num, max_num)
    result_index = randint(windows_start, progression_length - windows_start)
    num_list = []
    result = 0
    for i in range(progression_length):
        current = start_num + i * progression_diff
        if i == result_index:
            result = current
            num_list.append('..')
        else:
            num_list.append(current)

    print("Question:", " ".join(map(str, num_list)))

    return result


def run_game(user_name: str,
             greet_message: str,
             print_game_question_and_get_result: callable) -> None:
    print(greet_message)

    run_3_loop_game(user_name, print_game_question_and_get_result)
