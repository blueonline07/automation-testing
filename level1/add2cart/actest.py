# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ACTest(unittest.TestCase):
    def __init__(self, method_name='test_case', data=None):
        super(ACTest, self).__init__(method_name)
        self.name = data['name']
        self.out_xpath = data['out_xpath']
        self.out_value = data['out_value']

    def setUp(self, data=None):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        driver = self.driver
        driver.get("https://ecommerce-playground.lambdatest.io")
        driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div[2]/input').send_keys(self.name)
        driver.find_element_by_xpath('//*[@id="search"]/div[2]/button').click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="entry_212469"]/div/div[1]'))).click()
        add = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="entry_216842"]/button')))
        if add.text == 'ADD TO CART':
            add.click()
        res = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, self.out_xpath)))
        self.assertEqual(res.text, self.out_value)
        driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
