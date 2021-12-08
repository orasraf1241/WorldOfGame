import random


def generate_number():
    """Will generate number between 1 to difficulty and save it to
        secret_number."""
    while True:
        try:
            difficulty = int(input("please input a number  :"))
            break
        except:
            print("You need to insert number :")
    secret_number = random.randint(0, difficulty)
    return secret_number

def get_guess_from_user():
    """- Will prompt the user for a number between 1 to difficulty and
        return the number."""
    return int(input("pleass input a guess number :"))


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


def play():
    """Will call the functions above and play the game. Will return True / False if the user
        lost or won."""
    secret_number = generate_number()
    guess_number = get_guess_from_user()
    result = compare_results(secret_number, guess_number)
    return result