import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Score import add_Score

global difficulty, choose_game


def welcome():
    global name
    z = 0
    while z == 0:
        name = input('enter your name')
        if name.isalpha():
            print(f'hello  {name}  and welcome to the World of Games (WoG). Here you can find many cool games to play.')
            z = 1
        else:
            print('You enter an invalid name,please try again')
    return name


def load_game():
    global difficulty, choose_game
    while True:
        difficulty = input('enter difficulty between 1-5 for your game')
        if difficulty.isnumeric():
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                print(f'you choose level  {difficulty}  of difficulty for your game.')
                break
            print('You chose difficulty out of range')
        else:
            print('You enter an invalid number, please try again')

    print('''Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    x = 0

    while x == 0:
        try:
            choose_game = input('please choose a game')
            if choose_game.isnumeric():
                choose_game = int(choose_game)
                if 3 >= choose_game >= 1:
                    if choose_game == 1:
                        print('you chose option number 1')
                        if bool(MemoryGame.play(difficulty)) is True:
                            add_Score(difficulty=difficulty)
                        x = 1
                    elif choose_game == 2:
                        print('you chose option number 2')

                        if bool(GuessGame.play(difficulty)) is True:
                            add_Score(difficulty=difficulty)
                        x = 1
                    elif choose_game == 3:
                        print('you chose option number 3')
                        if bool(CurrencyRouletteGame.play(difficulty)) is True:
                            add_Score(difficulty=difficulty)
                        x = 1
                    continue_game = str(input('''Would you like to play again?
                                if yes press y, if not press n'''))
                    if continue_game == 'y':
                        x = 0
                    elif continue_game == 'n':
                        open('Score.txt', 'w').close()
                        x = 1
            else:
                print('you chose an invalid number, please try again')

        except:
            print('You enter an invalid answer, please try again')



    return difficulty, choose_game
