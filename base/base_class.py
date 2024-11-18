import datetime
from telnetlib import EC

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Base():
    def __init__(self, driver):
        self.driver = driver

        """Method get current url"""

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("current url " + get_url)

        """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

        """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\alexa\\oop\\FinalProject\\screen\\' + name_screenshot)

        """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method scroll page"""

    def scroll_to(self, pixels):
        """Прокручивает страницу вниз на заданное количество пикселей."""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")


    