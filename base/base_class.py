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

    """Метод проверки url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Метод проверки заголовка"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Заголовки совпадают")

    """Скриншот"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\alexa\\oop\\FinalProject\\screen\\' + name_screenshot)

    """Метод сравнения url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("url совпадает")

    """Метод скролла страницы"""

    def scroll_to(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    """Метод очистки полей"""

    def clear_input_field(self, xpath):
        """Очищает поле ввода по заданному XPATH."""
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.element.clear()  # Очищает поле ввода с помощью метода clear()
        print("Поле ввода очищено.")