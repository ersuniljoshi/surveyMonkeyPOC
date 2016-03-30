import pytest

from pages.signin import SignInPage


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.nondestructive
def test_user_signin(base_url, selenium):
    page = SignInPage(base_url, selenium).open()
    page.user_sign_in('xxxxx', 'xxxxx')
    assert 'Welcome to SurveyMonkey!' == selenium.title
