from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        return self.driver.title

    def is_visible(self, by_locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        except TimeoutException:
            print(f"Element with locator {by_locator} not visible")
            return False

