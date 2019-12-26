from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_1_input.send_keys(password)
        password_2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url,  "URL Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert  self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Register form is not presented"

    