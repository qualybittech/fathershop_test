import pytest
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium_helpers import login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,gradient,camera,save
from mainmenu_helper import add_offset
from header_helpers import navigate_to_header_screen,Top_menu_addNewItem,topmenu_addstatus,click_hovertab,select_icon,select_size,additional_option1,additional_option2,\
top_menu_edit,edit_select_icon,header_color
from classic_helper import navigat_to_classic,open_global_options,fullwidth_border,padding,header_height,max_width,open_homepage_override,shadow_dropdown,\
position,click_tab_by_name,cont_padding,header_max_width,item_btn
from button_helpers import open_menuitem,create_newstyle_btn,enter_stylelabel


class Classic:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.results = {}

    def login(self):
        try:
            login(self.wait, self.driver, USERNAME, PASSWORD)
            self.results["Login"] = "Passed"
        except Exception as e:
            self.results["Login"] = f"Failed: {e}"
    def navigate_to_header_screen(self):
      try:
          navigate_to_header_screen(self)
          self.results["Navigation to header Screen"] = "Passed"
      except Exception as e:
          self.results["Navigation to headerer Screen"] = f"Failed: {e}"

    def navigat_to_classic(self):
        try:
            navigat_to_classic(self.wait)
            self.results["Classic Screen is opened"] = "Passed"
        except Exception as e:
            self.results["Classic Screen is not opened"] = f"Failed: {e}"


    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Button is clicked "] = "Passed"
        except Exception as e:
            self.results["Create New Button is not clicked "] = f"Failed: {e}"

    def open_global_options(self):
        try:
            open_global_options(self.wait)
            self.results["Global Options dropdown menu is clicked "] = "Passed"
        except Exception as e:
            self.results["Global Options dropdown menu is not clicked "] = f"Failed: {e}"

    def gradient(self):
        try:
         gradient(self.wait)
         self.results["In Item Background Gradient has been selected"] = "Passed"
        except Exception as e:
            self.results["In Item Background Gradient has not been selected"] = f"Failed: {e}"

    def camera(self):
        try:
         camera(self.wait)
         self.results["In Background Camera Image has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Camera Image has not been selected"] = f"Failed: {e}"

    def header_color(self):
        try:
            header_color(self.wait)
            self.results["The Icon Color has been selected"] = "Passed"
        except Exception as e:
            self.results["The Icon Color has not been selected"] = f"Failed: {e}"

    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Top menu Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Top menu Screen are not Saved"] = f"Failed: {e}"

    def fullwidth_border(self,value):
        try:
            fullwidth_border(self.wait,value)
            self.results["fullwidth_border value is added"] = "Passed"
        except Exception as e:
            self.results["fullwidth_bordervalue is not added"] = f"Failed: {e}"

    def padding(self,value):
        try:
            padding(self.wait,value)
            self.results["header_padding value is added"] = "Passed"
        except Exception as e:
            self.results["header_padding is not added"] = f"Failed: {e}"

    def cont_padding(self,value):
        try:
            cont_padding(self.wait,value)
            self.results["container padding value is added"] = "Passed"
        except Exception as e:
            self.results["container padding is not added"] = f"Failed: {e}"

    def max_width(self,value):
        try:
            max_width(self.wait,value)
            self.results["header_padding value is added"] = "Passed"
        except Exception as e:
            self.results["header_padding is not added"] = f"Failed: {e}"

    def header_height(self):
        try:
            header_height(self.wait)
            self.results["header_heightvalue is added"] = "Passed"
        except Exception as e:
            self.results["header_height is not added"] = f"Failed: {e}"

    def header_max_width(self):
        try:
            header_max_width(self.wait)
            self.results["header_max_width is added"] = "Passed"
        except Exception as e:
            self.results["header_max_width is not added"] = f"Failed: {e}"

    def open_homepage_override(self):
        try:
            open_homepage_override(self.wait)
            self.results["header_max_width is added"] = "Passed"
        except Exception as e:
            self.results["header_max_width is not added"] = f"Failed: {e}"


    def position(self,value):
        try:
            position(self.wait,value)
            self.results[" position is selected"] = "Passed"
        except Exception as e:
            self.results[" positionnot selected"] = f"Failed: {e}"

    def add_offset(self,x_value, y_value):
        try:
            add_offset(self,x_value, y_value)
            self.results["Text Padding value is added"] = "Passed"
        except Exception as e:
            self.results["Text Padding value is not added"] = f"Failed: {e}"

    def click_tab_by_name(self,tab_name):
        try:
            click_tab_by_name(self.wait,tab_name)
            self.results["Topbar Tab is selected"] = "Passed"
        except Exception as e:
            self.results["Topbar Tab not selected"] = f"Failed: {e}"

    def  create_newstyle_btn(self):
        try:
            create_newstyle_btn(self.wait)
            self.results["Clicking on Create New Style button is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on Create New Style button  is not successful"] = f"Failed: {e}"

    def enter_stylelabel(self, variable_name):
        try:
            enter_stylelabel(self.wait, variable_name)
            self.results["Style label is entered"] = "Passed"
        except Exception as e:
            self.results["Style label is not entered"] = f"Failed: {e}"

    def item_btn(self):
        try:
            item_btn(self.wait)
            self.results["item_btn toggle button is clicked successfuly"] = "Passed"
        except Exception as e:
            self.results["Clicking on item_btn toggle button is not successful"] = f"Failed: {e}"

    def write_to_excel(self):
        excel_path = "classic_header_results.xlsx"  # Path to the Excel file
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Classic_Header_Test Results"
        sheet["A1"] = "Executed Steps"
        sheet["B1"] = "Result"
        sheet["A1"].alignment = Alignment(horizontal='center')
        sheet["B1"].alignment = Alignment(horizontal='center')

        row_index = 2  # Start writing from row 2
        for test_case, result in self.results.items():
            sheet[f"A{row_index}"] = test_case
            sheet[f"B{row_index}"] = result
            row_index += 1
        try:
            wb.save(excel_path)
        except Exception as e:
            print(f"An error occurred while writing to Excel: {e}")



class TestFathershopTheme:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        #driver.maximize_window()
        driver.set_window_size(1380, 1200)  # Set to a reasonable size

        yield driver
        driver.quit()

    def test_header_classic_functions(self, setup):
        driver = setup

        classic= Classic(driver)
        classic.login()
        classic.navigate_to_header_screen()
        classic.navigat_to_classic()
        classic.create_new_btn()


        classic.open_global_options()
        classic.header_color()
        classic.gradient()
        classic.camera()
        classic.padding("10")
        classic.fullwidth_border("10")
        classic.open_homepage_override()
# ----------------------------------------------------
        classic.click_tab_by_name("Logo")
        classic.header_color()
        classic.gradient()
        classic.camera()
        classic.cont_padding("10")
        classic.add_offset("10", "10")
# ----------------------------------------------------
        classic.click_tab_by_name("Top Bar")
        classic.header_color()
        classic.gradient()
        classic.camera()
        classic.fullwidth_border("10")
        classic.padding("10")
#----------------------------------------------------
        classic.click_tab_by_name("Top Menu")


        classic.click_tab_by_name("Top Menu 2")

        classic.click_tab_by_name("Secondary Menu")
        classic.click_tab_by_name("Language/Currency")
        classic.click_tab_by_name("Search")

        classic.save()


        #classic.open_logo_tab()

        #classic.open_global_options()
        #classic.header_color()
        #classic.gradient()
        #classic.camera()

        #classic.fullwidth_border("10")
        #classic.header_padding("10")
        #classic.header_height()
        #classic.open_homepage_override()
        #classic.position("10")
       # classic.header_color()
       # classic.gradient()
        #classic.camera()
        #classic.add_offset()
#-------------------------------------------------




