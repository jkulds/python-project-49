import prompt


def welcome_user() -> None:
    user = prompt.string("May I have your name?")
    print("Hello, " + user)