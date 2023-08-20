import prompt
from random import randint

def welcome_user() -> str:
    user = prompt.string("May I have your name? ")
    print("Hello, " + user)
    return user


def even_game(user_name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    i = 0
    while i < count:
        number = randint(1, 100)
        print("Question:", number)
        answer = prompt.string("Your answer: ")
        correct = 'yes' if number % 2 == 0 else 'no'

        if answer == correct:
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again {user_name}")
            i = 0

    print(f"Congratulations, {user_name}!")
