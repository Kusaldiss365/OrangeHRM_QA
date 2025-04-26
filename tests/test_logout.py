from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout_functionality(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    profile = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
    profile.click()

    logout = driver.find_element(By.LINK_TEXT, "Logout")
    logout.click()

    assert "login" in driver.current_url
