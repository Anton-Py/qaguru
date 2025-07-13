from homework_9_page_objects.pages.registration_page import RegistrationPage
from selene import browser, be, have
import os


def test_practice_form_filling():
    registration_page = RegistrationPage()

    registration_page.open_page()
    registration_page.fill_name("Anton")
    registration_page.fill_lastname("Lyakh")
    registration_page.fill_email("first@email.ru")
    registration_page.choose_gender()
    registration_page.fill_user_number("9130017081")
    registration_page.fill_users_birthday('[value="10"]', '[value="1988"]')
    registration_page.fill_subjects("Economics")
    registration_page.fill_users_hobbies()
    registration_page.picture_upload()
    registration_page.fill_current_address('Novosibirsk, Griboedova 80', 'Haryana', 'Karnal')

    # confirmation of form completion
    registration_page.submit_button()

    # checking the results table
    registration_page.should_open_form_with_text(
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
