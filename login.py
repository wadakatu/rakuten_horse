from selenium.webdriver.common.keys import Keys
from config import CONFIG
from selenium import webdriver

class Login:

    MAIL = CONFIG['mailAddress']
    PASSWORD = CONFIG['password']

    def loginFlow(self, driver: webdriver):
        driver.find_element_by_class_name("siteheader_actionlist_btn").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.maximize_window()

        userid = driver.find_element_by_name("u")
        userid.send_keys(self.MAIL)
        password = driver.find_element_by_name("p")
        password.send_keys(self.PASSWORD)
        password.send_keys(Keys.RETURN)
