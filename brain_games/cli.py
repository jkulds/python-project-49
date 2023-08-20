import prompt
from random import randint, choice


def welcome_user() -> str:
    user = prompt.string("May I have your name? ")
    print("Hello, " + user)
    return user


def even_game(user_name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    i = 0
    while i < count:
        result = print_even_game_question_and_get_result()

        answer = prompt.string("Your answer: ")

        if is_answer_correct(answer, result, user_name):
            i += 1
        else:
            i = 0

    print_user_congratulations(user_name)


def print_even_game_question_and_get_result():
    number = randint(1, 100)
    print("Question:", number)
    result = 'yes' if number % 2 == 0 else 'no'
    return result


def calc_game(user_name: str) -> None:
    print('What is the result of the expression?')

    run_3_loop_game(user_name, print_calc_game_question_and_get_result)

    print_user_congratulations(user_name)


def print_user_congratulations(user_name: str) -> None:
    print(f"Congratulations, {user_name}!")


def print_calc_game_question_and_get_result() -> int:
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


def is_answer_correct(answer, result, user_name) -> bool:
    if answer == result:
        print("Correct!")
        return True

    print(f"'{answer}' is wrong answer ;(."
          f" Correct answer was '{result}'.")
    print(f"Let's try again {user_name}")

    return False


def gcd_game(user_name: str) -> None:
    print('Find the greatest common divisor of given numbers.')

    run_3_loop_game(user_name, print_gcd_game_question_and_get_result)

    print_user_congratulations(user_name)


def run_3_loop_game(user_name, print_question_and_get_lap_result):
    count = 3
    i = 0
    while i < count:
        result = print_question_and_get_lap_result()

        answer = prompt.integer("Your answer: ")

        if is_answer_correct(answer, result, user_name):
            i += 1
        else:
            i = 0


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def print_gcd_game_question_and_get_result() -> int:
    min_num = 1
    max_num = 100
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
    result = gcd(a, b)

    print("Question:", a, b)

    return result
