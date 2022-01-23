import CurrencyRouletteGame
import GuessGame
import MainScores
import MemoryGame
import Score


def welcome(name):
    print("""Hello """, name, """ and welcome to the World of Games (WoG).
        Here you can find many cool games to play.""")


def choosing_difficulty():
    """choosing the difficulty of the game"""
    while True:
        try:
            difficulty = int(input("Pleas input a difficulty number between 1 - 5:  "))
            if 0 < difficulty < 6:
                print("difficulty is ", difficulty)
                return difficulty
            else:
                pass
        except BaseException:
            print("You need to input a number between 1 - 5")


def load_game():
    boole = True
    while boole:
        try:
            while True:
                game_select = int(input("""Please choose a game to play:
                   1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                   2. Guess Game - guess a number and see if you chose like the computer
                   3. Currency Roulette -try and guess the value of a random amount of USD in ILS 
                   4.Exit \n\n -------------->:"""))
                if 0 < game_select < 5:
                    break

            print(game_select)
            if game_select == 1:
                diff = choosing_difficulty()
                res = MemoryGame.play(diff)
                if res:
                    Score.add_score(diff)

            if game_select == 2:
                diff = choosing_difficulty()
                res = GuessGame.play(diff)
                if res:
                    Score.add_score(diff)

            if game_select == 3:
                res = CurrencyRouletteGame.play(diff)
                if res:
                    Score.add_score(diff)

            if game_select == 4:
                boole = False


        except :
            print("You need to insert a number between 1 - 4")


if __name__ == "__main__":
    welcome(input("pleas enter your name :"))
    load_game()
    MainScores.app.run()