from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIME_MEDIUM, WAIT_TIME_SHORT,WAIT_TIME_LONG ,click_element, wait_for_element


def navigate_to_header_screen(self):
    try:
        click_element(self.wait, (By.CSS_SELECTOR, ".menu-icon.brio-menu.rounded"))
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Clicked on the Collapased Tab successfully.")
    # Directly mouse hover over the "Theme" tab using a relative CSS selector
        theme_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//span[@class='menu-name']"))
    # Mouse hover over the "Theme" tab
        ActionChains(self.driver).move_to_element(theme_tab).perform()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Mouse hovered over the 'Theme' tab")
    # Click on the "Theme" tab
        theme_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Theme tab is clicked successfully")
     # Hover over the "styles_tab" element
        header_tab = wait_for_element(self.wait, (By.XPATH, "//li[@id='journal3-theme']//li[5]//a[1]"))
        ActionChains(self.driver).move_to_element(header_tab).perform()
        sleep(WAIT_TIME_MEDIUM)  # Using imported constant
        print("Mouse hovered over 'Header_tab'")

        # Click on the "styles_tab"
        header_tab.click()
        sleep(WAIT_TIME_SHORT)  # Using imported constant
        print("Header_tab clicked successfully")
    except Exception as e:
        # Catch any other exceptions that may occur
        print(f"Error occurred in accessing Header Screen from Dashboard Left column: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————————————

def Topmenu_modulename(wait, variable_name):
    try:
        general_tab = wait_for_element(wait, (By.CSS_SELECTOR, ".accordion-heading.id_general"))
        general_tab.click()
        sleep(WAIT_TIME_SHORT)
        enter_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Top Menu']"))
        enter_name.send_keys(variable_name)
        sleep(WAIT_TIME_MEDIUM)
        print("New Top Menu Name is added")
    except Exception as e:
        print(f"An error occurred in Top menu_name method: {e}")
        raise

#—————————————————————————————————————————————————————————————————————————————————————————————
def Top_menu_addNewItem(wait):
    try:
        click_addBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='new-item button'])[1]")))
        click_addBtn.click()
        sleep(WAIT_TIME_SHORT)
        print("New Item button is clicked")

        clone = wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='icon icon-clone']")))
        sleep(WAIT_TIME_SHORT)
        clone.click()
        print("New item is duplicated")

        opengeneral_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".accordion-heading.id_-1")))
        sleep(WAIT_TIME_SHORT)
        opengeneral_tab.click()
        print("New Item General dropdown menu is showing")

    except TimeoutException:
        print("Timeout occurred:")
         # Wait for 2 seconds before retrying
        raise
    except Exception as e:
        print(f"Error in Add New Item method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————————
def topmenu_name(wait,variable_name1,variable_name2):
    try:
        item_name = wait_for_element(wait, (By.XPATH, "//input[@value='New Item']"))
        item_name.send_keys(variable_name1)
        sleep(WAIT_TIME_MEDIUM)
        print("Item Name is entered")
        menu_Title = wait_for_element(wait, (By.XPATH, "(//input[@class='w-full'])[2]"))
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

#—————————————————————————————————————————————————————————————————————————————————————————————

def topmenu_addstatus(wait):
    try:
        device = wait_for_element(wait, (By.XPATH, "(//li)[30]"))
        device.click()
        sleep(WAIT_TIME_SHORT)
        print("Device tab is clicked")

        customer = wait_for_element(wait, (By.XPATH, "(//li)[31]"))
        customer.click()
        sleep(WAIT_TIME_SHORT)
        print("Customer tab is clicked")

        guest = wait_for_element(wait, (By.XPATH, "(//label[@class='is-checked'])[1]"))
        guest.click()
        sleep(WAIT_TIME_SHORT)
        print("Guest sub-tab is clicked")


        cust_grp = wait_for_element(wait, (By.XPATH, "(//li)[32]"))
        cust_grp.click()
        sleep(WAIT_TIME_SHORT)
        print("Customer Group tab is clicked")

        admin = wait_for_element(wait, (By.XPATH, "(//li[@class='tab-active'])[2]"))
        admin .click()
        sleep(WAIT_TIME_SHORT)
        print("Admin Only tab is clicked")

        admin_status=wait_for_element(wait, (By.XPATH, "(//label)[1]"))
        admin_status.click()
        sleep(WAIT_TIME_SHORT)
        print("Admin Only status is ON")
    except Exception as e:
        print(f"An error occurred in Adding Status method: {e}")
        raise

#——————————————————————————————————————————————————————————————————————————————————————————————————————————
def top_menu_edit(wait):
    try:
        click_edit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "item-icon")))
        click_edit_btn.click()
        sleep(WAIT_TIME_SHORT)
        print("Edit Icon is clicked")
        tab = wait.until(EC.element_to_be_clickable((By.ID, "0116381e-c4bf-4e63-8088-8459798fd4de")))
        tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Account tab is opened")
        open_general1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion-heading.id_-1")))
        open_general1.click()
        sleep(WAIT_TIME_SHORT)
        print("General dropdown is opened")
    except Exception as e:
        print(f"Error in edit method: {e}")
        raise
#————————————————————————————————————————————————————————————————————————————————————————
def select_icon(wait):
    try:
        icon = wait_for_element(wait, (By.CSS_SELECTOR, ".ui-icon-preview"))
        icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon Menu is opened successfuly")

        icon_image = wait_for_element(wait, (By.XPATH, "(//i[@class='icon icon-noun_bag_865857_000000'])[1]"))
        icon_image.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon image is selected")
    except Exception as e:
        print(f"An error occurred in Adding Menu Title name method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————
def edit_select_icon(wait):
    try:
        icon = wait_for_element(wait, (By.CSS_SELECTOR, ".ui-icon-preview"))
        icon.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon Menu is opened successfuly")
        icon_image = wait_for_element(wait, (By.XPATH, "//i[@class='icon icon-sidebar']"))
        icon_image.click()
        sleep(WAIT_TIME_SHORT)
        print("Icon image is edited")
    except Exception as e:
        print(f"An error occurred in Adding Menu Title name method: {e}")
        raise
#—————————————————————————————————————————————————————————————————————————————————
def header_color(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        select_color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color menu is opened")

        color = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[11]//div[1]")))
        color.click()  # Added parentheses to actually call the click method
        sleep(WAIT_TIME_SHORT)
        print("Color is selected")

    except Exception as e:
        print(f"Error occurred in color method: {e}")
        raise

#—————————————————————————————————————————————————————————————————————————————————
def edit_header_color(wait):
    try:
        select_color = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-color-picker-color-block-inner")))
        select_color.click()
        sleep(WAIT_TIME_SHORT)
        color = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div)[382]")))
        color.click()
        sleep(WAIT_TIME_SHORT)
        print("Color is edited")

    except Exception as e:
        print(f"Error occurred in color method: {e}")
        raise

#————————————————————————————————————————————————————————————————————————————————————————
def select_size(wait,size):
    try:
        enter_size = wait_for_element(wait, (By.XPATH, "//input[@placeholder='Size']"))
        enter_size.send_keys(size)
        sleep(WAIT_TIME_SHORT)
        print("Size Value is added successfuly")
    except Exception as e:
        print(f"An error occurred in Adding Menu Title name method: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————
def click_hovertab(wait):
    try:
        hover_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"(//li[contains(text(),'Hover')])[1]")))
        hover_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Hover Tab is clicked")
    except Exception as e:
        print(f"An error occurred on clicking Hover Tab: {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————
def additional_option1(wait,X,Y):
    try:
        option_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@type='primary'])[1]")))
        option_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Additional Options_1 Menu Screen is opened")
        X_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='X']")))
        X_value.send_keys(X)
        sleep(WAIT_TIME_SHORT)
        print("X value is added")
        Y_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Y']")))
        Y_value.send_keys(Y)
        sleep(WAIT_TIME_SHORT)
        print("Y value is added")
    except Exception as e:
        print(f"An error occurred on clicking Additional Options_1 button : {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————
def additional_option2(wait,x,y,z):
    try:
        option2_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@type='primary'])[2]")))
        option2_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Additional Options_2 Menu Screen is opened")
        X_value = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='X'])[2]")))
        X_value.send_keys(x)
        sleep(WAIT_TIME_SHORT)
        print("X value is added")
        Y_value = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Y'])[2]")))
        Y_value.send_keys(y)
        sleep(WAIT_TIME_SHORT)
        print("Y value is added")
        Blur = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Blur'])[1]")))
        Blur.send_keys(z)
        sleep(WAIT_TIME_SHORT)
        print("Blurr value is added")
    except Exception as e:
        print(f"An error occurred on clicking Additional Options_2 button : {e}")
        raise

#———————————————————————————————————————————————————————————————————————————————————————
def additional_option3(wait):
    try:
        option3_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@type='primary'])[3]")))
        option3_tab.click()
        sleep(WAIT_TIME_SHORT)
        print("Additional Options_3 Menu Screen is opened")
        new_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[@class='is-checked'])[3]")))
        new_tab .click()
        sleep(WAIT_TIME_SHORT)
        print("New tab value is selected")

    except Exception as e:
        print(f"An error occurred on clicking Additional Options_1 button : {e}")
        raise
#——————————————————————————————————————————————————————————————————————————————————————————
