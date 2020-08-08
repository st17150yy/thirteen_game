# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
# driver.get("https://www.doctorwho.tv/games/thirteen#_")
driver.get("https://www.google.com/")
# driver.get("http://abehiroshi.la.coocan.jp/")

# 検索語として「selenium」と入力し、Enterキーを押す。
# element = driver.find_element_by_id("lst-ib")
# element.send_keys(Keys.SHIFT, "selenium")

element = driver.find_element_by_class_name("gLFyf gsfi")
element.send_keys(Keys.SHIFT, "selenium")

# for h2 in driver.find_elements_by_tag_name("title"):
#     print(h2.text)


# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# driver.find_element_by_link_text("").click()
# 5秒間待機してみる。


sleep(5)
# ブラウザを終了する。
driver.close()