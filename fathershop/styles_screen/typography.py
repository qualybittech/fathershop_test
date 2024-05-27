import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from constants import WAIT_TIME_SHORT, WAIT_TIME_MEDIUM,click_element
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium_helpers import  wait_for_element,login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,edit,color,gradient,camera,image_options,save,click_back_btn,add_breakpoint_btn,\
edit_camera,edit_gradient,edit_color
from styles_helpers import navigate_to_styles_screen, new_label,max_width_btn,add_Padding,col_btn,select_none
class Typography:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
    def login(self):
        login(self.wait, self.driver, USERNAME, PASSWORD)

    def navigate_to_styles_screen(self):
        navigate_to_styles_screen(self)

    def navigate_to_typograpghy(self):
            try:

                typo = wait_for_element(self.wait,(By.XPATH, "//a[normalize-space()='Typography']"))
                sleep(WAIT_TIME_MEDIUM)
                typo.click()
                print("Typography screen is opened successfully")
            except Exception as e:
                print(f"An error occurred in typograpgy method: {e}")
                raise
    def check_cache_btn(self):
        check_cache_btn(self.wait)

    def no_element_dropdown(self):
        no_element_dropdown(self.wait)

    def duplicate(self):
        duplicate(self.wait)

    def delete(self):
        delete(self.wait)
    def filter_search(self, search_term):
        filter_search(self.wait, search_term)

    def edit(self):
        edit(self.wait)

    def color(self):
        color(self.wait)

    def gradient(self):
        gradient(self.wait)

    def camera(self):
        camera(self.wait)

    def image_options(self):
        image_options(self.wait)

    def save(self):
        save(self.wait)

    def click_back_btn(self):
        click_back_btn(self.wait)

    def create_new_btn(self):
        create_new_btn(self.wait)

    def new_label(self, variable_name):
        new_label(self.wait, variable_name)
#————————————————————————————————————————————————————
class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()

#———————————————————————————————————————————————————————
    def test_styles_functions(self, setup):
        driver = setup

        typo = Typography(driver)
        typo.login()
        typo.navigate_to_styles_screen()
        typo.navigate_to_typograpghy()
        #typo.check_cache_btn()
        #typo.duplicate()
        #typo.delete()
        #typo.no_element_dropdown()
        typo.filter_search("Te")

#———————————————————————————————————————————————————————


