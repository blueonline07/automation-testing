# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import unittest, time


class RegisterTest(unittest.TestCase):
    def __init__(self, method_name='test_case', data=None, browser="chrome"):
        super(RegisterTest, self).__init__(method_name)
        self.firstname = data["firstname"]
        self.lastname = data["lastname"]
        self.address = data["address"]
        self.city = data["city"]
        self.state = data["state"]
        self.country = data["country"]
        self.phone = data["phone"]
        self.email = data["email"]
        self.dob = data["dob"]
        self.password = data["password"]
        self.postcode = data["postcode"]
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
        self.wait = WebDriverWait(self.driver, 10)

    def test_case(self):
        driver = self.driver
        # Navigate directly to the registration page
        driver.get("http://localhost:4200/#/auth/register")
        
        # Wait for the page to load completely
        self.wait.until(
            EC.presence_of_element_located((By.ID, 'first_name'))
        )

        # Wait for and fill in the registration form fields
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'first_name'))
        )
        first_name_field.send_keys(self.firstname)

        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'last_name'))
        )
        last_name_field.send_keys(self.lastname)

        address_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'address'))
        )
        address_field.send_keys(self.address)

        city_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'city'))
        )
        city_field.send_keys(self.city)

        state_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'state'))
        )
        state_field.send_keys(self.state)

        phone_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'phone'))
        )
        phone_field.send_keys(self.phone)

        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_field.send_keys(self.email)

        dob_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'dob'))
        )
        dob_field.send_keys(self.dob)

        postcode_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'postcode'))
        )
        postcode_field.send_keys(self.postcode)

        password_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-test="password"]'))
        )
        password_field.send_keys(self.password)

        # Wait for and select country from dropdown
        country_dropdown = self.wait.until(
            EC.presence_of_element_located((By.ID, 'country'))
        )
        Select(country_dropdown).select_by_visible_text(self.country)

        # Wait for and click the register button
        register_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="register-submit"]'))
        )
        
        # Scroll to the button to ensure it's visible
        driver.execute_script("arguments[0].scrollIntoView(true);", register_button)
        time.sleep(1)  # Wait for scroll to complete
        

        register_button.click()
        # Add a wait after registration to see if there's any success message or redirect
        try:
            # Wait for potential success message or redirect
            time.sleep(2)
        except TimeoutException:
            pass
        
        if self.output == "success":
            assert self.driver.current_url == "http://localhost:4200/#/auth/login"
        else:
            assert self.driver.current_url == "http://localhost:4200/#/auth/register"

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
