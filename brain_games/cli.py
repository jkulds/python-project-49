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
    count = 3
    i = 0
    while i < count:
        result = print_calc_game_question_and_get_result()

        answer = prompt.integer("Your answer: ")

        if is_answer_correct(answer, result, user_name):
            i += 1
        else:
            i = 0

    print_user_congratulations(user_name)


def print_user_congratulations(user_name):
    print(f"Congratulations, {user_name}!")


def print_calc_game_question_and_get_result():
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


def is_answer_correct(answer, result, user_name):
    if answer == result:
        print("Correct!")
        return True

    print(f"'{answer}' is wrong answer ;(."
          f" Correct answer was '{result}'.")
    print(f"Let's try again {user_name}")

    return False
