from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url):
        """Открывает URL"""
        self.driver.get(url)

    def find_element(self, locator, timeout=5):
        """Находит элемент на странице"""
        by, value = locator
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Timeout: Элемент не найден по локатору: {locator} после {timeout} секунд")
            return None
        except NoSuchElementException:
            print(f"NoSuchElement: Элемент не найден по локатору: {locator}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def find_elements(self, locator, timeout=5):
        """Находит все элементы, соответствующие локатору"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except:
            raise Exception(f"Элементы не найдены по локатору: {locator}")

    def js_click(self, locator):
        """Кликает на элемент с помощью JavaScript"""
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise Exception(f"Невозможно кликнуть: Элемент не найден по локатору: {locator}")

    def get_text(self, locator):
        """Возвращает текст элемента."""
        element = self.find_element(locator)
        if element:
             return element.text
        else:
            return ""

    def send_keys(self, locator, text):
        """Добавлено для отправки текста элементу"""
        element = self.find_element(locator)
        element.send_keys(text)

    def clear(self, locator):
        """Функция для очистки поля перед вводом нового значения"""
        element = self.find_element(locator)
        element.clear()
