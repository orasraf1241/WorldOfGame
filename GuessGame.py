import random


def generate_number(diff):
    """Will generate number between 1 to difficulty and save it to
        secret_number."""
    return random.randint(1, diff)


def get_guess_from_user():
    """- Will prompt the user for a number between 1 to difficulty and
        return the number."""
    while True:
        try:
            return int(input("pleass input a guess number :"))
        except:
            pass


def compare_results(secret_number, guess_number):
    """Will compare the secret generated number to the one prompted
            by the get_guess_from_user."""
    print(secret_number,"  ", guess_number)
    if secret_number == guess_number:
        print("Its your lake day congratulation")
        return True
    else:
        print("oaaa... sory you worng ")
        return False


def play(diff):
    """Will call the functions above and play the game. Will return True / False if the user
        los or won."""
    print("play of Guess")
    secret_number = generate_number(diff)
    guess_number = get_guess_from_user()
    result = compare_results(secret_number, guess_number)
    print(secret_number,"  ",guess_number)
    if result:
        print("you are right !!")
    return result

