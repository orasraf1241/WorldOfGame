from selenium import webdriver
from time import sleep
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'http://127.0.0.1:5000/'


def test_score_service():
    try:

        my_driver = webdriver.Chrome(executable_path="/home/or/Desktop/devop_experts/WorldOfGame/test/chromedriver")
        my_driver.get(url)
        score = int(my_driver.find_element_by_id("score").text)
        return 0 <= score <= 1000
    except BaseException:
        print("cannot open the server")


def main_function():
    if test_score_service():
        print(0)
        return sys.exit(0)
    else:
        print(-1)
        return sys.exit(-1)



if __name__ == '__main__':
    main_function()