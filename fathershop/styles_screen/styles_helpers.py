# styles_helpers.py
import logging
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium_helpers import wait_for_element
from constants import WAIT_TIME_SHORT, WAIT_TIME_MEDIUM,click_element

def navigate_to_styles_screen(self):
    try:
        logging.info("Navigating to the styles screen...")
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Clicked on the styles screen link successfully.")

        # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))

        # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Mouse hovered over the 'Theme' tab")

        # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Theme tab clicked successfully")

        # Hover over the "styles_tab" element
        styles_tab = wait_for_element(self.wait, (By.XPATH, "//a[normalize-space()='Styles']"))
        ActionChains(self.driver).move_to_element(styles_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Mouse hovered over 'Styles_tab'")

        # Click on the "styles_tab"
        styles_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Styles_tab clicked successfully")

    except Exception as e:
        # Catch any other exceptions that may occur
        print(f"An error occurred in opening Styles screen: {e}")
        raise




#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def new_label(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Page Layout']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("label is added")
    except Exception as e:
        print(f"An error occurred in addng new label method: {e}")
        raise


#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def select_options(wait, driver):
    try:
        boxed = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[2]//label[1]")))
        ActionChains(driver).move_to_element(boxed).perform()
        sleep(WAIT_TIME_SHORT)
        print("Boxed option is hovered")
        boxed.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Boxed option is selected")
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise
    except TimeoutException as e:
        print(f"Timeout waiting for element to be clickable: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def edit_font(wait):
    try:
        FontType = wait.until(EC.element_to_be_clickable(By.XPATH, "//span[1]//label[1]"))
        FontType.cliick()

        sleep(WAIT_TIME_SHORT)
        print("System Font type is selected")

        FontFamily = wait.until(EC.element_to_be_clickable(By.XPATH, "(//span[@class='ant-select-selection-item'])[1]"))
        FontFamily.click()
        sleep(WAIT_TIME_SHORT)

        print("Font Family drop-down menu is opened")

        Dropdown = wait.until(EC.element_to_be_clickable(By.XPATH, "//div[@title='Times, serif']//div[@class='ant-select-item-option-content']"))
        Dropdown.click()
        sleep(WAIT_TIME_SHORT)
        print("Times Font Famil is selected")
        print("Font Family is Edited successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def open_general(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("General drop-down section is opened")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def close_general(wait):
    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("General drop-down section is closed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_boxedoption(wait):
    try:
        boxed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_boxed")))
        boxed.click()
        sleep(WAIT_TIME_SHORT)
        print("Boxed Options drop-down section is opened")
    except Exception as e:
        print(f"An error occurred in clicking boxed_option drop-down: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def close_boxedoption(wait):
    try:
        boxed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_boxed")))
        boxed.click()
        sleep(WAIT_TIME_SHORT)
        print("Boxed Options drop-down section is closed")
    except Exception as e:
        print(f"An error occurred in clicking boxed_option drop-down: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_site_container(wait):
    try:
        site = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_site']//div")))
        site.click()
        sleep(WAIT_TIME_MEDIUM)
        print("site_container drop-down section is opened")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def close_site_container(wait):
    try:
        site_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_site']//div")))
        site_container.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Site Container section is closed ")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_content_container(wait):
    try:
        cont = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_content']//div")))
        cont.click()
        sleep(WAIT_TIME_SHORT)
        print("Content_container drop-down section is opened")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def close_content_container(wait):
    try:
        cont1 = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_content']//div")))
        cont1.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Content_container drop-down section is closed")
    except Exception as e:
        print(f"An error occurred in closing Content_container drop-down section: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_side_column(wait):
    try:
        side = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_1']")))
        side.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Side_column drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def close_side_column(wait):
    try:
        side1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_1']")))
        side1.click()
        sleep(WAIT_TIME_SHORT)
        print("Side_column drop-down section is closed")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def open_right_column(wait):
    try:
        side2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_2']")))
        side2.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Right_column drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def close_right_column(wait):
    try:
        side3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_2']")))
        side3.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Right_column drop-down section is closwed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def max_width_btn(wait):
    try:
        width = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[2]")))
        width.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Width is added ")
    except Exception as e:
        logging.error(f"Error clicking on create_new button: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_Padding(wait,value):
    try:
         add_padding_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_padding_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         logging.info("Padding value is added")

    except Exception as e:
        logging.error(f"Error clicking on max width button method: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def col_btn(wait):
    try:
        col = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label)[5]")))
        col.click()
        sleep(WAIT_TIME_SHORT)
        print("Column Left on Tablet is added ")
    except Exception as e:
        logging.error(f"Error in adding Paddng value method: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def select_none(wait):
    try:
        none_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-name='value.valueColumnRightBackground']//label")))
        none_btn.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("None button is selected ")
    except Exception as e:
        print(f"Error clicking on None button method: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
