from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

def test_leave_functionality(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_my_leave()

    leave = LeavePage(driver)
    assert leave.is_leave_page_displayed()
