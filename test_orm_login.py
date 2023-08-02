from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
chrome_option= webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_option)

class Test_orange_001:

    def test_login_001(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        dash =driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text

        if dash == 'Dashboard':
            print('test 001 pass')
            assert True
        else:
            print('test 001 faild')
            assert False

