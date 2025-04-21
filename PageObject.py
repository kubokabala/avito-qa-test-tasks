from BasePage import BasePage


class GameCatalogPage(BasePage):
    """
    Page Object для страницы каталога игр.
    Определяет локаторы и методы для взаимодействия с элементами.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        """Открывает страницу каталога."""
        self.open_url(url)

    def get_number_of_game_cards(self):
        """Количество карточек игр на странице"""
        cards = self.find_elements(self.GAME_CARD)
        return len(cards)

    def click_next_page(self):
        """Переходит на следующую страницу"""
        self.js_click(self.PAGINATION_NEXT_BUTTON)

