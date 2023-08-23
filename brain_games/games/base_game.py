import prompt

NEEDED_CORRECT_ANSWERS = 3


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    user = prompt.string("May I have your name? ")

    print("Hello, " + user)

    return user


def run_game(greet_message: str,
             print_game_question_and_get_result: callable) -> None:

    user = welcome_user()

    print(greet_message)

    correct_answer_count = 0
    for _ in range(NEEDED_CORRECT_ANSWERS):
        result, question = print_game_question_and_get_result()

        print("Question: " + question)

        answer = prompt.string("Your answer: ")

        if answer == str(result):
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'.")
            print(f"Let's try again, {user}!")
            break

    if correct_answer_count == NEEDED_CORRECT_ANSWERS:
        print(f"Congratulations, {user}!")
