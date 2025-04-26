from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    MY_LEAVE = (By.XPATH, "//button[@title='My Leave']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        return self.is_visible(self.DASHBOARD_HEADER)

    def click_my_leave(self):
        try:
            # Wait for the MY_LEAVE button to be visible and clickable
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.MY_LEAVE)
            )
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.MY_LEAVE)
            )

            # Click the element if it is clickable
            element.click()
            print("Clicked on MY_LEAVE button successfully.")
        except Exception as e:
            print(f"Error while clicking MY_LEAVE: {e}")
            self.driver.save_screenshot("click_my_leave_failure.png")