from selenium.webdriver import ActionChains
from sampleproject.autoproject.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import openpyxl


class DetailsPage(BasePage):
    name_xpath = "//input[@id = 'name']"
    email_xpath = "//input[@id = 'email']"
    phone_xpath = "//input[@id = 'phone']"
    address_xpath = "//textarea[@id = 'textarea']"

    country_dd_xpath = "//select[@id = 'country']"
    colors_dd_xpath = "//select[@id = 'colors']"
    date_box_xpath = "//input[@id = 'datepicker']"
    month_xpath = "//span[@class = 'ui-datepicker-month']"
    year_xpath = "//span[@class = 'ui-datepicker-year']"
    next_month_xpath = "//span[text() = 'Next']"
    previous_month_xpath = "//span[text() = 'Prev']"
    date_xpath = "//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a"
    search_input_xpath = "//input[@class = 'wikipedia-search-input']"
    search_xpath = "//input[@class = 'wikipedia-search-button']"
    click_search = "//a[text() = 'Comedy film']"
    alert_xpath = "//button[text() = 'Alert']"
    confirm_xpath = "//button[text() = 'Confirm Box']"
    prompt_xpath = "//button[text() = 'Prompt']"
    double_xpath = "//button[text() = 'Copy Text']"
    drag_xpath = "//div[@id = 'draggable']"
    drop_xpath = "//div[@id = 'droppable']"
    slider_xpath = "//div[@id = 'slider']//span"
    dob_xpath = "//span[@class = 'icon_calendar']"

    def enter_name(self, name):
        element = self.find_element(self.name_xpath)
        element.send_keys(name)

    def enter_email(self, email):
        element = self.find_element(self.email_xpath)
        element.send_keys(email)

    def enter_phone(self, mobile):
        element = self.find_element(self.phone_xpath)
        element.send_keys(mobile)

    def enter_address(self, address):
        element = self.find_element(self.address_xpath)
        element.send_keys(address)

    def select_gender(self, gender):
        gender_xpath = f"//input[@value = '{gender}']"
        element = self.find_element(gender_xpath)
        element.click()

    def select_day(self, day):
        Day_xpath = f"//input[@id='{day}']"
        element = self.find_element(Day_xpath)
        element.click()

    def enter_country(self, country):
        element = self.find_element(self.country_dd_xpath)
        drp = Select(element)
        drp.select_by_visible_text(country)

    def enter_colour(self, color):
        element = self.find_element(self.colors_dd_xpath)
        drp = Select(element)
        drp.select_by_visible_text(color)

    def enter_date(self, month, year, day):
        element = self.find_element(self.date_box_xpath)
        element.click()
        while True:
            ele_m = self.find_element(self.month_xpath).text
            ele_y = self.find_element(self.year_xpath).text

            if ele_m == month and ele_y == year:
                break
            else:
                self.find_element(self.next_month_xpath).click()
                # self.find_element(self.previous_month_xpath).click()
        ele_d = self.find_elements(self.date_xpath)
        for ele in ele_d:
            if ele.text == day:
                ele.click()
                break

    def get_price(self, book):
        price_xpath = f"//td[text() = '{book}']/following-sibling::td[3]"
        element = self.find_element(price_xpath)
        print(f"{book} price is: ", element.text)

    def get_author(self, subject):
        author_xpath = f"//td[text() = '{subject}']/preceding-sibling::td[1]"
        element = self.find_element(author_xpath)
        print(f"author of {subject} is: ", element.text)

    def click_product(self, product):
        select_product = f"//td[text() = '{product}']/following-sibling::td[2]"
        element = self.find_element(select_product)
        element.click()

    def search(self, search_input):
        element = self.find_element(self.search_input_xpath)
        element.send_keys(search_input)
        click = self.find_element(self.search_xpath)
        click.click()
        # choose = self.find_element(self.click_search)
        # choose.click()

    def alerts(self):
        element = self.find_element(self.alert_xpath)
        element.click()
        self.switch_alert().accept()
        con = self.find_element(self.confirm_xpath)
        con.click()
        self.switch_alert().dismiss()

    def double(self):
        element = self.find_element(self.double_xpath)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def drag_drop(self):
        source = self.find_element(self.drag_xpath)
        destination = self.find_element(self.drop_xpath)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, destination).perform()

    def slider(self, x, y):
        slider = self.find_element(self.slider_xpath)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, x, y).perform()

