from selene import browser, be, have
import os


def test_practice_form_filling():
    browser.open("/")

    # first_name
    browser.element("#firstName").should(be.visible).type('Anton')

    # last_name
    browser.element("#lastName").should(be.visible).type('Lyakh')

    # email
    browser.element("#userEmail").should(be.visible).type('first@email.ru')
    browser.element('[for="gender-radio-1"]').click()

    # user_number
    browser.element("#userNumber").should(be.visible).type('9130017081')

    # birth
    browser.element("#dateOfBirthInput").click()

    # month
    browser.element(".react-datepicker__month-select").should(be.visible).element('[value="10"]').click()

    # year
    browser.element(".react-datepicker__year-select").should(be.visible).element('[value="1988"]').click()
    browser.element('[aria-label="Choose Friday, November 18th, 1988"]').click()

    # subjects
    browser.element('#subjectsInput').type('Economics').press_enter()

    # hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()

    # picture_upload
    file_path = 'files/picture.png'
    browser.element('#uploadPicture').send_keys(os.path.abspath(file_path))

    # current_address
    browser.element('#currentAddress').should(be.visible).type('Novosibirsk, Griboedova 80').click()
    browser.element('#react-select-3-input').should(be.visible).type('Haryana').press_enter()
    browser.element('#react-select-4-input').should(be.visible).type('Karnal').press_enter()

    # submit
    browser.element('#submit').click()

    # checking the results table
    browser.element('//table').all('td').should(
        have.exact_texts(
            'Student Name', 'Anton Lyakh',
            'Student Email', 'first@email.ru',
            'Gender', 'Male',
            'Mobile', '9130017081',
            'Date of Birth', '18 November,1988',
            'Subjects', 'Economics',
            'Hobbies', 'Sports',
            'Picture', 'picture.png',
            'Address', 'Novosibirsk, Griboedova 80',
            'State and City', 'Haryana Karnal'
        )
    )
