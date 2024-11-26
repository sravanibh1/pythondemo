import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def launch_browser(url: str, driver_path: str) -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver  # Return the driver instead of quitting


def wait_for_element(driver, locator):
    element = WebDriverWait(driver, 150).until(EC.element_to_be_clickable((By.XPATH, locator)))
    return element


def scroll_to_element(driver, locator):
    element = WebDriverWait(driver, 150).until(EC.element_to_be_clickable((By.XPATH, locator)))
    driver.execute_script("arguments[0].scrollIntoView();", element)


if __name__ == "__main__":
    driver_path = 'C:/Users/Sravani Bhogadi/Desktop/fitpeo/chromedriver.exe'
    url = "https://fitpeo.com/"
    rc = "//div[text()='Revenue Calculator']"
    scale = "/html/body/div[2]/div[1]/div[1]/div[2]/div/h4"
    scale_input = '//*[@id=":r0:"]'
    click_text = "/html/body/div[2]/div[1]/div[1]/div[1]/div/h5"
    CPT_99091_text = "//p[text()='CPT-99091']"
    CPT_99091_checkbox = "//p[text()='CPT-99091']/parent::div//span[contains(@class, 'MuiTypography-root')]"
    CPT_99453_text = "//p[text()='CPT-99453']"
    CPT_99453_checkbox = "//p[text()='CPT-99453']/parent::div//span[contains(@class, 'MuiTypography-root')]"
    CPT_99454_text = "//p[text()='CPT-99454']"
    CPT_99454_checkbox = "//p[text()='CPT-99454']/parent::div//span[contains(@class, 'MuiTypography-root')]"
    CPT_99474_text = "//p[text()='CPT-99474']"
    CPT_99474_checkbox = "//p[text()='CPT-99474']/parent::div//span[contains(@class, 'MuiTypography-root')]"
    Total_rec = "(//header[contains(@class,'MuiPaper-root')])//p[text()='Total Recurring Reimbursement for all Patients Per Month:']/p"


    # Launch the browser and keep the instance open
    browser = launch_browser(url, driver_path)

    # Wait for the element and click it
    wait_for_element(browser, rc).click()
    time.sleep(5)
    scroll_to_element(browser, scale)
    time.sleep(5)
    wait_for_element(browser, scale_input).clear()
    time.sleep(5)
    wait_for_element(browser, scale_input).send_keys("560")
    time.sleep(5)
    # wait_for_element(browser, checkbox_1).click()
    # time.sleep(5)
    wait_for_element(browser, click_text).click()
    scroll_to_element(browser, CPT_99091_text)
    wait_for_element(browser, CPT_99091_checkbox).click()
    time.sleep(3)
    scroll_to_element(browser, CPT_99453_text)
    wait_for_element(browser, CPT_99453_checkbox).click()
    time.sleep(3)
    scroll_to_element(browser, CPT_99454_text)
    wait_for_element(browser, CPT_99454_checkbox).click()
    time.sleep(3)
    scroll_to_element(browser, CPT_99474_text)
    wait_for_element(browser, CPT_99474_checkbox).click()
    time.sleep(3)
    Total_Recurring_Reimbursement_for_all_Patients_Per_Month = wait_for_element(browser, Total_rec).text
    print(Total_Recurring_Reimbursement_for_all_Patients_Per_Month)
    time.sleep(3)

