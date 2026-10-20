import pytest

from pages.login_page import LoginPage
from pages.progress_bar_page import ProgressBar


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def progress_bar_page(page):
    pb = ProgressBar(page)
    pb.navigate()
    return pb