from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage

from pages.login_page import LoginPage


class Main_page():
    """Класс включающий сценарий покупки товара"""

def test_buy_product_1():
    """Тест по покупке товара включает:
             в себя авторизацию, выбор аптеки, выбор товара, подтверждение покупки."""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    print("Начало теста")

    login = LoginPage(driver)
    login.authorization()

    cp = CatalogPage(driver)
    cp.buy_product()

    cap = CartPage(driver)
    cap.select_product()

    if cp.global_product_title_1 == cap.global_order_title_1:
        print("Названия первого товара совпадают!")
    else:
        print("Названия первого товара не совпадают!")

    if cp.global_product_title_2 == cap.global_order_title_2:
        print("Названия второго товара совпадают!")
    else:
        print("Названия второго товара не совпадают!")

        # Убедимся, что названия совпадают
    assert cp.global_product_title_1 == cap.global_order_title_1, "Названия первого товара не совпадают!"
    assert cp.global_product_title_2 == cap.global_order_title_2, "Названия второго товара не совпадают!"

    if cp.product_price_1 == cap.order_price_1:
        print("Цены первого товара совпадают!")
    else:
        print("Цены первого товара не совпадают!")

    if cp.product_price_2 == cap.order_price_2:
        print("Цены второго товара совпадают!")
    else:
        print("Цены второго товара не совпадают!")

        # Убедимся, что цены совпадают
    assert cp.product_price_1 == cap.order_price_1, "Цены первого товара не совпадают!"
    assert cp.product_price_2 == cap.order_price_2, "Цены второго товара не совпадают!"
    print("Тест пройден успешно")




