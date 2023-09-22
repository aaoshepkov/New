from selene import be, have
from selene.support.shared import browser


def test_google_search():
    # Открытие Google
    browser.open("https://www.google.com")

    # Поиск по запросу "yashaka/selene"
    browser.element('#APjFqb').should(be.blank).type('yashaka/selene').press_enter()

    # Проверка наличия текста на странице
    browser.element('h3').should(have.text("yashaka/selene: User-oriented Web UI browser"))

def test_google_search_negative():
    # Открытие Google
    browser.open("https://www.google.com")

    # Поиск по запросу "yashaka/selene"
    browser.element('#APjFqb').should(be.blank).type('nvdjsnvkhsbdlkewjfoiahsdukfb').press_enter()

    # Проверка наличия текста на странице
    browser.element('#result-stats').should(have.text("Результатов: примерно 0"))