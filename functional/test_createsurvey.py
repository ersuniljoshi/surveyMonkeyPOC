import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.createsurvey import Builder


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_verify_create_survey_page(base_url, selenium):
    page = Builder(base_url, selenium).open()
    page.user_sign_in('xxxxx','xxxxxxx')
    page.create_survey_via_top_link()
    page.add_survey_name_and_category('sjoshiPOC','Education')
    page.add_page_title_and_description('POC','Proof of Concept')
    WebDriverWait(selenium,30).until(EC.element_to_be_clickable(page._multiple_choice_question_locator))
    # Q1 - Adding Multiple Choice Question
    page.add_multiple_choice_question_to_survey()
    page.add_data_to_multiple_choice_question('My Multiple Choice Question',['Option1','Option2','Option3'])
    # TODO: This timeout is added to settle down the UI. This is a nasty Hack. Need to find a solution.
    time.sleep(5)
    # Q2 - Adding Drop Down Question
    page.add_drop_down_question_to_survey()
    page.add_data_to_drop_down_question('My Drop Down Question',['DropDown1','DropDown2','DropDown3'])
    # TODO: This timeout is added to settle down the UI. This is a nasty Hack. Need to find a solution.
    time.sleep(5)
    # Q3 - Adding Ranking Question
    page.add_ranking_question_to_survey()
    page.add_data_to_ranking_question('My Ranking Question',['Rank1','Rank2','Rank3'])
    # TODO: This timeout is added to settle down the UI. This is a nasty Hack. Need to find a solution.
    time.sleep(5)
    # Q4 - Adding Single TextBox Question
    page.add_single_textbox_question_to_survey()
    page.add_data_to_single_textbox_question('My Single TextBox Question')
    # TODO: This timeout is added to settle down the UI. This is a nasty Hack. Need to find a solution.
    time.sleep(5)
    # Q5- Adding Multiple TextBox Question
    page.add_multiple_textbox_question_to_survey()
    page.add_data_to_multiple_textbox_question('My Multiple TextBox Question',['Textbox1','Textbox2','Textbox3'])
    # this sleep has been added to showcase that all 5 questions has been added the survey, can be removed.
    time.sleep(10)
    page.sign_out()
