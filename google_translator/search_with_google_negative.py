from selene import browser, have, by, be
import time

def test_search_negative():
    # Открываем браузер Yandex
    browser.open('https://ya.ru')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    # Находим элемент и вводим текст для поиска
    browser.element('[name="text"]').should(be.blank).type('уtgbyhnujm').press_enter()
    # Находим текст 'Ничего не нашли'
    browser.element('[class="EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))