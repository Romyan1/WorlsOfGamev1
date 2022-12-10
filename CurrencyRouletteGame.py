from currency_converter import ECB_URL, CurrencyConverter


def get_money_interval(difficulty):
    import random
    random_num = int(random.uniform(1, 100))
    c = CurrencyConverter()
    t = c.convert(random_num, 'USD', 'ILS')
    low = int(t - (10 - difficulty))
    high = int(t + (10 - difficulty))
    return t, low, high


def get_guess_from_user(t):
    # User needs to guess the Value to a given amount of USD
    while True:
        try:
            guess = int(input(f"Guess the value of {t}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        return guess


def play(difficulty):
    t, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(t)
    if high >= guess or guess >= low:
        print("you won")
        return True
    else:
        print("you lost")
        return False

