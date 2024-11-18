from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class CartPage(Base):

    order_price_1 = None  # Атрибут для хранения цены первого товара в корзине
    order_price_2 = None  # Атрибут для хранения цены второго товара в корзине
    global_order_title_1 = ""
    global_order_title_2 = ""

    def __init__(self, driver):  # добавляем driver для того чтобы содержать шаги по авторизации
        super().__init__(driver)
        self.driver = driver
        self.final_price: float | None = None  # Инициализация атрибута экземпляра


    # Locators

    cart_word = "/html/body/div[3]/section[1]/div/ul/li[2]/span"
    button_order = "//input[@class='cart__order-button']"
    order_title_locator_1 = "(//a[@class='page-link'])[1]"
    order_title_locator_2 = "(//a[@class='page-link'])[2]"
    order_price_locator_1 = "(//div[@class='summary'])[1]"
    order_price_locator_2 = "(//div[@class='summary'])[2]"
    final_price_locator = "/html/body/div[3]/div[1]/section/div/div[1]/div/div[2]/div/div/div/div/div[2]/span[2]"

    # Getters

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

    def get_order_title_1(self):
        """Получает название товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.order_title_locator_1))).text

    def get_order_title_2(self):
        """Получает название товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.order_title_locator_2))).text

    def get_order_price_1(self):
        """Получает цену товара"""
        price = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.order_price_locator_1))
        ).text
        return price

    def get_order_price_2(self):
        """Получает цену товара"""
        price = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.order_price_locator_2))
        ).text
        return price

    def calculate_total_order_price(self):
        """Метод для расчёта общей цены товаров"""
        # Сохраняем значения цен в атрибуты
        self.order_price_1 = self.get_order_price_1()  # Сохраняем цену первого товара
        self.order_price_2 = self.get_order_price_2()  # Сохраняем цену второго товара

        # Обработка строк для получения числовых значений
        try:
            order_price_1 = float(self.order_price_1.replace(' руб.', '').replace(' ', '').replace('₽', ''))
            order_price_2 = float(self.order_price_2.replace(' руб.', '').replace(' ', '').replace('₽', ''))
        except TypeError:
            print("Цены не заданы (None). Проверьте визуальные локаторы или состояние элементов.")
            return 0.0  # Возвращаем 0, если возникла ошибка
        except ValueError as e:
            print(f"Ошибка при преобразовании цен: {e}")
            return 0.0  # Возвращаем 0, если возникла ошибка

        # Считаем общую цену
        total_order_price = order_price_1 + order_price_2
        print(f"Цена 1: {int(order_price_1)} ₽, Цена 2: {int(order_price_2)} ₽, Общая сумма: {int(total_order_price)} ₽")
        return total_order_price  # Возвращаем общую цену

    def get_final_price(self):
        try:
            # Ожидание появления элемента на странице
            final_price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.final_price_locator))
            )
            final_price_text = final_price_element.text.strip()  # Извлечение текста и удаление лишних пробелов
            # Добавьте обработку для преобразования текста в число, если необходимо
            return float(final_price_text.replace('₽', '').replace(' ', ''))  # Преобразование в float
        except Exception as e:
            print(f"Ошибка при получении финальной цены: {e}")
            return None  # Вернуть None в случае ошибки


    # Actions

    def click_button_order(self):
        self.get_button_order().click()
        print("click button order")

    # Methods
    def select_product(self):
        self.get_current_url()  # Переход на текущий URL
        self.assert_word(self.get_cart_word(), "Корзина")
        self.global_order_title_1 = self.get_order_title_1()
        self.order_price_1 = self.get_order_price_1()
        print(f"Название товара 1: {self.global_order_title_1}")
        print(f"Цена товара 1: {self.order_price_1}")  # Отладочное сообщение

        self.global_order_title_2 = self.get_order_title_2()
        self.order_price_2 = self.get_order_price_2()
        print(f"Название товара 2: {self.global_order_title_2}")
        print(f"Цена товара 2: {self.order_price_2}")  # Отладочное сообщение

        if self.order_price_1 is None or self.order_price_2 is None:
            print("Цены не были установлены. Проверьте локаторы.")
            return

        total_order_price = self.calculate_total_order_price()  # Вызов метода для расчёта общей цены
        self.final_price = self.get_final_price()  # Инициализация final_price

        if self.final_price is None:
            print("Не удалось получить финальную цену. Проверьте локаторы или логику.")
            return

        try:
            self.final_price = int(float(self.final_price))  # Преобразование финальной цены в целое число
            print(f"Финальная цена: {self.final_price} ₽")

            # Сравнение final_price и total_order_price
            if total_order_price == self.final_price:
                print("Общая сумма совпадает с финальной ценой.")
            else:
                print(f"Общая сумма {total_order_price} ₽ не совпадает с финальной ценой {self.final_price} ₽.")

        except ValueError as e:
            print(f"Ошибка преобразования финальной цены: {e}. Проверьте, что цена имеет корректный формат.")

        self.click_button_order()