from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        wait = WebDriverWait(self.driver, 25)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return element

    def find_elements(self, locator):
        elements = self.driver.find_elements(By.XPATH, locator)
        return elements

    def scroll_to_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_alert(self):
        alert = self.driver.switch_to.alert
        return alert
