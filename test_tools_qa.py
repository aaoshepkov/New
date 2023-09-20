import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Импортируем By для использования селектора по имени


@pytest.fixture(scope="module")
def browser():
    # Инициализация веб-драйвера (здесь используется Chrome)
    driver = webdriver.Chrome()

    # Установка размера окна браузера
    driver.set_window_size(1200, 800)

    yield driver


    # Завершение работы браузера после выполнения тестов
    driver.quit()


def test_google_search(browser):
    # Открытие Google
    browser.get("https://www.google.com")

    # Поиск по запросу "yashaka/selene"
    search_input = browser.find_element(By.NAME, "q")  # Используем By.NAME для поиска по имени
    search_input.send_keys("yashaka/selene")
    search_input.send_keys(Keys.RETURN)

    # Проверка наличия текста на странице
    assert "yashaka/selene: User-oriented Web UI browser tests in ..." in browser.page_source
