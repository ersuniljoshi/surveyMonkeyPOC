import pytest

from pages.homepage import HomePage


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_create(base_url, selenium):
    page = HomePage(base_url, selenium).open()
    page.user_sign_in('xxxxx', 'xxxxx')
    page.create_survey_via_top_link()
    assert 'SurveyMonkey : New Survey' == selenium.title
    page.sign_out()
    assert "SurveyMonkey: Free online survey software & questionnaire tool." \
        == selenium.title
