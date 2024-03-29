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
actions = ActionChains(ef_driver)

#time.sleep(5)

t = 0
init_score = getScore(ef_driver)
past_init_score = init_score
score = init_score
score_changed = True

for i in range(0,100):
#	actions.click()

	init_score = getScore(ef_driver)
	actions.key_down(Keys.DOWN)
	actions.pause(t)
	actions.key_down(Keys.LEFT)
	actions.pause(t)

	actions.key_down(Keys.DOWN)
	actions.pause(t)

	actions.key_down(Keys.RIGHT)
	actions.pause(t)

	"""
	actions.key_down(Keys.DOWN)
	actions.pause(t)
	"""
	"""
	time.sleep(0)
	if getScore(ef_driver) == init_score:
		actions.key_down(Keys.RIGHT)
		actions.key_down(Keys.DOWN)

		actions.pause(t)
#		print("RIGHT!!")

#		if past_init_score == init_score:
#			ActionChains(ef_driver).key_down(Keys.UP).perform()
#			print("UP!!")
		past_init_score = init_score
	"""
	actions.perform()



	init_score = getScore(ef_driver)
	actions = ActionChains(ef_driver)


element  = ef_driver.find_element_by_class_name('tile-container' )

table = element.get_attribute('innerHTML')
table = table.replace('<div class="tile-inner"></div></div>','\n')
table = table.replace('<div class="tile tile-','')
table = table.replace('tile-position-',',(')
table = table.replace('-',',')
table = table.replace('">',')')
table = table.replace('tile','')
table = table.replace(' ,new','')
table = table.replace(' ,merged','')
table = table.replace(' ','')
table_list = table.split('\n')

# print('merged : ',NbMerged)
length = len(table_list)
for i in range(len(table_list)):
    if i+1 < length :
        if table_list[i] == table_list[i+1]:
            table_list[i] = ''
            table_list[i+1] = ''
            # table_list.pop(i)
            # table_list.pop(i)
            # length -= 2

length = len(table_list)


try:
    for item in table_list:
        table_list.remove('')
except:
        print("END")    

for item in table_list:
	item.split(',')
	


print('list-length : ',len(table_list))
#print(table)
print(table_list)
#print('row table\n',element.get_attribute('innerHTML').replace('<div class="tile-inner"></div></div>','\n'))



element = ef_driver.find_element_by_class_name('best-container')
l = element.location

print(element.text)



#time.sleep(2)
# ブラウザを終了する。
ef_driver.close()
# driver.close()
