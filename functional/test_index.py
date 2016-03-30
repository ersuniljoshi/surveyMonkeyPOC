import pytest

from pages.index import IndexPage


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_index_page_displayed(base_url, selenium):
    page = IndexPage(base_url, selenium).open()
    assert "SurveyMonkey: Free online survey software & questionnaire tool" == selenium.title
    assert page.is_signin_displayed


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_sign_in_page_displayed(base_url, selenium):
    page = IndexPage(base_url, selenium).open()
    page.click_sign_in()
    assert "SurveyMonkey - Log in" == selenium.title
