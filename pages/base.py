from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page import Page


class BasePage(Page):

    _url = '{base_url}'

    def __init__(self, base_url, selenium):
        super(BasePage, self).__init__(base_url, selenium)

    def wait_for_page_to_load(self):
        super(BasePage, self).wait_for_page_to_load()
        return self
