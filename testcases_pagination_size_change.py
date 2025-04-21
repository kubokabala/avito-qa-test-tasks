from telnetlib import EC
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObject import GameCatalogPage
from testcase_data import BASE_URL
from confest import browser


def test_navigation_buttons_w_nums_change_page(browser):
    """
    Тест: Проверяет, что при нажатии на кнопки навигации с цифрами происходит
    переход на соответствующую страницу. Проверяет по появлению класса 'ant-pagination-item-active'.
    Использует lambda-функцию для ожидания.
    """
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    PAGE_NUMBER_BUTTONS = (By.CSS_SELECTOR, "ul.ant-pagination.css-17a39f8 li[title][class*='ant-pagination-item']")

    ACTIVE_PAGE_BUTTON = (By.CSS_SELECTOR, "ul.ant-pagination.css-17a39f8 li.ant-pagination-item-active")

    PAGES_TO_TEST = list(range(1, 42))

    for page_number in PAGES_TO_TEST:
        try:
            page_buttons = catalog_page.find_elements(PAGE_NUMBER_BUTTONS)

            target_button = None
            for button in page_buttons:
                if button.text == str(page_number):
                    target_button = button
                    break

            if not target_button:
                pytest.fail(f"Кнопка страницы {page_number} не найдена")

            target_button.click()

            WebDriverWait(browser, 10).until(
                lambda driver: f"ant-pagination-item-{page_number} ant-pagination-item-active" in catalog_page.find_element(ACTIVE_PAGE_BUTTON).get_attribute("class")
            )
            print(f"Успешно: Переход на страницу {page_number} выполнен")

        except TimeoutException:
            pytest.fail(f"Таймаут при ожидании загрузки страницы {page_number}")
        except Exception as e:
            pytest.fail(f"Ошибка при переходе на страницу {page_number}: {e}")

def test_navigation_arrows_change_page(browser):
    """
    Тест: Переключается между страницами с помощью кнопок-стрелок.
    Два шага вперед, один назад, от первой до последней страницы.
    (так мы проверим сразу и левую, и правую кнопку на каждой странице)
    """
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "li[title='Next Page'] button")
    PREVIOUS_PAGE_BUTTON = (By.CSS_SELECTOR, "li[title='Previous Page'] button")

    ACTIVE_PAGE_BUTTON = (By.CSS_SELECTOR, "ul.ant-pagination.css-17a39f8 li.ant-pagination-item-active")

    current_page = 1
    last_page = 41

    while current_page < last_page:
        try:
            #Два шага вперед
            for _ in range(2):
                if current_page < last_page:
                    next_button = catalog_page.find_element(NEXT_PAGE_BUTTON)
                    next_button.click()
                    current_page += 1

                    WebDriverWait(browser, 10).until(
                        lambda driver: f"ant-pagination-item-{current_page} ant-pagination-item-active" in catalog_page.find_element(ACTIVE_PAGE_BUTTON).get_attribute("class")
                    )
                else:
                    break  # На последней странице

            # Шаг назад (если мы не на первой странице)
            if current_page > 1:
                prev_button = catalog_page.find_element(PREVIOUS_PAGE_BUTTON)
                prev_button.click()
                current_page -= 1

                WebDriverWait(browser, 10).until(
                    lambda driver: f"ant-pagination-item-{current_page} ant-pagination-item-active" in catalog_page.find_element(ACTIVE_PAGE_BUTTON).get_attribute("class")
                )

        except TimeoutException:
            pytest.fail(f"Таймаут при переходе на страницу {current_page}")
        except Exception as e:
            pytest.fail(f"Ошибка при переходе на страницу {current_page}: {e}")

    print("Тест завершен: достигли последней страницы.")

def test_navigation_jump_buttons(browser):
    """
    Тест: Проверяет навигацию с помощью кнопок "Next 5 Pages" и "Previous 5 Pages".
    """
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    NEXT_5_PAGES_BUTTON = (By.CSS_SELECTOR, "li[title='Next 5 Pages'] a")
    PREVIOUS_5_PAGES_BUTTON = (By.CSS_SELECTOR, "li[title='Previous 5 Pages'] a")
    ACTIVE_PAGE_BUTTON = (By.CSS_SELECTOR, "ul.ant-pagination.css-17a39f8 li.ant-pagination-item-active")

    current_page = 1
    last_page = 41

    try:
        # Движение вперед
        while current_page + 5 <= last_page:
            next_5_button = catalog_page.find_element(NEXT_5_PAGES_BUTTON)
            next_5_button.click()
            current_page += 5
            WebDriverWait(browser, 10).until(
                lambda driver: f"ant-pagination-item-{current_page}" in catalog_page.find_element(ACTIVE_PAGE_BUTTON).get_attribute("class")
            )

        # Движение назад
        while current_page > 1:
            prev_5_button = catalog_page.find_element(PREVIOUS_5_PAGES_BUTTON)
            prev_5_button.click()
            current_page -= 5
            WebDriverWait(browser, 10).until(
                lambda driver: f"ant-pagination-item-{current_page}" in catalog_page.find_element(ACTIVE_PAGE_BUTTON).get_attribute("class")
            )

    except TimeoutException:
        pytest.fail(f"Таймаут при переходе на страницу {current_page}")
    except Exception as e:
        pytest.fail(f"Ошибка при переходе на страницу {current_page}: {e}")

    print("Тест завершен.")