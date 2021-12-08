# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def welcome(name):
    print("""Hello """ + name + """ and welcome to the World of Games (WoG).
        Here you can find many cool games to play.""")


def memory_game():
    """The purpose of memory game is to display an amount of random numbers to the users for 0.7
        seconds and then prompt them from the user for the numbers that he remember. If he was right
        with all the numbers the user will win otherwise he will lose."""
    """create random number between 0 - 100 
    x = random.sample(range(101), diff * 2) --> number 
    import time """


def load_game():
    x = 0
    while True:
        x = int(input("""Please choose a game to play:
           1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back
           2. Guess Game - guess a number and see if you chose like the computer
           3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"""))


