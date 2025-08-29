# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class SearchTest(unittest.TestCase):
    def __init__(self, method_name='test_case', data=None, browser="chrome"):
        super(SearchTest, self).__init__(method_name)
        self.value = data["value"]
        self.output = data["output"]
        self.browser = browser

    def setUp(self, data=None):
        if self.browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser.lower() == 'safari':
            self.driver = webdriver.Safari()
        elif self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
        
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        driver = self.driver
        driver.get("https://with-bugs.practicesoftwaretesting.com")
        driver.find_element_by_xpath("/html/body/app-root/div/app-overview/div[3]/div[1]/form[2]/div/input").send_keys(self.value)
        driver.find_element_by_xpath("/html/body/app-root/div/app-overview/div[3]/div[1]/form[2]/div/button[2]").click()
        res = driver.find_element_by_xpath("/html/body/app-root/div/app-overview/div[3]/div[2]/h3")
        self.assertEqual(res.text, self.output)
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
        try:
            if hasattr(self, 'driver') and self.driver:
                if self.browser.lower() == 'safari':
                    time.sleep(1)
                
                self.driver.quit()
        except Exception as e:
            try:
                if hasattr(self, 'driver') and self.driver:
                    self.driver.close()
            except:
                pass
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
