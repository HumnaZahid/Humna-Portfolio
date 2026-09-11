import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run browser in headless mode for CI/CD
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_login(driver):
    """Test Case: Verify user login with valid credentials"""
    driver.get("https://example.com/login")
    
    # Locate elements and perform login actions
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")
    
    email_input.send_keys("student@example.com")
    password_input.send_keys("Password123")
    login_button.click()
    
    # Assertion
    assert "dashboard" in driver.current_url.lower()

def test_invalid_login(driver):
    """Test Case: Verify error message on invalid credentials"""
    driver.get("https://example.com/login")
    
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")
    
    email_input.send_keys("student@example.com")
    password_input.send_keys("WrongPassword")
    login_button.click()
    
    error_msg = driver.find_element(By.ID, "error-message").text
    assert "invalid" in error_msg.lower()
