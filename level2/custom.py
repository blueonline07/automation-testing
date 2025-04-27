# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import unittest


action = {
    "send_keys": lambda x: x.send_keys,
    "click": lambda x: x.click
}


class CustomTest(unittest.TestCase):
    def __init__(self, url = "", steps = [], output = None):
        super(CustomTest, self).__init__('test_case')
        self.url = url
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
        driver.get(self.url)
        for step in self.steps:
            xpath = step['xpath']
            data = step['data']
            type_ = step['type']
            if type_ == 'button':
                driver.find_element_by_xpath(xpath).click()
            else:
                driver.find_element(By.XPATH, xpath).send_keys(data)
        print(driver.find_element_by_xpath(self.output['xpath']).text)
        self.assertEqual(driver.find_element_by_xpath(self.output['xpath']).text, self.output['value'])
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
