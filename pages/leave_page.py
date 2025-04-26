from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LeavePage(BasePage):
    LEAVE_LIST_HEADER = (By.XPATH, "//li//a[text()='My Leave']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_leave_page_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LEAVE_LIST_HEADER)
            )
            return True
        except:
            print("Leave Page did not load properly.")
            return False
