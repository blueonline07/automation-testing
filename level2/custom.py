# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomTest(unittest.TestCase):
    def __init__(self, steps=None, output = None):
        super(CustomTest, self).__init__('test_case')
        if steps is None:
            steps = []
        self.steps = steps
        self.output = output

    def setUp(self, data = None):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def test_case(self):
        driver = self.driver
        driver.get("https://ecommerce-playground.lambdatest.io")
        for step in self.steps:
            type_ = step['type']
            if type_ == 'button':
                try:
                    button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, step['xpath']))
                    )
                    button.click()
                except TimeoutException:
                    continue
            elif type_ == 'select':
                dropdown = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, step['xpath'])))
                Select(dropdown).select_by_visible_text(step['data'])
            elif type_ == 'text':
                text_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, step['xpath'])))
                data = step['data']
                text_field.clear()
                text_field.send_keys(data)


        out_ele = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, self.output['xpath'])))
        self.assertEqual(out_ele.text, self.output['value'])
        driver.close()
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
