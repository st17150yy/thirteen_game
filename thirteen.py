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


def merged(navigated_driver,merged_query='tile-merged'):
	elements = navigated_driver.find_elements_by_class_name(merged_query)
	return len(elements) != 0;

def getScore(navigated_driver,getScore_query='score-container'):
	element = navigated_driver.find_element_by_class_name(getScore_query)
	return (eval(element.text.replace('\n','')));



driver = webdriver.Chrome()
ef_driver = EventFiringWebDriver(driver, MyListener())
ef_driver.get('https://asset-manager.bbcchannels.com/m/2fzi3/')


element = ef_driver.find_element_by_class_name('best-container')
l = element.location
print(element.text)
actions = ActionChains(ef_driver)
actions.move_by_offset(l['x'],l['y'])

#time.sleep(5)

t = 0
init_score = getScore(ef_driver)
score = init_score

for i in range(0,10):
#	actions.click()

	actions.key_down(Keys.LEFT)
	actions.pause(t)
	score += getScore(ef_driver)

	actions.key_down(Keys.DOWN)
	actions.pause(t)
	score += getScore(ef_driver)


	actions.key_down(Keys.RIGHT)
	actions.pause(t)
	score += getScore(ef_driver)

	actions.key_down(Keys.DOWN)
	actions.pause(t)
	score += getScore(ef_driver)


	time.sleep(0)
	if score == init_score:
		actions.key_down(Keys.UP)
		actions.pause(t)
		print("UP")
	init_score = getScore(ef_driver)
	score = init_score
	actions.perform()
	actions = ActionChains(ef_driver)

element = ef_driver.find_element_by_class_name('best-container')
l = element.location
print(element.text)

time.sleep(2)
# ブラウザを終了する。
#ef_driver.close()
