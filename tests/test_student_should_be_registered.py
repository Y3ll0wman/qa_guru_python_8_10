from qa_guru_python_8_10.pages.registration_page import RegistrationPage
from qa_guru_python_8_10.data.users import User

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    student = User(first_name='Vasya', last_name='Vasilyev', email='example@example.com', gender='Male', phone_number='7999999999',
                   month_of_brith='5', year_of_brith='20', day_of_brith='012', subject='Computer Science',
                   hobby='Sports, Reading, Music', picture='avatar.png', current_address='Palace Square, 2, St Petersburg, 190000', state='NCR',
                   city='Delhi')
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.student_should_by_registred(student)
