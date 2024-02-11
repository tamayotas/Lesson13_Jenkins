from selene import browser, have, be, by
from demoqa_tests import resource
from tests import conftest


class RegistrationPage:
    browser = conftest.setup_browser

    def open_registration_page(self):
        browser.open('/automation-practice-form')
        browser.element('.main-header').should(have.text('Practice Form'))
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def gender_selection(self, value):
        if value == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif value == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
        return self

    def fill_user_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(month)
        ).click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(year)
        ).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_user_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def user_hobby_checkbox(self, value):
        if value == "Sports":
            browser.element("[for='hobbies-checkbox-1']").click()
        elif value == "Reading":
            browser.element("[for='hobbies-checkbox-2']").click()
        elif value == "Music":
            browser.element("[for='hobbies-checkbox-3']").click()
        return self

    def user_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))
        return self

    def user_current_adress(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def user_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def user_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit_the_form(self):
        browser.element('#submit').press_enter()
        return self

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        number,
        date_of_birth,
        subjects,
        hobbies,
        file,
        current_address,
        state_and_city,
    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                file,
                current_address,
                state_and_city,
            )
        )
        return self

    def close_the_form(self):
        browser.element('#closeLargeModal').press_enter()
        return self