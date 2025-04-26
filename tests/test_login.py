from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_page_title(driver):
    assert "OrangeHRM" in driver.title

def test_login_functionality(driver):
    login = LoginPage(driver)
    assert login.is_login_page_displayed()
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_displayed()
