import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class LoginPage(Base):

    url = 'https://vn1.ru/'

    # Locators

    button_login = "//p[@class='navbar__item-link-desc']"
    user_name = "//input[@class='authorization__form-input']"
    button_sms = "//button[@class='authorization__form-btn']"
    password = "//input[@class='authorization__form-input']"
    button_authorization = "//input[@class='btn_site']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_button_sms(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sms)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    # Actions

    def click_button_login(self):
        self.get_button_login().click()
        print("click button login")

    def click_button_sms(self):
        self.get_button_sms().click()
        print("click button sms")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    #Methods

    def authorization(self):  # self.driver указывает системе откуда брать драйвер
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url() #отображает текущий url
        self.click_button_login() #клик кнопки авторизации
        time.sleep(2)
        self.input_user_name("9999999999") #ввод номера телефона
        self.click_button_sms() #клик на поле смс
        time.sleep(2)
        self.input_password("1379") #ввод кода

