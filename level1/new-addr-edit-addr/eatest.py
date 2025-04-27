# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class EATest(unittest.TestCase):
    def __init__(self, method_name='test_case', data=None, output=None):
        super(EATest, self).__init__(method_name)
        self.email = data["email"]
        self.password = data["password"]
        self.firstname = data["firstname"]
        self.lastname = data["lastname"]
        self.address = data["address"]
        self.city = data["city"]
        self.postcode = data["postcode"]
        self.country = data["country"]
        self.zone = data["zone"]
        self.output = output

    def setUp(self, data=None):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        driver = self.driver
        driver.get("https://ecommerce-playground.lambdatest.io")
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        driver.find_element_by_name("email").send_keys(self.email)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/address")
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/address/edit&address_id=16654")
        driver.find_element_by_id("input-firstname").clear()
        driver.find_element_by_id("input-firstname").send_keys(self.firstname)
        driver.find_element_by_id("input-lastname").clear()
        driver.find_element_by_id("input-lastname").send_keys(self.lastname)
        driver.find_element_by_id("input-address-1").clear()
        driver.find_element_by_id("input-address-1").send_keys(self.address)
        driver.find_element_by_id("input-city").clear()
        driver.find_element_by_id("input-city").send_keys(self.city)
        driver.find_element_by_id("input-postcode").clear()
        driver.find_element_by_id("input-postcode").send_keys(self.postcode)

        driver.find_element_by_id("input-country").click()
        time.sleep(1)
        Select(driver.find_element_by_id("input-country")).select_by_visible_text(self.country)
        driver.find_element_by_id("input-zone").click()
        time.sleep(1)
        Select(driver.find_element_by_id("input-zone")).select_by_visible_text(self.zone)

        driver.find_element_by_xpath("//input[@value='Continue']").click()
        res = driver.find_element_by_class_name(self.output["class_"])
        self.assertEqual(res.text, self.output["text_"])
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
