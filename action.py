from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import CONFIG

class Action:
  
    PINCODE = CONFIG['pinCode']
    MONEY = CONFIG['amountOfMoney']

    def InsertMoney(self, driver: webdriver):
        insert_money = driver.find_element_by_id("dialogDepositingInputPrice")
        insert_money.send_keys(self.MONEY)
        confirm = driver.find_element_by_id("dialogDepositingConfirm")
        confirm.send_keys(Keys.RETURN)

    def InsertPinCode(self, driver: webdriver):
        pincode = driver.find_element_by_id("dialogDepositingConfirmPin")
        pincode.send_keys(self.PINCODE)
        complete_insert = driver.find_element_by_id("dialogDepositingComplete")
        complete_insert.send_keys(Keys.RETURN)
