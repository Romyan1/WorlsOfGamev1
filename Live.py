import GuessGame
import MemoryGame
import CurrencyRouletteGame
global difficulty, choose_game


def welcome():
    z = 0
    while z == 0:
        name = str(input('enter your name'))
        if type(name) != str(z):
            print(f'hello  {name}  and welcome to the World of Games (WoG). Here you can find many cool games to play.')
            z = 1
        else:
            print('You enter an invalid name,please try again')
    return name


def load_game(difficulty):
    print('Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
    x = 0
    while x == 0:
        choose_game = int(input('please choose a game'))
        if choose_game <= 3 and choose_game >= 1:
            if choose_game == 1:
                print('you chose option number 1')
                MemoryGame.play(difficulty)
                x = 1
            elif choose_game == 2:
                print('you chose option number 2')
                GuessGame.play(difficulty)
                x = 1
            elif choose_game == 3:
                print('you chose option number 3')
                CurrencyRouletteGame.play(difficulty)
                x = 1
        else:
            print('you chose an invalid number, please try again')
    return difficulty, choose_game


