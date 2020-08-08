from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from selenium.webdriver.common.keys import Keys


import time

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

driver = Firefox()
ef_driver = EventFiringWebDriver(driver, MyListener())
# ef_driver.get("https://hello-flask0412.herokuapp.com")
ef_driver.get("https://www.google.com")

# element = ef_driver.find_element_by_id("page-title")

element = ef_driver.find_element_by_name('q') 
print(element.text)
element.send_keys("selenium")
element.send_keys(Keys.ENTER)



# time.sleep(5)
# # ブラウザを終了する。
# ef_driver.close()