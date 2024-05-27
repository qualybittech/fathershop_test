import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_SHORT, WAIT_TIME_MEDIUM


def open_general(wait):

    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("General drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def close_general(wait):

    try:
        general = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_gen")))
        general.click()
        sleep(WAIT_TIME_SHORT)
        print("General drop-down section is closed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def open_site_container(wait):
    try:
        site = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_site']//div")))
        site.click()
        sleep(WAIT_TIME_MEDIUM)
        print("site_container drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def close_site_container(wait):
    try:
        site_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_site']//div")))
        site_container.click()
        sleep(WAIT_TIME_MEDIUM)
        print("Site Container section is closed ")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise


def open_content_container(wait):
    try:
        cont = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_content']//div")))
        cont.click()
        sleep(WAIT_TIME_SHORT)
        print("Content_container drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def close_content_container(wait):
    try:
        cont1 = wait.until(EC.element_to_be_clickable ((By.XPATH, "//div[@class='accordion-heading id_content']//div")))
        cont1.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Content_container drop-down section is closed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def open_side_column(wait):
    try:
        side = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_1']")))
        side.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Side_column drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def close_side_column(wait):
    try:
        side1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_1']")))
        side1.click()
        sleep(WAIT_TIME_SHORT)
        logging("Side_column drop-down section is closed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def open_right_column(wait):
    try:
        side2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_2']")))
        side2.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Right_column drop-down section is opened")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def close_right_column(wait):
    try:
        side3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accordion-heading id_2']")))
        side3.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Right_column drop-down section is closwed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
def max_width_btn(wait):
    try:
        width = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='Increase Value'])[1]")))
        width.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Width is added ")
    except Exception as e:
        logging.error(f"Error clicking on create_new button: {e}")
        raise
#———————————————————————————
def add_Padding(wait,value):
    try:
         add_padding_value= wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='ALL'])[1]")))
         add_padding_value.send_keys(value)
         sleep(WAIT_TIME_SHORT)
         logging.info("Padding value is added")

    except Exception as e:
        logging.error(f"Error clicking on max width button method: {e}")
        raise
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def max_col_btn(wait):
    try:
        col = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Increase Value']")))
        col.click()
        sleep(WAIT_TIME_SHORT)
        logging.info("Column is added ")
    except Exception as e:
        logging.error(f"Error in adding Paddng value method: {e}")
        raise