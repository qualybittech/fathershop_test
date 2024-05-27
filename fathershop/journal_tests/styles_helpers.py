# styles_helpers.py
import logging
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_SHORT, WAIT_TIME_MEDIUM, wait_for_element, click_element

def navigate_to_styles_screen(self):
    try:
        logging.info("Navigating to the styles screen...")
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Clicked on the styles screen link successfully.")

        # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))

        # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Mouse hovered over the 'Theme' tab")

        # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Theme tab clicked successfully")

        # Hover over the "styles_tab" element
        styles_tab = wait_for_element(self.wait, (By.XPATH, "//a[normalize-space()='Styles']"))
        ActionChains(self.driver).move_to_element(styles_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Mouse hovered over 'Variables_tab'")

        # Click on the "styles_tab"
        styles_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Styles_tab clicked successfully")

    except Exception as e:
        # Catch any other exceptions that may occur
        logging.error(f"An error occurred: {e}")
        raise


def new_label(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Page Layout']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("label is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
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
        logging.error(f"Element not found: {e}")
        raise
    except TimeoutException as e:
        logging.error(f"Timeout waiting for element to be clickable: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def breakpoint(wait):
    try:
        add_breakpoint = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='button list-add-btn'])[1]")))
        add_breakpoint.click()
        sleep(WAIT_TIME_SHORT)
        print("Add breakpoint button is clicked")
    except Exception as e:
        logging.error(f"Error in breakpoint method: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def color(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        select_color.click()
        sleep(WAIT_TIME_SHORT)
        color = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[11]//div[1]")))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def gradient(wait):
    try:
        gradient = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gradient-preview")))
        gradient.click()
        sleep(WAIT_TIME_SHORT)
        preview = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='gradient-preview'])[5]")))
        preview.click()
        sleep(WAIT_TIME_SHORT)
        print("Gradient preview screen is opened")
        gra = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gradient-preview")))
        gra.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Gradient is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def camera(wait):
    try:
        camera =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-image")))
        camera.click()
        sleep(WAIT_TIME_MEDIUM)
        preview = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='puzzle-1980x600']")))
        preview.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Image is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def image_options(wait):
    try:
        image_options = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button edit-btn']//*[name()='svg']")))
        image_options.click()
        sleep(WAIT_TIME_SHORT)
        print("Image Options menu is opened")
        image_option1 = wait.until(EC.element_to_be_clickable ((By.XPATH, "(//span[@title='Inherit'])[2]")))
        image_option1.click()
        sleep(WAIT_TIME_SHORT)
        print("Background Attachement field is clicked")
        image_option2 = wait.until(EC.element_to_be_clickable ((By.XPATH, "(//div[@class='ant-select-item-option-content'])[2]")))
        image_option2.click()
        sleep(WAIT_TIME_SHORT)
        print("Scroll Option is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
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
        print.error(f"An error occurred: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def save(wait):
    try:
        save_btn =wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-btn-icon'])[3]")))
        sleep(WAIT_TIME_MEDIUM)
        save_btn.click()
        print("Save button is clicked")
        print("Data is saved")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def click_back_btn(wait):
    try:
        back_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon icon-arrow_back'])[1]")))
        back_btn.click()
        sleep(WAIT_TIME_MEDIUM)
        logging.info("Back button is clicked")
    except Exception as e:
        logging.error(f"Error occurred in Clicking Back button method: {e}")
        raise
