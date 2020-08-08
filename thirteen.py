from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

driver = webdriver.Firefox()
ef_driver = EventFiringWebDriver(driver, MyListener())
ef_driver.get("https://asset-manager.bbcchannels.com/m/2fzi3/")


element = ef_driver.find_element_by_class_name('best-container')
l = element.location

actions = ActionChains(ef_driver)
actions.move_by_offset(l['x'],l['y'])

for i in range(0,15):
	actions.click()
	actions.key_down(Keys.LEFT)
	actions.key_down(Keys.DOWN)
	actions.key_down(Keys.RIGHT)
	actions.key_down(Keys.DOWN)

	actions.perform()
	time.sleep(0.1)
	actions = ActionChains(ef_driver)

time.sleep(2)
# ブラウザを終了する。
#ef_driver.close()
