from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, wait_for_element

def navigat_to_classic(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='classic']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Classic screen is opened")
    except Exception as e:
        print(f"An error occurred on clicking Classic Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————
def open_global_options(wait):
    try:
        global1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='accordion-heading id_gen'])[1]")))
        global1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Global Options dropdown menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Global Options dropdown menu: {e}")
        raise
#—————————————————————————————————————————————————————————————

def color(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-color-picker-color-block-inner")))
        select_color.click()
        sleep(WAIT_TIME_MEDIUM)
        color = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[11]//div[1]")))
        color.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Color is selected")
    except Exception as e:
        print(f"Error occurred in color method: {e}")
        raise

#———————————————————————————————————————————————————
def fullwidth_border(wait,value):
    try:
         add_border_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_border_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("fullwidth Border  value is added")

    except Exception as e:
        print(f"Error in adding full width Border  value method: {e}")
        raise

#———————————————————————————————————————————————————
def padding(wait,value):
    try:
         header_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='L'])[2]")))
         header_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Header Padding value is added")

    except Exception as e:
        print(f"Error in adding Header Padding  value method: {e}")
        raise
#———————————————————————————————————————————————————
def cont_padding(wait,value):
    try:
         value= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='ALL']")))
         value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Container Padding value is added")

    except Exception as e:
        print(f"Error in adding Container Padding  value method: {e}")
        raise
#———————————————————————————————————————————————————
def header_height(wait):
    try:
         header_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[1]")))
         header_value.click()
         sleep(WAIT_TIME_SHORT)
         print("header_height value is added")

    except Exception as e:
        print(f"Error in adding header_height  value method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def max_width(wait,value):
    try:
         max_value= wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Increase Value']")))
         max_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Header max width is added")

    except Exception as e:
        print(f"Error in header max width method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def header_max_width(wait,value):
    try:
         max_width= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='px'])[3]")))
         max_width.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Header max width is added")

    except Exception as e:
        print(f"Error in header max width method: {e}")
        raise

#—————————————————————————————————————————————————————————————
def open_homepage_override(wait):
    try:
        global1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_home")))
        global1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Global Options dropdown menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Global Options dropdown menu: {e}")
        raise

#—————————————————————————————————————————————————————————————
def shadow_dropdown(wait):
    try:
        # Find the Header_Shadow element
        Header_Shadow = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='ant-select-item-option-content'])[1]")))

        # Scroll to the Header_Shadow element
        wait.driver.execute_script("arguments[0].scrollIntoView();", Header_Shadow)

        # Click the Header_Shadow element using JavaScript
        wait.driver.execute_script("arguments[0].click();", Header_Shadow)

        sleep(WAIT_TIME_MEDIUM)
        print("Header_Shadow dropdown menu is opened")

        # Find the dropdown option element
        select = wait.until(EC.element_to_be_clickable((By.ID, "Dropdown")))

        # Click the dropdown option
        select.click()

        sleep(WAIT_TIME_MEDIUM)
        print("Dropdown option is selected")
    except Exception as e:
        print(f"An error occurred on Shadow dropdown button: {e}")
        raise


#—————————————————————————————————————————————————————————————
def position(wait,value):
    try:
        logo = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='px']")))
        logo.send_keys(value)
        sleep(WAIT_TIME_MEDIUM)
        print("Position is value is added")
    except Exception as e:
        print(f"An error occurred on Position increase button screen tab menu: {e}")
        raise
#—————————————————————————————————————————————————————————————
def click_tab_by_name(wait, tab_name):
    try:
        # Find the tab element by its text
        tab_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//ul[@class='tab-items']/li[text()='{tab_name}']")))

        # Click on the tab element
        tab_element.click()

        print(f"{tab_name} tab is clicked")
        sleep(WAIT_TIME_MEDIUM)

    except Exception as e:
        print(f"An error occurred while clicking {tab_name} tab: {e}")
        raise

def item_btn(self):
    try:
        hover = wait_for_element(self.wait, (By.CSS_SELECTOR, ".ui-radio.radio-toggle"))
        ActionChains(self.driver).move_to_element(hover).perform()
        sleep(WAIT_TIME_SHORT)
        print("item radio button is hovered")
        btn = wait_for_element(self.wait, (By.XPATH, ".(//label)[1]"))
        btn .click()
        sleep(WAIT_TIME_SHORT)
        print("item_btn toggle button is clicked successfuly")
    except Exception as e:
        print(f"An error occurred on clicking item_btn button : {e}")
        raise