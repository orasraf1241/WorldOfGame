import os

import Utils


def add_score(difficulty):
    """this func checks if the user play in the game before
    if not we create a new Score file if yes we guest add value to exsist file"""

    if not os.path.isfile(Utils.SCORES_FILE_NAME):
        with open(Utils.SCORES_FILE_NAME, 'a+') as file:
            file.write(str('0'))

    add = (difficulty * 3) + 5
    with open(Utils.SCORES_FILE_NAME, 'r+') as file:
        current_score = int(file.read())
        file.seek(0)
        file.write(str(current_score + ((difficulty * 3) + 5)))
