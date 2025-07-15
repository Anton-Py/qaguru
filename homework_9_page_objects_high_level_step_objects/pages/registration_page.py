from selene import browser, be, have
import os


class RegistrationPage:

    def open_page(self):
        browser.open("")

    def fill_user_data_in_registration_form(self, user, gender=None):
        browser.element("#firstName").should(be.visible).type(user.first_name)
        browser.element("#lastName").should(be.visible).type(user.last_name)
        browser.element("#userEmail").should(be.visible).type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element("#userNumber").should(be.visible).type(user.phone_number)
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(user.hobbies)).click()
        file_path = os.path.join(os.path.dirname(__file__), f'../files/{user.picture}')
        # file_path = f'../files/{user.picture}'
        browser.element('#uploadPicture').send_keys(os.path.abspath(file_path))
        browser.element('#currentAddress').should(be.visible).type(user.address).click()
        browser.element('#react-select-3-input').should(be.visible).type(user.state).press_enter()
        browser.element('#react-select-4-input').should(be.visible).type(user.city).press_enter()

        browser.element('#submit').click()

    def should_open_form_with_text(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        )
        )
