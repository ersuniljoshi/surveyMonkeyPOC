import pytest


@pytest.fixture(scope='session')
def base_url(base_url, request):
    return base_url or request.getfuncargvalue('live_server').url

@pytest.fixture(scope='session')
def selenium(selenium):
    selenium.implicitly_wait(40)
    selenium.maximize_window()
    return selenium