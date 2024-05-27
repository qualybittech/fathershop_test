import pytest
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from selenium.webdriver.support.ui import WebDriverWait
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium_helpers import login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,edit, click_back_btn,reset_btn,color,\
    image_options
from header_helpers import navigate_to_header_screen,top_menu_edit,Topmenu_create,Top_menu_addNewItem,Add_menuTitle,random,Topmenu_addDetails

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
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
          self.results["Navigation to headerer Screen"] = "Passed"
      except Exception as e:
          self.results["Navigation to headerer Screen"] = f"Failed: {e}"

    def check_cache_btn(self):
      try:
        check_cache_btn(self.wait)
        self.results["Cache button s clicked"] = "Passed"
      except Exception as e:
         self.results["Cache button s clicked"] = f"Failed: {e}"

    def no_element_dropdown(self):
      try:
        no_element_dropdown(self.wait)
        self.results["No_of elements button clicking & list"] = "Passed"
      except Exception as e:
          self.results["No_of elements button clicking & list"] = f"Failed: {e}"

    def duplicate(self):
      try:
        duplicate(self.wait)
        self.results["duplicate button is clicked"] = "Passed"
      except Exception as e:
       self.results["duplicate button is clicked"] = f"Failed: {e}"

    def delete(self):
      try:

        delete(self.wait)
        self.results["delete button is clicked"] = "Passed"
      except Exception as e:
       self.results["delete button is clicked"] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Filter Search result is showing"] = "Passed"
        except Exception as e:
            self.results["Filter Search"] = f"Failed: {e}"

    def edit(self):
        edit(self.wait)

    def top_menu_edit(self):
        top_menu_edit(self.wait)
    def click_back_btn(self):
        click_back_btn(self.wait)

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Header Button"] = "Passed"
        except Exception as e:
            self.results["Create New Header Button"] = f"Failed: {e}"

    def Topmenu_create(self, variable_name):
        try:
            Topmenu_create(self.wait, variable_name)
            self.results["Topmenu_create"] = "Passed"
        except Exception as e:
            self.results["Topmenu_create"] = f"Failed: {e}"

    def Top_menu_addNewItem(self):
        Top_menu_addNewItem(self.wait)

    def random(self):
        random(self)

    def Add_menuTitle(self, variable_name):
        try:
            Add_menuTitle(self.wait, variable_name)  # pass self.wait instead of self
            self.results["Add Menu Title"] = "Passed"
        except Exception as e:
            self.results["Add Menu Title"] = f"Failed: {e}"

    def Topmenu_addDetails(self, variable_name):
        try:
            Topmenu_addDetails(self.wait, variable_name)  # pass self.wait instead of self
            self.results["Add Menu Title"] = "Passed"
        except Exception as e:
            self.results["Add Menu Title"] = f"Failed: {e}"

    def color(self):
        color(self.wait)

    def image_options(self):
        image_options(self.wait)

    def reset_btn(self):
        reset_btn(self.wait)


    def write_to_excel(self):
        excel_path = "header_results.xlsx"  # Path to the Excel file
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Header_Test Results"
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
        driver.set_window_size(1280, 1000)  # Set to a reasonable size

        yield driver
        driver.quit()

    def test_header_functions(self, setup):
        driver = setup

        header= Header(driver)
        header.login()
        header.navigate_to_header_screen()
        #header.check_cache_btn()
        #header.duplicate()
        #header.filter_search("Top")
        header.create_new_btn()
        header.Topmenu_create( " Test")
        header.Top_menu_addNewItem()
        header.random()
        header.click_back_btn()
        header.edit()


        #header.Add_menuTitle("Category_Test")
        #header.color()
        #header.image_options()

        #header.reset_btn()
        #header.edit()
        #header.top_menu_edit()
        #header.reset_btn()
        #header.Topmenu_addDetails()

        #header.no_element_dropdown()
        #header.delete()


        #header.top_menu_edit()



