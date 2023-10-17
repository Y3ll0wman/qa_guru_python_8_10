from selene import browser, be, have
from qa_guru_python_8_10 import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').should(be.visible).type(user.last_name)
        browser.element('#userEmail').should(be.visible).type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').should(be.visible).type(user.phone_number)
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({user.month_of_brith})').should(be.visible).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({user.year_of_brith})').should(be.visible).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{user.day_of_brith}').should(be.visible).click()
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        if 'Sports' in user.hobby:
            browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
        if 'Reading' in user.hobby:
            browser.element('label[for=hobbies-checkbox-2]').should(be.visible).click()
        if 'Music' in user.hobby:
            browser.element('label[for=hobbies-checkbox-3]').should(be.visible).click()
        browser.element('#uploadPicture').should(be.visible).type(resource.path(user.picture))
        browser.element('#currentAddress').should(be.visible).type(user.current_address)
        browser.element("#react-select-3-input").should(be.visible).type(user.state).press_enter()
        browser.element("#react-select-4-input").should(be.visible).type(user.city).press_enter()
        browser.element("#submit").should(be.visible).click()

    def student_should_by_registred(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f"{user.day_of_brith.replace('0', '')} "
            f"{user.month_of_brith.replace('5', 'May')},"
            f"{user.year_of_brith.replace('20', '1919')}",
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.city}'
        ))
