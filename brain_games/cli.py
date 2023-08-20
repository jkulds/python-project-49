import prompt


def welcome_user() -> str:
    user = prompt.string("May I have your name? ")
    print("Hello, " + user)
    return user


def even_game(user_name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numbers_array = [15, 7, 6]
    i = 0
    while i < len(numbers_array):
        print("Question:", numbers_array[i])
        answer = prompt.string("Your answer: ")
        correct = 'yes' if numbers_array[i] % 2 == 0 else 'no'

        if answer == correct:
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again {user_name}")
            i = 0

    print(f"Congratulations, {user_name}!")
