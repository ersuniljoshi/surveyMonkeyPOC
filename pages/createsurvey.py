from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from homepage import HomePage
import time


class CreateSurveyPage(HomePage):

    _url = '{base_url}/user/sign-in'

    _survey_title_locator = (By.ID, 'newName')
    _survey_category_dropdown_locator = (By.ID, 'newCategory')
    _letsgo_link_locator = (By.LINK_TEXT, "Let's Go!")
    _survey_edit_title_bar_locator = (By.XPATH, '//span[text()="+ Add Page Title"]')
    _survey_edit_page_title_locator = (By.ID, 'pageTitle')
    _survey_edit_page_title_description_locator = (By.ID, 'pageSubtitle')
    _survey_edit_page_title_save_locator = (By.LINK_TEXT, 'Save')
    _survey_edit_page_title_cancel_locator = (By.LINK_TEXT, 'Cancel')

    _survey_done_locator = (By.CSS_SELECTOR,'btn.small.survey-page-button.done-button.notranslate')

    _question_area_locator = (By.CSS_SELECTOR,'div.questions.clearfix.ui-sortable')

    @property
    def is_survey_title_displayed(self):
        return self.is_element_displayed(self._survey_title_locator)

    @property
    def is_survey_category_displayed(self):
        return self.is_element_displayed(self._survey_category_dropdown_locator)

    @property
    def is_letsgo_link_displayed(self):
        return self.is_element_displayed(self._letsgo_link_locator)

    @property
    def is_page_title_bar_displayed(self):
        return self.is_element_displayed(self._survey_edit_title_bar_locator)

    def type_survey_title(self,value):
        self.find_element(self._survey_title_locator).send_keys(value)

    def select_survey_category(self,value):
        el = self.find_element(self._survey_category_dropdown_locator)
        Select(el).select_by_visible_text(value)

    def click_letsgo(self):
         self.find_element(self._letsgo_link_locator).click()

    def type_page_title(self,value):
        self.find_element(self._survey_edit_page_title_locator).send_keys(value)

    def type_page_title_description(self,value):
        self.find_element(self._survey_edit_page_title_description_locator).send_keys(value)

    def click_add_page_title(self):
        self.find_element(self._survey_edit_title_bar_locator).click()

    def click_save_page_title_and_description(self):
        self.find_element(self._survey_edit_page_title_save_locator).click()

    def click_done_survey(self):
        self.scroll_element_into_view(self._survey_done_locator)
        self.find_element(self._survey_done_locator).click()

    def add_survey_name_and_category(self, surveyname, surveycategory):
        if self.is_survey_title_displayed:
            self.type_survey_title(surveyname)
            self.select_survey_category(surveycategory)
            self.click_letsgo()

    def add_page_title_and_description(self, pagetitle, pagedesc):
        self.click_add_page_title()
        self.type_page_title(pagetitle)
        self.type_page_title_description(pagedesc)
        self.click_save_page_title_and_description()


class Builder(CreateSurveyPage):

    _url = '{base_url}/user/sign-in'

    # Locators for Multiple Choice Questions in Builder
    _multiple_choice_question_locator = (By.CLASS_NAME, 'qmc')
    _multiple_choice_question_add_locator = (By.XPATH, '//id("builderQues tionContainer")/x:ul/x:li[1]/x:a')

    # Locators for DropDown Questions in Builder
    _drop_down_question_locator = (By.CLASS_NAME,'qdd')
    _drop_down_question_add_locator = (By.XPATH,'//id("builderQuestionContainer")/x:ul/x:li[2]/x:a')

    # Locators for DropDown Questions in Builder
    _ranking_question_locator = (By.CLASS_NAME,'qrk')
    _ranking_question_add_locator = (By.XPATH,'//id("builderQuestionContainer")/x:ul/x:li[5]/x:a')

    # Locators for Single TextBox Questions in Builder
    _single_textbox_question_locator = (By.CLASS_NAME,'qst')
    _single_textbox_add_locator = (By.XPATH,'//id("builderQuestionContainer")/x:ul/x:li[7]/x:a')

    # Locators for Single TextBox Questions in Builder
    _multiple_textbox_question_locator = (By.CLASS_NAME,'qmt')
    _multiple_textbox_add_locator = (By.XPATH,'//id("builderQuestionContainer")/x:ul/x:li[8]/x:a')

    _question_section_locator = (By.CSS_SELECTOR,'.questions.clearfix.ui-sortable')
    _question_text_locator = (By.ID, 'editTitle')
    _question_add_answer_bulk_locator = (By.ID, 'addBulkAns')
    _question_add_answer_bulk_textarea_locator = (By.CSS_SELECTOR, 'textarea.bulk-add-input')
    _question_add_answer_bulk_save_locator = (By.CSS_SELECTOR, 'a.btn.teal.btn-txt-primary')
    _question_save_locator = (By.CSS_SELECTOR, 'a.btn.teal.save')

    @property
    def is_multiple_choice_question_add_displayed(self):
        return self.is_element_displayed(self._multiple_choice_question_add_locator)

    @property
    def is_ranking_question_add_displayed(self):
        return self.is_element_displayed(self._ranking_question_add_locator)

    @property
    def is_drop_down_question_add_displayed(self):
        return self.is_element_displayed(self._drop_down_question_add_locator)

    @property
    def is_single_textbox_question_add_displayed(self):
        return self.is_element_displayed(self._single_textbox_add_locator)

    @property
    def is_multiple_textbox_question_add_displayed(self):
        return self.is_element_displayed(self._multiple_textbox_add_locator)

    @property
    def is_question_section_displayed(self):
        return self.is_element_displayed(self._question_section_locator)

    @property
    def is_question_text_displayed(self):
        return self.is_element_displayed(self._question_text_locator)

    @property
    def is_question_add_answer_bulk_save_displayed(self):
        return self.is_element_displayed(self._question_add_answer_bulk_save_locator)

    @property
    def is_question_save_displayed(self):
        return self.is_element_displayed(self._question_save_locator)

    def type_question(self,value):
        self.find_element(self._question_text_locator).send_keys(value)

    def click_save_question(self):
        #self.scroll_element_into_view(self._question_save_locator)
        self.find_element(self._question_save_locator).click()

    def click_add_answers_in_bulk(self):
        self.find_element(self._question_add_answer_bulk_locator).click()

    def click_save_answers_in_bulk(self):
        self.find_element(self._question_add_answer_bulk_save_locator).click()

    def type_answer_bulk(self, options=[]):
        for opt in options:
            self.find_element(self._question_add_answer_bulk_textarea_locator).send_keys(opt)
            self.find_element(self._question_add_answer_bulk_textarea_locator).send_keys(Keys.ENTER)

    def add_multiple_choice_question_to_survey(self):
        self.find_element(self._multiple_choice_question_locator).click()
        if self.is_multiple_choice_question_add_displayed:
            actions = ActionChains(self.selenium)
            actions.click_and_hold(self.find_element(self._multiple_choice_question_locator))
            actions.drag_and_drop(self.find_element(self._multiple_choice_question_locator),self.find_element(self._question_area_locator))
            actions.perform()

    def add_data_to_multiple_choice_question(self,question, options=[]):
        WebDriverWait(self.selenium,30).until(EC.presence_of_element_located(self._question_text_locator))
        self.type_question(question)
        self.click_add_answers_in_bulk()
        self.type_answer_bulk(options)
        if self.is_question_add_answer_bulk_save_displayed:
            self.click_save_answers_in_bulk()
        if self.is_question_save_displayed:
            self.click_save_question()

    def add_drop_down_question_to_survey(self):
        self.find_element(self._drop_down_question_locator).click()
        if self.is_drop_down_question_add_displayed:
            actions = ActionChains(self.selenium)
            actions.click_and_hold(self.find_element(self._drop_down_question_locator))
            actions.drag_and_drop(self.find_element(self._drop_down_question_locator),self.find_element(self._question_area_locator))
            actions.perform()

    def add_data_to_drop_down_question(self,question, options=[]):
        WebDriverWait(self.selenium,30).until(EC.presence_of_element_located(self._question_text_locator))
        self.type_question(question)
        self.click_add_answers_in_bulk()
        self.type_answer_bulk(options)
        if self.is_question_add_answer_bulk_save_displayed:
            self.click_save_answers_in_bulk()
        if self.is_question_save_displayed:
            self.click_save_question()

    def add_ranking_question_to_survey(self):
        self.find_element(self._ranking_question_locator).click()
        if self.is_ranking_question_add_displayed:
            actions = ActionChains(self.selenium)
            actions.click_and_hold(self.find_element(self._ranking_question_locator))
            actions.drag_and_drop(self.find_element(self._ranking_question_locator),self.find_element(self._question_area_locator))
            actions.perform()

    def add_data_to_ranking_question(self,question, options=[]):
        WebDriverWait(self.selenium,30).until(EC.presence_of_element_located(self._question_text_locator))
        self.type_question(question)
        self.click_add_answers_in_bulk()
        self.type_answer_bulk(options)
        if self.is_question_add_answer_bulk_save_displayed:
            self.click_save_answers_in_bulk()
        if self.is_question_save_displayed:
            self.click_save_question()

    def add_single_textbox_question_to_survey(self):
        #self.scroll_element_into_view(self._single_textbox_question_locator)
        self.find_element(self._single_textbox_question_locator).click()
        if self.is_single_textbox_question_add_displayed:
            actions = ActionChains(self.selenium)
            actions.click_and_hold(self.find_element(self._single_textbox_question_locator))
            actions.drag_and_drop(self.find_element(self._single_textbox_question_locator),self.find_element(self._question_area_locator))
            actions.perform()

    def add_data_to_single_textbox_question(self,question):
        WebDriverWait(self.selenium,30).until(EC.presence_of_element_located(self._question_text_locator))
        self.type_question(question)
        if self.is_question_save_displayed:
            self.click_save_question()

    def add_multiple_textbox_question_to_survey(self):
        self.find_element(self._multiple_textbox_question_locator).click()
        if self.is_multiple_textbox_question_add_displayed:
            actions = ActionChains(self.selenium)
            actions.click_and_hold(self.find_element(self._multiple_textbox_question_locator))
            actions.drag_and_drop(self.find_element(self._multiple_textbox_question_locator),self.find_element(self._question_area_locator))
            actions.perform()

    def add_data_to_multiple_textbox_question(self,question, options=[]):
        WebDriverWait(self.selenium,30).until(EC.presence_of_element_located(self._question_text_locator))
        self.type_question(question)
        self.click_add_answers_in_bulk()
        self.type_answer_bulk(options)
        if self.is_question_add_answer_bulk_save_displayed:
            self.click_save_answers_in_bulk()
        if self.is_question_save_displayed:
            self.click_save_question()


class QuestionBank(CreateSurveyPage):
    pass


class Themes(CreateSurveyPage):
    pass


class Logic(CreateSurveyPage):
    pass


class Options(CreateSurveyPage):
    pass
