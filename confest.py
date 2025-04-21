import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="session")
def browser(request):
    """
    Фикстура для инициализации браузера.
    Поддерживает Chrome.
    """
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")  # Запуск в headless режиме, если нужно
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.implicitly_wait(10)  # Неявное ожидание
    yield driver
    driver.quit()
