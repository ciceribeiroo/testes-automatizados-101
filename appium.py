# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "emulator-5554"
caps["adv"] = "Tablet"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
actions = TouchAction(driver)

el1 = driver.find_element_by_accessibility_id("Alarm")
el1.click()
actions.tap(None, 1275, 1413, 1).perform()
el2 = driver.find_element_by_accessibility_id("6")
el2.click()
el3 = driver.find_element_by_accessibility_id("0")
el3.click()
el4 = driver.find_element_by_id("android:id/button1")
el4.click()

driver.quit()