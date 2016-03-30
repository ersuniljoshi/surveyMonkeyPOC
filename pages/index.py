from selenium.webdriver.common.by import By

from base import BasePage


class IndexPage(BasePage):

    _url = '{base_url}'

    _sign_in_locator = (By.CLASS_NAME,'sign-in')

    @property
    def is_signin_displayed(self):
        return self.is_element_displayed(self._sign_in_locator)

    def click_sign_in(self):
        self.find_element(self._sign_in_locator).click()