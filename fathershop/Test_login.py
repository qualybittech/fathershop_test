from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def login(self, username, password):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, 'input-username')))
        username_field.send_keys(username)
        sleep(5)
        print('Entered Username')

        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, 'input-password')))
        password_field.send_keys(password)
        sleep(5)
        print('Entered Password')

        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "//button[@type='submit']")))
        login_button.click()
        sleep(5)
        print('Clicked on Login Button')

        # Check if the login button is clickable
        if not login_button.is_enabled():
            raise AssertionError('Login button is not clickable')

        login_button.click()
        sleep(5)
        print('Fathershops Admin Dashboard screen is opened successfully')

class TestFathershopLogin:
    @pytest.fixture
    def driver_setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get('https://kiran.myfathershops.com/admin/?route=common/login')
        driver.maximize_window()
        yield driver
        driver.quit()

    # Pytest function for testing login page navigation
    def test_login_page_navigation(self, driver_setup):
        driver = driver_setup

        # Instantiate the LoginPage class
        login_page = LoginPage(driver)

        # Call the login method with the username and password
        login_page.login("your_username", "your_password")

        # Check if the driver navigated to the login page
        assert "common/login" in driver.current_url, "Failed to navigate to the login page"
        print("Successfully navigated to the login page")

if __name__ == "__main__":
    pytest.main()
