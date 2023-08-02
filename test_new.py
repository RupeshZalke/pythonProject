from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option= webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_option)

class Test_00:
    def test_0(self):
        driver.get("https://iemodemoindia.meditab.com/#/login?returnUrl=%2Fapp%2Fpatient%2Fcreate")
        driver.find_element(By.XPATH,"//label[@class='mtab-demo-link-text']").click()
