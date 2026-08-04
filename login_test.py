# pyright: reportMissingImports=false
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

driver.find_element(By.ID, "submit").click()

time.sleep(2)

# Test Case 1: Valid Login
def test_valid_login(self):
        self.login("student", "Password123")
        self.assertIn("Logged In Successfully", self.driver.page_source)

# Test Case 2: Invalid Username
def test_invalid_username(self):
        self.login("wrongUser", "Password123")
        self.assertIn("Your username is invalid!", self.driver.page_source)

# Test Case 3: Invalid Password
def test_invalid_password(self):
        self.login("student", "wrongPass")
        self.assertIn("Your password is invalid!", self.driver.page_source)

# Test Case 4: Empty Username
def test_empty_username(self):
        self.login("", "Password123")
        self.assertIn("Your username is invalid!", self.driver.page_source)

# Test Case 5: Empty Password
def test_empty_password(self):
        self.login("student", "")
        self.assertIn("Your password is invalid!", self.driver.page_source)

# Test Case 6: Both Fields Empty
def test_empty_fields(self):
        self.login("", "")
        self.assertIn("Your username is invalid!", self.driver.page_source)

driver.quit()
