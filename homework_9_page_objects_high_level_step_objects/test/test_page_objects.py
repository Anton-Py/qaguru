from homework_9_page_objects_high_level_step_objects.data.users import User
from homework_9_page_objects_high_level_step_objects.pages.registration_page import RegistrationPage


def test_practice_form_filling():
    registration_page = RegistrationPage()
    registration_page.open_page()

    my_user = User(
        first_name='Anton',
        last_name='Lyakh',
        email='first@email.ru',
        gender='Male',
        phone_number='9130017081',
        year='1988',
        month='November',
        day='18',
        subjects='Economics',
        hobbies='Sports',
        picture='picture.png',
        address='SNovosibirsk, Griboedova 80',
        state='Haryana',
        city='Karnal'
    )

    registration_page.fill_user_data_in_registration_form(my_user)
    registration_page.should_open_form_with_text(my_user)
