import pytest
from selenium import webdriver
from selenium_helpers import login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,edit,color,gradient,camera,image_options,save,click_back_btn,add_breakpoint_btn,edit_color,edit_gradient,edit_camera
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from styles_helpers import navigate_to_styles_screen, new_label,select_options,open_general,open_site_container,open_content_container,open_side_column,max_width_btn,add_Padding,close_general,close_site_container,close_content_container,close_side_column,open_right_column,\
    close_right_column,open_boxedoption,close_boxedoption,col_btn,select_none
class GlobalStyles:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
    def login(self):
        login(self.wait, self.driver, USERNAME, PASSWORD)# Utilizing imported constants and helper function
    def navigate_to_styles_screen(self):
        navigate_to_styles_screen(self)
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

    def  select_options(self):
         select_options(self.wait, self.driver)

    def open_general(self):
        open_general(self.wait)

    def close_general(self):
        close_general(self.wait)

    def open_boxedoption(self):
        open_boxedoption(self.wait)

    def close_boxedoption(self):
        close_boxedoption(self.wait)
    def open_site_container(self):
        open_site_container(self.wait)
    def close_site_container(self):
        close_site_container(self.wait)
    def open_content_container(self):
        open_content_container(self.wait)

    def close_content_container(self):
        close_content_container(self.wait)

    def open_side_column(self):
        open_side_column(self.wait)

    def close_side_column(self):
        close_side_column(self.wait)

    def open_right_column(self):
        open_right_column(self.wait)

    def close_right_column(self):
        close_right_column(self.wait)

    def max_width_btn(self):
        max_width_btn(self.wait)
    def add_Padding(self, value):
        add_Padding(self.wait, value)
    def col_btn(self):
        col_btn(self.wait)
    def select_none(self):
        select_none(self.wait)

    def edit_color(self):
        edit_color(self.wait)

    def edit_gradient(self):
        edit_gradient(self.wait)

    def edit_camera(self):
        edit_camera(self.wait)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def test_styles_functions(self, setup):
        driver = setup

        styles = GlobalStyles(driver)
        styles.login()
        styles.navigate_to_styles_screen()
        styles.check_cache_btn()
        styles.filter_search("Def")
        styles.create_new_btn()
        styles.new_label(" Test")
        styles.open_general()
        styles.select_options()
        styles.color()
        styles.gradient()
        styles.camera()
        styles.close_general()
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.open_boxedoption()
        styles.max_width_btn()
        styles.add_Padding("10")
        styles.color()
        styles.close_boxedoption()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.open_site_container()
        styles.max_width_btn()
        styles.color()
        styles.gradient()
        styles.camera()
        styles.add_Padding("10")
        styles.close_site_container()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.open_content_container()
        styles.max_width_btn()
        styles.color()
        styles.gradient()
        styles.camera()
        styles.close_content_container()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.open_side_column()
        styles.col_btn()
        styles.color()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.open_right_column()
        styles.select_none()
        styles.save()
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        styles.edit()
        styles.open_general()
        styles.edit_color()
        styles.edit_gradient()
        styles.edit_camera()
        styles.save()


