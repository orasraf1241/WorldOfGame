import os
import random
import time
import sys

"""The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose."""


def generate_sequence(difficulty):
    """ - Will generate a list of random numbers between 1 to 101. The list  length will be difficulty."""
    list_of_rand = []
    for i in range(difficulty):
        list_of_rand.append(random.randint(0, 101))

    print(list_of_rand)
    time.sleep(1)
    os.system('cls' if os.name =='nt' else 'clear')

    return list_of_rand


def get_list_from_user(difficulty):
    """ - Will return a list of numbers prompted from the user. The list length
        will be in the size of difficulty."""
    guess_list = []
    print("pleas enter ", difficulty, "numer : ")
    for i in range(difficulty):
        guess_list.append(int(input()))
    return guess_list


def is_list_equal(list1, list2):
    """ - A function to compare two lists if they are equal. The function will return  True / False."""
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print("\n\n The list is not equal \n")
            return False
    print("\n\n good !!! you are right \n")
    return True


def play(difficulty):
    """- Will call the functions above and play the game. Will return True / False if the user
        lost or won."""
    result_list = generate_sequence(difficulty)
    guess_list = get_list_from_user(difficulty)
    return is_list_equal(result_list, guess_list)
