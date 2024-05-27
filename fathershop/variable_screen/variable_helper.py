# variable_helpers.py
import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, click_element, wait_for_element

def navigate_to_variable_screen(self):
    try:
        logging.info("Navigating to the Variable screen...")
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Clicked on the Variable screen Tab successfully.")

        # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))

        # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Mouse hovered over the 'Theme' tab")

        # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        logging.info("Theme tab clicked successfully")

        # Hover over the "styles_tab" element
        variables_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//li[2]//a[1]"))
        ActionChains(self.driver).move_to_element(variables_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Mouse hovered over 'Variables_tab'")

        # Click on the "styles_tab"
        variables_tab.click()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        logging.info("Variables_tab clicked successfully")

    except Exception as e:
        # Catch any other exceptions that may occur
        logging.error(f"An error occurred: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def new_breakpoint(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Breakpoint']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("Breakpoints label is added")

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Breakpoints Value is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_breakpoint(wait, new_value):
    try:

        value_field = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        sleep(WAIT_TIME_MEDIUM)
        value_field.clear()
        sleep(WAIT_TIME_SHORT)
        logging.info("Previous value is cleared")
        value_field.send_keys(new_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Breakpoint value is edited")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def select_Colours(wait):
    try:
        colour_tab = wait_for_element(wait, (By.XPATH, "(//a[normalize-space()='Colors'])[1]"))
        sleep(WAIT_TIME_SHORT)
        colour_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Colours screen is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def new_colors(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Color']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("Colors label is added")

        value = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Colors Menu is opened")

        color = wait_for_element(wait, (By.XPATH, "(//div)[162]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Color is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_colors(wait):
    try:
        value = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Colors Menu is opened")

        color = wait_for_element(wait, (By.XPATH, "//div[28]//div[1]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Color is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def selectFontFamily(wait):
        Font_Family_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Font Family']"))
        sleep(WAIT_TIME_SHORT)
        Font_Family_tab.click()
        sleep(WAIT_TIME_MEDIUM)
        logging.info("Font Family screen is opened")

def new_font(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Font']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        logging.info("New Font Famly label is added")

        FontType = wait_for_element(wait, (By.XPATH, "//span[1]//label[1]"))
        FontType.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("System Font tyoe is selected")

        FontFamily = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-select-selection-item'])[1]"))
        FontFamily.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Family drop-down menu is opened")

        Dropdown = wait_for_element(wait, (By.XPATH, "//div[@title='Times, serif']//div[@class='ant-select-item-option-content']"))
        Dropdown.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Times Font Famil is selectedy")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_font(wait):
    try:
        FontType = wait_for_element(wait, (By.XPATH, "//span[1]//label[1]"))
        FontType.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("System Font type is selected")

        FontFamily = wait_for_element(wait, (By.XPATH, "(//span[@class='ant-select-selection-item'])[1]"))
        FontFamily.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Family drop-down menu is opened")

        Dropdown = wait_for_element(wait, (By.XPATH, "//div[@title='Times, serif']//div[@class='ant-select-item-option-content']"))
        Dropdown.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Family is Edited successfully")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def select_size(wait):
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Font Size']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Size screen is opened")
def new_fontsize(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Font Size']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Size label is added")

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Size Value is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def edit_fontsize(wait, variable_value):
    try:

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Font Size Value is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#-----------------------------------------------------------------------------------------------------------------------
def select_spacing(wait):
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Spacing']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Spacing screen is opened")

def new_spacing(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Spacing']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Spacing label is added")

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Spacing Value is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_spacing(wait, variable_value):
    try:

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Spacing Value is edited")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#----------------------------------------------------------------------------------------------------------
def select_radius(wait):
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Radius']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Radius' screen is opened")

def new_radius(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Value']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Radius label is added")
        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Radius Value is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_radius(wait, variable_value):
    try:

        value = wait_for_element(wait, (By.XPATH, "//input[@role='spinbutton']"))
        value.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Spacing Value is edited")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#=------------------------------------------------------------------------------------------------------
def select_gradient(wait):
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Gradient']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Gradient screen is opened")

def new_gradient(wait, variable_name):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Gradient']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Gradient label is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def edit_gradient(wait,variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Gradient']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Gradient label is added")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
#------------------------------------------------------------------------------------------------------
def select_shadow(wait):
        FontSze_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Shadow']"))
        sleep(WAIT_TIME_SHORT)
        FontSze_tab.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Gradient screen is opened")
def new_shadow(wait, variable_name, variable_value):
    try:

        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Shadow']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Shadow label is added")

        value1 = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Spr']"))
        value1.send_keys(variable_value)
        sleep(WAIT_TIME_SHORT)
        logging.info("Shadow Value is added")

        value2 = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value2.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Colors Menu is opened")

        blur = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Blur']"))
        blur.send_keys("2")
        sleep(WAIT_TIME_SHORT)
        logging.info("Blurr value is added")

        color = wait_for_element(wait, (By.XPATH, "(//div)[162]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Color is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def edit_shadow(wait):
    try:
        value = wait_for_element(wait, (By.CSS_SELECTOR, ".ant-color-picker-color-block-inner"))
        value.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Colors Menu is opened")
        blur = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Blur']"))
        blur.send_keys("2")
        sleep(WAIT_TIME_SHORT)
        logging.info("Blurr value is added")
        color = wait_for_element(wait, (By.XPATH, "//div[28]//div[1]"))
        color.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Color is selected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

#-----------------------------------------------------------------------------------------------------------------------

def select_items(wait):
        items_tab = wait_for_element(wait, (By.XPATH, "//a[normalize-space()='Items per Row']"))
        sleep(WAIT_TIME_SHORT)
        items_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Items Per Row screen is opened")

def new_items(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "(//input[@value='New Items per Row'])[1]"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        logging.info("Items label is added")

        noofcols = wait_for_element(wait, (By.XPATH, "(//span[@aria-label='Increase Value'])[1]"))
        noofcols.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("No. of columns Value is increased")

        col = wait_for_element(wait, (By.XPATH, "(//span[@aria-label='Increase Value'])[2]"))
        col.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("One column Value is increased")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

