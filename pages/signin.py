from selenium.webdriver.common.by import By

from base import BasePage


class SignInPage(BasePage):

    _url = '{base_url}/user/sign-in'

    _username_locator = (By.ID, 'username')
    _password_locator = (By.ID, 'password')
    _sign_in_button_locator = (By.XPATH, '//button[@type="submit"]')
    _remember_me_checkbox_locator = (By.ID,'remember_me')

    @property
    def is_username_displayed(self):
        return self.is_element_displayed(self._username_locator)

    @property
    def is_password_displayed(self):
        return self.is_element_displayed(self._password_locator)

    @property
    def is_sign_in_button_displayed(self):
        return self.is_element_displayed(self._sign_in_button_locator)

    @property
    def is_remember_me_checked(self):
        return self.find_element(self._remember_me_checkbox_locator).is_selected()

    def type_username(self,value):
        self.find_element(self._username_locator).send_keys(value)

    def type_password(self,value):
        self.find_element(self._password_locator).send_keys(value)

    def click_user_sign_in(self):
        self.find_element(self._sign_in_button_locator).click()

    def check_remember_me(self):
        if not self.is_remember_me_checked:
            self.find_element(self._remember_me_checkbox_locator).click()

    def user_sign_in(self,username,password):
        self.type_username(username)
        self.type_password(password)
        self.check_remember_me()
        self.click_user_sign_in()



