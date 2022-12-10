import time
import os


def generate_sequence(difficulty):
    import random
    random_num = []
    for number in range(difficulty):
        random_num.append(int(random.uniform(1, 101)))
    print(random_num)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_num


def get_list_from_user(difficulty):
    user_numbers = []
    print(f"Please Insert {difficulty} numbers")
    for num in range(difficulty):
        num = user_numbers.append(int(input("Import a Number: ")))
    return user_numbers


def is_list_equal(random_num, user_numbers):
    random_num.sort()
    user_numbers.sort()
    os.system('cls')
    if random_num == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    random_num = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)
    if is_list_equal(user_numbers=user_numbers, random_num=random_num):
        print("you won")
        return True
    else:
        print("you lost")
        return False


