# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "emulator-5556"
caps["adv"] = "Tablet"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("Calculator")
el1.click()
time.sleep(3)
el2 = driver.find_element_by_id("com.google.android.calculator:id/digit_9")
el2.click()
time.sleep(1)
el3 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
el3.click()
time.sleep(1)
el4 = driver.find_element_by_accessibility_id("×")
el4.click()
time.sleep(1)
el5 = driver.find_element_by_id("com.google.android.calculator:id/digit_6")
el5.click()
time.sleep(1)
el6 = driver.find_element_by_id("com.google.android.calculator:id/digit_8")
el6.click()
time.sleep(1)
el7 = driver.find_element_by_accessibility_id("plus")
el7.click()
time.sleep(1)
el8 = driver.find_element_by_accessibility_id("left parenthesis")
el8.click()
time.sleep(1)
el9 = driver.find_element_by_id("com.google.android.calculator:id/digit_4")
el9.click()
time.sleep(1)
el10 = driver.find_element_by_accessibility_id("divide")
el10.click()
time.sleep(1)
el11 = driver.find_element_by_accessibility_id("pi")
el11.click()
time.sleep(1)
el12 = driver.find_element_by_accessibility_id("right parenthesis")
el12.click()
time.sleep(1)
el13 = driver.find_element_by_xpath('//android.widget.Button[@content-desc="equals"]')
el13.click()

driver.quit()