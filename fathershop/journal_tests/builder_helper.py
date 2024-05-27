import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT, click_element, wait_for_element

#———————————————————————————————————————————
def add_row_btn(wait):
    try:
        add_row = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='new-item button']//a")))
        add_row.click()
        sleep(WAIT_TIME_SHORT)
        print("New Row is added")
    except Exception as e:
        print(f"Error occurred on Clicking Add Row button method: {e}")
        raise
#———————————————————————————————————————
def add_column_btn(self):
    try:
        hover = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".position-heading.row-heading")))
        ActionChains(self.driver).move_to_element(hover).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")
        add_col = self.wait.until(EC.element_to_be_clickable((By.ID, "add-column")))
        # Click the element after hovering
        add_col.click()
        sleep(WAIT_TIME_MEDIUM)
        print("New Column is added")
    except Exception as e:
        print(f"Error occurred on Clicking Add Column button method: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_module(self):
    try:
        hover3 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".position-heading.row-heading")))
        ActionChains(self.driver).move_to_element(hover3).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")
        add_mod_btn  = self.wait.until(EC.element_to_be_clickable((By.ID, "add-module")))
        add_mod_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Module is added")
    except Exception as e:
        print(f"Error occurred on Clicking Add Module button method: {e}")
        raise
#———————————————————————————————————————————————————
def select_module(wait):
    try:
        add_module_btn= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "module-id")))
        add_module_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("My Module screen is opened")
        my_module = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='item-name'])[5]")))
        my_module.click()
        sleep(WAIT_TIME_SHORT)
        print("Info Blocks Module is clicked")
        select_module = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='variable-name'])[1]")))
        select_module.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Info  Homepage Module Menu is selected")

    except Exception as e:
        print(f"Error occurred in adding module button method: {e}")
        raise
#————————————————————————————————————————————————
def edit_column(wait):
    try:
        hover1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "position-heading column-heading")))
        ActionChains(wait.driver).move_to_element(hover1).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")
        edit_col  = wait.until(EC.element_to_be_clickable((By.ID, "edit-column")))
        edit_col.click()
        sleep(WAIT_TIME_SHORT)
        print("Edit column menu is opened")
    except Exception as e:
        print(f"Error occurred in edit column method: {e}")
        raise
#————————————————————————————————————————————————————
def duplicate_row(self):
    try:
        hover2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position-heading column-heading']")))
        ActionChains(self.driver).move_to_element(hover2).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")

        row = self.wait.until(EC.element_to_be_clickable((By.ID, "duplicate-row")))
        row.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Row is duplicated")
    except Exception as e:
        print(f"Error occurred in Row duplicate method: {e}")
        raise
#————————————————————————————————————————————————————————————
def delete_row(self):
    try:
        hover3 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position-heading column-heading']")))
        ActionChains(self.driver).move_to_element(hover3).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")

        row1= self.wait.until(EC.element_to_be_clickable((By.ID, "delete-row")))
        row1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Row is deleted")
    except Exception as e:
        print(f"Error occurred in Row duplicate method: {e}")
        raise


#——————————————————————————————————————————————————————————
def duplicate_column(self):
    try:
        hover4 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position-heading column-heading']")))
        ActionChains(self.driver).move_to_element(hover4).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")
        col_1  = self.wait.until(EC.element_to_be_clickable((By.ID, "duplicate-column")))
        col_1.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Column is duplicated")
    except Exception as e:
        print(f"Error occurred in Column duplicate method: {e}")
        raise

#————————————————————————————————————————————————————————————
def delete_column(self):
    try:
        hover5 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position-heading column-heading']")))
        ActionChains(self.driver).move_to_element(hover5).perform()
        sleep(WAIT_TIME_SHORT)
        print("Row Section hovered")
        col2  = self.wait.until(EC.element_to_be_clickable((By.ID, "delete-column")))
        col2.click()
        sleep(WAIT_TIME_SHORT)
        print("Column is deleted")

    except Exception as e:
        print(f"Error occurred in delete Column method: {e}")
        raise