import requests
import os
import random


def get_money_interval(difficulty):
    """In this func we Will get the current currency rate
            from USD to ILS and will generate an interval"""

    rand = random.randint(1, 100)
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/607c30cf0e0ee03c7b4669c8/latest/USD'
    # Making our request
    response = requests.get(url)
    data = response.json()

    # in this line we take the jason entry and parsing it to get the value of the shekal using dict
    dolar = float(dict(dict(data).get("conversion_rates")).get("ILS"))
    total = dolar * rand

    interval_a = total - difficulty + 5
    interval_b = total + difficulty + 5

    print("the dolar is :", dolar, "randon num is :", rand, "interval is :", interval_a, "  ", interval_b)
    get_guess_from_user([interval_a, interval_b])


def get_guess_from_user(intervals):
    while True:
        try:
            user_input = int(input("Pleas enter integer to guess :"))
            if user_input < intervals[0] or user_input > intervals[1]:
                print("Oaaa.. Your guess is not right  ")
                return False
            else:
                print("Congratulation your guess is right")
                return True
        except:
            print("You need to input a number")


def play(difficulty):
    return get_money_interval(difficulty)
