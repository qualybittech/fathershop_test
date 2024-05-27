import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT , click_element, wait_for_element

def navigate_to_footer_screen(self):
    try:

        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Clicked on the Collapsed Tab successfully.")
    # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))
    # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        print("Mouse hovered over the 'Theme' tab")
    # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Theme tab clicked successfully")
     # Hover over the "styles_tab" element
        footer_tab = wait_for_element(self.wait, (By.CSS_SELECTOR, "a[href*='/admin/theme/module_footer']"))
        ActionChains(self.driver).move_to_element(footer_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Mouse hovered over 'Footer_tab'")

        # Click on the "styles_tab"
        footer_tab.click()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        print("Footer_tab clicked successfully")
    except Exception as e:
        # Catch any other exceptions that may occur
        print(f"Error occurred in accessing Footer Screen from Dashboard Left column: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def footer_name(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Footer']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        print("New Footer Name is added")
    except Exception as e:
        print(f"An error occurred in Footer_name method: {e}")
        raise

def add_Margin(wait,value):
    try:
         add_margin_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_margin_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Margin value is added")
    except Exception as e:
        print(f"Error in adding Margin value method: {e}")
        raise
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_Padding(wait,value):
    try:
         add_padding_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[2]")))
         add_padding_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Padding value is added")

    except Exception as e:
        print(f"Error in adding Paddng value method: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_Border(wait,value):
    try:
         add_border_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[3]")))
         add_border_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Border value is added")

    except Exception as e:
        print(f"Error in adding Border value method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def max_width_btn(wait):
    try:
        width = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Increase Value']")))
        width.click()
        sleep(WAIT_TIME_SHORT)
        print("Width is added ")
    except Exception as e:
        print(f"Error clicking on max width button method: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def footer_type(wait):
    try:
        width = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label)[3]")))
        width.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Footer type 'Reveal' is selected")
    except Exception as e:
        print(f"Error clicking on footer type button method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def hover_reset(wait):
    try:
        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon icon-close reset-field'])[1]")))
        ActionChains(wait.driver).move_to_element(reset).perform()
        reset.click()
        sleep(WAIT_TIME_SHORT)
        print("Reset button is hovered is selected")
    except Exception as e:
        print(f"Error clicking on reset button method: {e}")
        raise

