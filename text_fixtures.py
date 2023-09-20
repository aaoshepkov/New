@pytest.fixture(scope="module")
def browser():
    # Инициализация веб-драйвера (здесь используется Chrome)
    driver = webdriver.Chrome()

    # Установка размера окна браузера
    driver.set_window_size(1200, 800)

    yield driver


    # Завершение работы браузера после выполнения тестов
    driver.quit()