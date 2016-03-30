from selenium.webdriver.common.by import By

from signin import SignInPage


class HomePage(SignInPage):

    _url = '{base_url}/user/sign-in'

    _create_survey_top_link_locator = (By.LINK_TEXT, '+ Create Survey')
    _account_tab_main_menu_locator = (By.ID, 'userAcctTab_MainMenu')
    _sign_out_link_locator = (By.LINK_TEXT, 'Sign Out')

    @property
    def is_create_survey_top_link_displayed(self):
        return self.is_element_displayed(self._create_survey_top_link_locator)

    @property
    def is_account_tab_main_menu_displayed(self):
        return self.is_element_displayed(self._account_tab_main_menu_locator)

    @property
    def is_sign_out_link_displayed(self):
        return self.is_element_displayed(self._sign_out_link_locator)

    def create_survey_via_top_link(self):
        self.find_element(self._create_survey_top_link_locator).click()

    def sign_out(self):
        self.scroll_element_into_view(self._account_tab_main_menu_locator)
        self.find_element(self._account_tab_main_menu_locator).click()
        if self.is_sign_out_link_displayed:
            self.find_element(self._sign_out_link_locator).click()
