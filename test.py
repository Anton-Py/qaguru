from selene import browser, have

def test_table_texts_selene():
    browser.open("https://demoqa.com/automation-practice-form")

    # browser.element("customers").all("tr").should(have.exact_texts(
    #
    # ))