from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from PageObject import GameCatalogPage
from testcase_data import BASE_URL
from confest import browser


def test_open_game_card(browser):
    """
    Тест: Открытие карточки игры по имени и проверка заголовка.
    """
    GAME_NAME = "Tarisland"
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    GAME_CARD_BY_NAME = (By.XPATH, f"//div[@class='_container_vlg32_23']//h1[text()='{GAME_NAME}']//ancestor::div[@class='_container_vlg32_23']")


    GAME_INFO_PAGE_TITLE = (By.CSS_SELECTOR, "h2.ant-typography")

    try:
        catalog_page.js_click(GAME_CARD_BY_NAME)
    except Exception as e:
        pytest.fail(f"Не удалось найти карточку игры с именем '{GAME_NAME}'. Ошибка: {e}")

    try:
        game_title = catalog_page.get_text(GAME_INFO_PAGE_TITLE)
        assert game_title == GAME_NAME, f"Ожидалось, что откроется страница игры '{GAME_NAME}', но открылась '{game_title}'"
        print(f"Открыта страница игры: {game_title}")

    except Exception as e:
        pytest.fail(f"Страница информации об игре не загрузилась или не содержит ожидаемого заголовка. Ошибка: {e}")

def test_open_all_game_cards(browser):
    """
    Тест: Открытие всех карточек игр на странице и проверка заголовка,
    с возвратом на главную страницу по кнопке 'Back to main'.
    """
    catalog_page = GameCatalogPage(browser)
    catalog_page.open(BASE_URL)

    GAME_CARDS = (By.XPATH, "//div[@class='_container_vlg32_23']")
    GAME_INFO_PAGE_TITLE = (By.CSS_SELECTOR, "h2.ant-typography")
    BACK_TO_HOME_BUTTON = (By.XPATH, "//button[@class='ant-btn css-17a39f8 ant-btn-primary ant-btn-lg']")
    game_cards = catalog_page.find_elements(GAME_CARDS)

    assert game_cards, "На странице не найдено ни одной карточки игры."

    for i in range(len(game_cards)):
        try:
            game_cards = catalog_page.find_elements(GAME_CARDS)
            card = game_cards[i]

            try:
                game_name_element = card.find_element(By.XPATH, ".//h1")
            except NoSuchElementException:
                game_name_element = card.find_element(By.XPATH, ".//h2")

            game_name = game_name_element.text
            GAME_CARD_BY_NAME = (By.XPATH, f"//div[@class='_container_vlg32_23']//h1[text()='{game_name}']//ancestor::div[@class='_container_vlg32_23']")

            catalog_page.js_click(GAME_CARD_BY_NAME)

            try:
                game_title = catalog_page.get_text(GAME_INFO_PAGE_TITLE)
                assert game_title == game_name, f"Ожидалось, что откроется страница игры '{game_name}', но открылась '{game_title}'"
                # print(f"Открыта страница игры: {game_title}")
            except Exception as e:
                pytest.fail(f"Страница информации об игре для '{game_name}' не загрузилась или не содержит ожидаемого заголовка. Ошибка: {e}")

            try:
                back_button = catalog_page.find_element(BACK_TO_HOME_BUTTON)
                back_button.click()
            except Exception as e:
                pytest.fail(f"Не удалось кликнуть на кнопку возврата на главную страницу для игры '{game_name}'. Ошибка: {e}")

        except Exception as e:
            pytest.fail(f"Не удалось обработать карточку игры. Ошибка: {e}")