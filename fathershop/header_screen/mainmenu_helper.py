from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, wait_for_element


def click_main_menu(wait):
    try:
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Main Menu']")))
        menu.click()
        sleep(WAIT_TIME_SHORT)
        print("Main Menu is opened")
    except Exception as e:
        print(f"An error occurred on clicking Main Menu Tab: {e}")
        raise
#—————————————————————————————————————————————————————————————

def enter_modulename(wait, variable_name):
    try:
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Main Menu']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        print("Main Menu Module Name is added")
    except Exception as e:
        print(f"An error occurred in Main Menu Module Name method: {e}")
        raise
#—————————————————————————————————————————————————————————————

def mainmenu_name(wait,variable_name1,variable_name2):
    try:
        item_name = wait_for_element(wait, (By.XPATH, "(//input[@value='Menu Item'])[1]"))
        item_name.send_keys(variable_name1)
        sleep(WAIT_TIME_MEDIUM)
        print("Item Name is entered")
        menu_Title = wait_for_element(wait, (By.XPATH, "(//input[@value='Menu Item'])[2]"))
        menu_Title .send_keys(variable_name2)
        sleep(WAIT_TIME_MEDIUM)
        print("Menu title is entered")

    except TimeoutException:
        print("Error Timeout occurred:")
        # Wait for 2 seconds before retrying
        raise
    except Exception as e:
        print(f"Error in the random Item method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def click_styles_override(wait):
    try:
        styles_override_tab = wait_for_element(wait, (
        By.XPATH, "//ul[@class='tab_items']/li[contains(text(), 'StylesOverride')]"))
        styles_override_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Style Override tab is opened successfully")
    except Exception as e:
        print(f"An error occurred on clicking styles override method: {e}")
        raise


#———————————————————————————————————————————————————
def item_padding(wait,value):
    try:
         add_padding_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_padding_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Padding value is added")

    except Exception as e:
        print(f"Error in adding Paddng value method: {e}")
        raise
#———————————————————————————————————————————————————
def item_border_radius(wait,value):
    try:
         add_border_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='TL'])[1]")))
         add_border_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Item Border Radius value is added")

    except Exception as e:
        print(f"Error in adding Item Border Radius value method: {e}")
        raise
#————————————————————————————————————————————————————

def text_border_dropdown(wait):
    try:
         border_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-select-selection-search")))
         border_dropdown.click()
         sleep(WAIT_TIME_SHORT)
         print("Text border dropdown is opened")
         dropdown_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Dashed']")))
         dropdown_option.click()
         sleep(WAIT_TIME_SHORT)
         print("Text border dropdown option is opened")

    except Exception as e:
        print(f"Error on selecting Text border dropdown option method: {e}")
        raise
#————————————————————————————————————————————————————
def text_border(wait,value):
    try:
         text_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[2]")))
         text_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Item Border Radius value is added")

    except Exception as e:
        print(f"Error in adding Item Border Radius value method: {e}")
        raise
#———————————————————————————————————————————————————————————
def text_padding(wait,value):
    try:
         text_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[3]")))
         text_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         print("Text Padding value is added")

    except Exception as e:
        print(f"Error in adding Text Paddng value method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def min_width_btn(wait):
    try:
        width = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[1]")))
        width.click()
        sleep(WAIT_TIME_SHORT)
        print("Width is added ")
    except Exception as e:
        print(f"Error clicking on min width button method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def click_dropdown_triangle(wait):
    try:
        tri = wait_for_element(wait, (By.XPATH, "(//div[@class='accordion-heading id_triangle'])[1]"))
        tri.click()
        sleep(WAIT_TIME_SHORT)
        print("Dropdown Triangle tab is opened successfuly")
    except Exception as e:
        print(f"An error occurred on clicking Dropdown Trianglemethod: {e}")
        raise

#————————————————————————————————————————————————————
def add_offset(wait, x_value, y_value):
    try:
        x_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='X'])[1]")))
        x_input.send_keys(x_value)
        sleep(WAIT_TIME_SHORT)
        print("X offset value is added")
        y_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Y'])[1]")))
        y_input.send_keys(y_value)
        sleep(WAIT_TIME_SHORT)
        print("Y offset value is added")
    except Exception as e:
        print(f"Error in adding offset value method: {e}")
        raise
#—————————————————————————————————————————————————————————————
def click_menulabel(wait):
    try:
        menu_label_tab = wait_for_element(wait,(By.XPATH, "//ul[@class='tab_items']/li[contains(text(), 'MenuLabel')]"))
        menu_label_tab.click()

        sleep(WAIT_TIME_SHORT)
        print("Menu label tab is opened successfully")
    except Exception as e:
        print(f"An error occurred on clicking Menu label method: {e}")
        raise

#—————————————————————————————————————————————————————————————

def enter_menulabel(wait, variable_name):
    try:
        menulabel = wait_for_element(wait, (By.XPATH, "(//input[@class='w-full'])[1]"))
        menulabel.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Menu label Name is added")
    except Exception as e:
        print(f"An error occurred in Main Menu Module Name method: {e}")
        raise
#—————————————————————————————————————————————————————————————

def create_newstyle_btn(wait):
    try:
        new_style_btn = wait_for_element(wait, (By.XPATH, "(//input[@class='w-full'])[1]"))
        new_style_btn .click()
        sleep(WAIT_TIME_SHORT)
        print("Create New Style button is clicked successfuly")
    except Exception as e:
        print(f"An error occurred on clicking Create New Style button : {e}")
        raise
#—————————————————————————————————————————————————————————————
def enter_stylelabel(wait, variable_name):
    try:
        enterlabel = wait_for_element(wait, (By.XPATH, "(//input[@value='New Table'])[1]"))
        enterlabel.send_keys(variable_name)
        sleep(WAIT_TIME_SHORT)
        print("Style label Name is added")
    except Exception as e:
        print(f"An error occurred in Style label method: {e}")
        raise
def click_tab2(wait, tab_name):
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
