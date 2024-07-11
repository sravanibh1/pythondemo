from sampleproject.autoproject.pages.basepage import BasePage


class HomePage(BasePage):
    browser_xpath = "//button[text() = 'New Browser Window']"

    def new_browser(self):
        element = self.find_element(self.browser_xpath)
        element.click()
