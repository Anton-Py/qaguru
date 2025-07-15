from selene import browser, be, have
import os


class RegistrationPage:

    def open_page(self):
        browser.open("")

    def fill_name(self, value):
        browser.element("#firstName").should(be.visible).type(value)

    def fill_lastname(self, value):
        browser.element("#lastName").should(be.visible).type(value)

    def fill_email(self, value):
        browser.element("#userEmail").should(be.visible).type(value)

    def choose_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_user_number(self, value):
        browser.element("#userNumber").should(be.visible).type(value)

    def fill_users_birthday(self, month, year):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").should(be.visible).element(month).click()
        browser.element(".react-datepicker__year-select").should(be.visible).element(year).click()
        browser.element('[aria-label="Choose Friday, November 18th, 1988"]').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_users_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def picture_upload(self):
        file_path = os.path.join(os.path.dirname(__file__), '../files/picture.png')
        browser.element('#uploadPicture').send_keys(os.path.abspath(file_path))

    def fill_current_address(self, address, state, city):
        browser.element('#currentAddress').should(be.visible).type(address).click()
        browser.element('#react-select-3-input').should(be.visible).type(state).press_enter()
        browser.element('#react-select-4-input').should(be.visible).type(city).press_enter()

    def submit_button(self):
        browser.element('#submit').click()

    def should_open_form_with_text(self, *value):
        browser.element('//table').all('td').should(have.exact_texts(value))
