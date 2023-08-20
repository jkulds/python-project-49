#!/usr/bin/python3
from brain_games.cli import welcome_user, prime_game


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    prime_game(user)
