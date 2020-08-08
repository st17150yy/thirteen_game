from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

import time

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

driver = Firefox()
ef_driver = EventFiringWebDriver(driver, MyListener())
# ef_driver.get("https://hello-flask0412.herokuapp.com")
#ef_driver.get("https://www.doctorwho.tv/games/thirteen#_")
ef_driver.get("https://asset-manager.bbcchannels.com/m/2fzi3/")

# element = ef_driver.find_element_by_id("page-title")
#element = ef_driver.find_element_by_xpath('/html/body/div/div[1]/div[2]') 

element = ef_driver.find_element_by_class_name('best-container')
#element = ef_driver.find_element_by_xpath('//*[@id="full-width"]/div[1]/div/iframe/html/body/div/div[1]/div[2]/div[1]') 
l = (element.location)
#element.send_keys("selenium")
#element.send_keys(Keys.ENTER)

actions = ActionChains(ef_driver)
actions.move_by_offset(l['x'],l['y'])
for i in range(0,100):
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
