from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "https://practicetestautomation.com/practice-test-login/"


def login(username, password):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get(URL)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    return driver


def test_valid_login():
    driver = login("student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    driver.quit()


def test_invalid_username():
    driver = login("wrongUser", "Password123")
    assert "Your username is invalid!" in driver.page_source
    driver.quit()


def test_invalid_password():
    driver = login("student", "wrongPass")
    assert "Your password is invalid!" in driver.page_source
    driver.quit()


def test_empty_username():
    driver = login("", "Password123")
    assert "Your username is invalid!" in driver.page_source
    driver.quit()


def test_empty_password():
    driver = login("student", "")
    assert "Your password is invalid!" in driver.page_source
    driver.quit()


def test_empty_fields():
    driver = login("", "")
    assert "Your username is invalid!" in driver.page_source
    driver.quit()