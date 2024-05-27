from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, wait_for_element


def create_newstyle_btn(wait):
    try:
        new_style_btn = wait_for_element(wait, (By.XPATH, "//a[@class='ui-create']"))
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

def open_menuitem(wait):
    try:
        menu_item = wait_for_element(wait, (By.CSS_SELECTOR, "..accordion-heading.id_menu"))
        menu_item.click()
        sleep(WAIT_TIME_SHORT)
        print("Menu item dropdown is opened successfuly")
    except Exception as e:
        print(f"An error occurred on clicking Menu item dropdown : {e}")
        raise