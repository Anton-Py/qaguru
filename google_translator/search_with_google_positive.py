from selene import browser, have, by, be

def test_captcha_should_be_shown():
    # Открываем браузер Google
    browser.open('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    # Находим элемент для ввода текста и жмем Enter
    browser.element('[name="q"]').type('Основы Python').press_enter()
    # Находим элемент с текстом 'Об этой странице'
    browser.element('b').should(have.text('Об этой странице'))


