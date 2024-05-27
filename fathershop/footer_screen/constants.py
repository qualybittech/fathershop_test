
#This File contains webpage URL,User name , Password and Wait times
# constants.py

from selenium.webdriver.support import expected_conditions as EC


USERNAME = 'ola'
PASSWORD = '1212'

#USERNAME = 'kiran@fathershops.com'
#PASSWORD = '123456'

Driver_path = '/Users/zain/Downloads/chromedriver'
#LOGIN_URL = 'https://kiran.myfathershops.com/admin/?route=common/login'
LOGIN_URL = 'https://test101.fathershops-test.xyz/admin'

SETTINGS_ICON_CLASS = "brio-icon.animate-spin"

WAIT_TIME_SHORT = 2
WAIT_TIME_MEDIUM = 5
WAIT_TIME_LONG = 10

ERROR_INVALID_CREDENTIALS = "Invalid username or password"

def click_element(wait, locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def wait_for_element(wait, locator):
    element = wait.until(EC.presence_of_element_located(locator))
    return element


