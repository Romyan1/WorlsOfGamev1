import random

import Score


def generate_number(difficulty):

    secret_number = int(random.uniform(1, difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    guess_number = int(input(f"You need to guess a number between 1 to {difficulty}: "))
    return guess_number


def compare_results(secret_number, guess_number):
    if secret_number == guess_number:
        return True


def play(difficulty):
    secret_number = generate_number(difficulty)

    print("Generating a Number....")
    print("Yeap! The number is ready. Now it is Your turn")
    guess_number = get_guess_from_user(difficulty)
    if compare_results(secret_number=secret_number, guess_number=guess_number):
        print("you won")
        return True
    else:
        print("you lost")
        return False