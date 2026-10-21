import pytest
from playwright.sync_api import expect


def test_successful_login(login_page):
    login_page.login("student", "Password123")

    expect(login_page.page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(login_page.login_success).to_have_text("Logged In Successfully") 
    expect(login_page.logout_button).to_be_visible()   


@pytest.mark.parametrize("username, password, expected_error", [
    ("SonGoku", "Password123", "Your username is invalid!"),
    ("student", "ZyrafyWchodzaDoSzafy", "Your password is invalid!")
])
def test_unsuccessful_login(login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error_banner).to_be_visible()
    expect(login_page.error_banner).to_have_text(expected_error)


def test_progress_bar_initial_state(progress_bar_page):
    expect(progress_bar_page.start_location).to_be_visible()
    expect(progress_bar_page.stop_location).to_be_visible()
    expect(progress_bar_page.progress_bar).to_have_text("25%")


def test_progress_bar_stops_at_threshold(progress_bar_page):
    progress_bar_page.start()
    progress_bar_page.wait_for_threshold(75)
    progress_bar_page.stop()
    expect(progress_bar_page.result).to_be_visible()
    val = int(progress_bar_page.progress_bar.get_attribute("aria-valuenow"))
    assert 75 <= val <= 100  


def test_dynamic_table_value_comparison(dynamic_table_page):
    table_cpu = dynamic_table_page.get_chrome_cpu_from_table()
    warning_cpu = dynamic_table_page.get_warning_text()

    assert table_cpu in warning_cpu