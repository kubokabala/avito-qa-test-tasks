from telnetlib import EC
from selenium.webdriver import Keys
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObject import GameCatalogPage
from testcase_data import BASE_URL, PAGE_SIZES
from confest import browser


def test_display_different_number_of_game_cards(browser):
    """
    Тест: Отображение разного количества карточек игр на странице поиска,
    ввод значения в текстовое поле и сверка с фактическим количеством.
    """
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    GAME_CARDS = (By.XPATH, "//div[@class='_container_vlg32_23']")

    PAGE_SIZE_INPUT = (
        By.XPATH,
        "//div[@class='ant-select ant-pagination-options-size-changer css-17a39f8 ant-select-single ant-select-show-arrow ant-select-show-search']//input[@class='ant-select-selection-search-input']",
    )

    for page_size in PAGE_SIZES[2]:
        try:
            input_field = catalog_page.find_element(PAGE_SIZE_INPUT)
            input_field.clear()  # Используем метод clear из Selenium
            input_field.send_keys(str(page_size))
            input_field.send_keys(Keys.ENTER)

            WebDriverWait(catalog_page.driver, 5).until(
                lambda driver: len(catalog_page.find_elements(GAME_CARDS)) == page_size
            )

            game_cards = catalog_page.find_elements(GAME_CARDS)
            actual_card_count = len(game_cards)

            print("\n")
            assert (
                actual_card_count == page_size
            ), f"Ожидалось {page_size} карточек, отображается {actual_card_count}"
            print(
                f"Успешно: Отображается {actual_card_count} карточек (ожидалось {page_size})"
            )
            previous_page_size = page_size


        except TimeoutException as e:
            pytest.fail(
                f"Ошибка сайта: Не получается перейти с {previous_page_size} количества карточек на {page_size} количество карточек. Ошибка: {e}"
            )
        except Exception as e:
            pytest.fail(
                f"Ошибка при проверке количества карточек на странице ({page_size} карточек). Ошибка: {e}"
            )