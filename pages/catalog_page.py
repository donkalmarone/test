import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class CatalogPage(Base):
    product_price_1 = None  # Атрибут для хранения цены первого товара
    product_price_2 = None  # Атрибут для хранения цены второго товара
    global_product_title_1 = ""
    global_product_title_2 = ""
    def __init__(self,driver): #добавляем driver для того чтобы содержать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators

    location_menu = "//a[@class='header-desktop__select_pharma']"
    select_search = "(//input[@type='search'])[6]"
    search_location = "(//input[@type='submit'])[3]"
    select_location = "//label[@class='radio-label']"
    button_location = "(//input[@type='submit'])[4]"
    button_burger = "//div[@class='header-desktop__catalog-burger']"
    button_catalog_1 = "//a[@data-attr='cataloglekarstvennyepreparaty']"
    button_catalog_2 = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/a"
    button_open_filter = "(//div[@class='bx_filter_parameters_box_title'])[3]"
    catalog_filter = "//input[@id='catalogFilter_P1_MIN']"
    button_filter = "//input[@id='set_filter']"
    select_filter = "(//input[@class='button button--large button--1'])[2]"
    catalog_word = "/html/body/div[3]/section[2]/div/h1"
    select_product_1 = "//a[@id='bx_359463013_60281_07d64dff100a5b1449d7c45e551996e6_buy_id']"
    product_title_locator_1 = "(//p[@class='product_name'])[3]"
    product_price_locator_1 = "//span[@id='bx_359463013_60281_07d64dff100a5b1449d7c45e551996e6_price']"
    select_product_2 = "//a[@id='bx_359463013_33157_8cce7393fbde258a40398406ac639c2d_buy_id']"
    product_title_locator_2 = "/html/body/div[3]/section[3]/div/div[2]/div[2]/div[4]/div/a[2]/p"
    product_price_locator_2 = "//span[@id='bx_359463013_33157_8cce7393fbde258a40398406ac639c2d_price']"
    button_cart = "(//a[@class='navbar__item-link'])[4]"

    # Getters

    def get_location_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location_menu)))

    def get_select_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_search)))

    def get_search_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_location)))

    def get_select_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_location)))

    def get_button_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_location)))
    def get_button_burger(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_burger)))

    def get_button_catalog_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog_1)))

    def get_catalog_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_word)))

    def get_catalog_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_filter)))

    def get_select_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_filter)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,  self.button_cart)))

    def get_product_title_1(self):
        """Получает название товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_title_locator_1))).text

    def get_product_title_2(self):
        """Получает название товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_title_locator_2))).text

    def get_product_price_1(self):
        """Получает цену первого товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_price_locator_1))).text

    def get_product_price_2(self):
        """Получает цену товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_price_locator_2))).text

    # Actions

    def click_location_menu(self):
        self.get_location_menu().click()
        print("click location menu")

    def input_select_search(self, user_name):
        self.get_select_search().send_keys(user_name)
        print("input select search")

    def click_search_location(self):
        self.get_search_location().click()
        print("click search location")

    def click_select_location(self):
        self.get_select_location().click()
        print("click select location")

    def click_button_location(self):
        self.get_button_location().click()
        print("click button location")

    def click_button_burger(self):
        self.get_button_burger().click()
        print("click button burger")

    def click_button_catalog_1(self):
        self.get_button_catalog_1().click()
        print("click button catalog 1")

    def input_catalog_filter(self, catalog_filter):
        self.get_catalog_filter().send_keys(catalog_filter)
        print("input catalog filter")

    def click_select_filter(self):
        self.get_select_filter().click()
        print("select filter")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("click select product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("click select product 2")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("click button cart")

    #Methods

    def buy_product(self): #self.driver указывает системе откуда брать драйвер
        self.get_current_url()
        time.sleep(14)
        self.click_location_menu()
        self.input_select_search("пер. Хользунова, д. 6")
        self.click_search_location()
        self.click_select_location()
        self.click_button_location()
        self.click_button_burger()
        self.click_button_catalog_1()
        self.assert_word(self.get_catalog_word(), "Лекарственные препараты")
        self.input_catalog_filter(500)
        self.click_select_filter()
        self.get_current_url()
        self.click_select_product_1()

        self.global_product_title_1 = self.get_product_title_1()  # Сохраняем название первого товара в глобальную переменную
        self.product_price_1 = self.get_product_price_1()  # Сохраняем цену первого товара
        print(f"Название товара 1: {self.global_product_title_1}")
        print(f"Цена товара 1: {self.product_price_1}")

        self.click_select_product_2()
        self.global_product_title_2 = self.get_product_title_2()  # Сохраняем название второго товара в глобальную переменную
        self.product_price_2 = self.get_product_price_2()  # Сохраняем цену второго товара
        print(f"Название товара 2: {self.global_product_title_2}")
        print(f"Цена товара 2: {self.product_price_2}")

        self.click_button_cart()
        time.sleep(3)
