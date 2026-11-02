import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:5000/login"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()

def login(driver, username, password):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()

def test_valid_login(driver):
    login(driver, "admin", "admin123")
    welcome = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "welcome"))
    )
    assert "dashboard" in driver.current_url
    assert "Welcome" in welcome.text

def test_invalid_login(driver):
    login(driver, "wrong", "wrong")
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error"))
    )
    assert "Invalid credentials" in error.text