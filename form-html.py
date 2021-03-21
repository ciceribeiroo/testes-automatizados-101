# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://testes-automatizados.000webhostapp.com/")

        driver.find_element_by_xpath("//input[@id='fname']").click()
        driver.find_element_by_xpath("//input[@id='fname']").clear()
        driver.find_element_by_xpath("//input[@id='fname']").send_keys("nome")
        driver.find_element_by_xpath("//input[@id='lname']").click()
        driver.find_element_by_xpath("//input[@id='lname']").clear()
        driver.find_element_by_xpath("//input[@id='lname']").send_keys("sobrenome")
        #driver.find_element_by_xpath("xpath aqui").send_keys(Keys.ENTER)

        driver.find_element_by_xpath("//label[3]").click()
        #time.sleep(2)
        driver.find_element_by_xpath("//label[4]").click()
        #time.sleep(2)
        driver.find_element_by_xpath("//label[5]").click()
        
        el1 = driver.find_element_by_xpath("//label[3]")
        t1 = el1.text
        t2 = el1.get_attribute('textContent')
        t3 = el1.get_attribute("innerHTML")
        print(t1, t2, t3)

        try: self.assertEqual("Homem", el1.text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        self.assertEqual("Homem", el1.text)

        if t2.find("Homem") != -1:
            print("entrou")

        driver.find_element_by_xpath("//label[6]").click()
        driver.find_element_by_xpath("//label[7]").click()
        driver.find_element_by_xpath("//label[8]").click()

        sel = driver.find_element_by_xpath("//select[@id='cars']")
        driver.execute_script("arguments[0].click();", sel)
        Select(driver.find_element_by_xpath("//select[@id='cars']")).select_by_visible_text("Saab")
        driver.execute_script("arguments[0].click();", sel)

        data = driver.find_element_by_id("birthday")
        driver.execute_script("arguments[0].click();", data)
        driver.find_element_by_id("birthday").clear()
        driver.find_element_by_id("birthday").send_keys("10-03-2021")

        file_upload = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myfile"))
        )
        file_upload.send_keys("c:/Users/Squadra/Downloads/testes/captura/porcentagemantes.png")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
