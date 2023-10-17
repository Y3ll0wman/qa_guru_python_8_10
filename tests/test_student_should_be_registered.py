import os
from selene import browser, be, have


def test_student_registration_form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").should(be.visible).type("Vasya")
    browser.element("#lastName").should(be.visible).type("Vasilyev")
    browser.element("#userEmail").should(be.visible).type("example@example.com")
    browser.element("[for='gender-radio-1']").should(be.visible).click()
    browser.element("#userNumber").should(be.visible).type("7999999999")
    browser.element("#dateOfBirthInput").should(be.visible).click()
    browser.element(".react-datepicker__month-select").should(be.visible).click()
    browser.element(".react-datepicker__month-select > option:nth-child(5)").should(be.visible).click()
    browser.element(".react-datepicker__year-select").should(be.visible).click()
    browser.element(".react-datepicker__year-select > option:nth-child(20)").should(be.visible).click()
    browser.element(".react-datepicker__day.react-datepicker__day--012").should(be.visible).click()
    browser.element("#subjectsInput").should(be.visible).type("Computer Science").press_enter()
    browser.element("label[for='hobbies-checkbox-1']").should(be.visible).click()
    browser.element("label[for='hobbies-checkbox-2']").should(be.visible).click()
    browser.element("label[for='hobbies-checkbox-3']").should(be.visible).click()
    browser.element("#uploadPicture").should(be.visible).type(os.path.abspath("pictures/avatar.png"))
    browser.element("#currentAddress").should(be.visible).type("Palace Square, 2, St Petersburg, 190000")
    browser.element("#react-select-3-input").should(be.visible).type("NCR").press_enter()
    browser.element("#react-select-4-input").should(be.visible).type("Delhi").press_enter()
    browser.element("#submit").should(be.visible).click()
    browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
        "Vasya Vasilyev",
        "example@example.com",
        "Male",
        "7999999999",
        "12 May,1919",
        "Computer Science",
        "Sports, Reading, Music",
        "avatar.png",
        "Palace Square, 2, St Petersburg, 190000",
        "NCR Delhi"
    ))
    browser.element("#closeLargeModal").should(be.visible).click()