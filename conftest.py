import pytest

from pages.dynamic_table_page import DynamicTablePage
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


@pytest.fixture
def dynamic_table_page(page):
    dt = DynamicTablePage(page)
    dt.navigate()
    return dt