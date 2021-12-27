import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0
screen_cleaner = lambda: os.system('cls' if os.name == 'nt' else 'clear')
