from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import Login
from action import Action
from slack import Slack
import time

class Main:
    
  def main():
      login = Login()
      action = Action()
      slack = Slack()
      
      try:
          options = Options()
          options.add_argument('--headless')
          
          slack.start()

          driver = webdriver.Chrome("./chromedriver")
          driver.get("https://keiba.rakuten.co.jp/?l-id=top_logo")

          time.sleep(5)

          if len(driver.find_elements_by_xpath("/html/body/section/div[2]/div")):
              pop = driver.find_element_by_xpath("/html/body/section/div[2]/div")
              pop.click()

          login.loginFlow(driver)

          driver.find_element_by_class_name("modal").click()
          time.sleep(3)

          action.InsertMoney(driver)
          time.sleep(5)

          action.InsertPinCode(driver)
          time.sleep(3)
          
      except Exception as e:
          slack.error()
      finally:
          slack.finish()
          driver.quit()

  if __name__ == "__main__":
      main()
