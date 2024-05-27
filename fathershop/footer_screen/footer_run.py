import pytest
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from selenium.webdriver.support.ui import WebDriverWait
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium_helpers import login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,edit,color,gradient,camera,save,click_back_btn,edit_color,edit_gradient,image_options
from footer_helper import navigate_to_footer_screen,footer_name,max_width_btn,add_Padding,footer_type,add_Margin,add_Border
from builder_helper import add_row_btn, add_column_btn,add_module,select_module,edit_column,duplicate_row,duplicate_column,delete_row,delete_column

class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)  # Reduced wait time to 20 seconds
        self.results = {}

    def login(self):
        try:
            login(self.wait, self.driver, USERNAME, PASSWORD)
            self.results["Fathersshop Login"] = " Passed"
        except Exception as e:
            self.results["Fathersshop Login"] = f" Failed: {e}"

    def navigate_to_footer_screen(self):
      try:
          navigate_to_footer_screen(self)
          self.results["Navigation to Footer Screen is successful"] = "Passed"
      except Exception as e:
          self.results["Navigation to Footer Screen is not successful"] = f"Failed: {e}"


    def check_cache_btn(self):
      try:
        check_cache_btn(self.wait)
        self.results["Cache button is clicked & working"] = "Passed"
      except Exception as e:
         self.results["Cache button s clicked & not working "] = f"Failed: {e}"

    def no_element_dropdown(self):
      try:
        no_element_dropdown(self.wait)
        self.results["No_of elements button clicking & list is showing"] = "Passed"
      except Exception as e:
          self.results["No_of elements button clicking & list is not showing"] = f" is Failed: {e}"

    def duplicate(self):
      try:
        duplicate(self.wait)
        self.results["Clicking on Footer duplicate button is successful"] = "Passed"
      except Exception as e:
       self.results["Footer duplicate button clicking is not successful"] = f"Failed: {e}"

    def delete(self):
      try:

        delete(self.wait)
        self.results["Clicking on Footer delete button is successful"] = "Passed"
      except Exception as e:
       self.results["Footer delete button clicking is not successful"] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Footer Search is showing the desired result"] = "Passed"
        except Exception as e:
            self.results["Footer Filter Search is not working"] = f"Failed: {e}"

    def edit(self):
        try:
         edit(self.wait)
         self.results["Edit button on Footer Screen is working "] = "Passed"
        except Exception as e:
            self.results["Edit button on Footer Screen is not working "] = "Passed"


    def click_back_btn(self):
        try:
         click_back_btn(self.wait)
         self.results["Back button on Footer Screen is working"] = "Passed"
        except Exception as e:
            self.results["Back button on Footer Screen is not working"] = f"Failed: {e}"

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Footer Create New Button is working"] = "Passed"
        except Exception as e:
            self.results["Footer Create New Button is not working"] = f"Failed: {e}"

    def footer_name(self, variable_name):
        try:
         footer_name(self.wait, variable_name)
         self.results["Footer Name is entered"] = "Passed"
        except Exception as e:
            self.results["Footer Name is not entered"] = f"Failed: {e}"

    def color(self):
        try:
         color(self.wait)
         self.results["In Background Color has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Color has not been selected"] = f"Failed: {e}"

    def gradient(self):
        try:
         gradient(self.wait)
         self.results["In Background Gradient has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Gradient has not been selected"] = f"Failed: {e}"

    def edit_color(self):
        try:
         edit_color(self)
         self.results["In Background Color has been edited"] = "Passed"

        except Exception as e:
            self.results["In Background Color is not edited"] = f"Failed: {e}"

    def edit_gradient(self):
        try:
         edit_gradient(self.wait)
         self.results["In Background Gradient has been edited"] = "Passed"
        except Exception as e:
            self.results["In Background Gradient is not edited"] = f"Failed: {e}"

    def camera(self):
        try:
         camera(self.wait)
         self.results["In Background Camera Image has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Camera Image has not been selected"] = f"Failed: {e}"

    def image_options(self):
        try:
         image_options(self.wait)
         self.results["In Background Image Options has been selected"] = "Passed"
        except Exception as e:
            self.results["In Background Image Options has not been selected"] = f"Failed: {e}"

    def add_Margin(self,value):
        try:
         add_Margin(self.wait,value)
         self.results["Margin value has been added"] = "Passed"
        except Exception as e:
            self.results["Margin value has not been added"] = f"Failed: {e}"


    def add_Padding(self, value):
        try:
         add_Padding(self.wait, value)
         self.results["Paddng value has been added"] = "Passed"
        except Exception as e:
            self.results["Paddng value has not been added"] = f"Failed: {e}"

    def add_Border(self,value):
        try:
         add_Border(self.wait,value)
         self.results["Border value has been added"] = "Passed"
        except Exception as e:
            self.results["Border value has not been added"] = f"Failed: {e}"

    def max_width_btn(self):
        try:
         max_width_btn(self.wait)
         self.results["Maximum width value has been added"] = "Passed"
        except Exception as e:
            self.results["Maximum width  value has not been added"] = f"Failed: {e}"


    def footer_type(self):
        try:
         footer_type(self.wait)
         self.results["Footer Type has been selected"] = "Passed"
        except Exception as e:
            self.results["Footer Type has not been selected"] = f"Failed: {e}"



    def add_row_btn(self):
        try:
         add_row_btn(self.wait)
         self.results["In the Builder section Row has been added"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Row has not been added"] = f"Failed: {e}"

    def add_column_btn(self):
        try:
         add_column_btn(self)
         self.results["In the Builder section Column has been added"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Column has not been added"] = f"Failed: {e}"

    def add_module(self):
        try:
         add_module(self)
         self.results["In the Builder section Module has been added"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Module has not been added"] = f"Failed: {e}"

    def select_module(self):
        try:
         select_module(self.wait)
         self.results["In the Builder section Module is selected"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Module is not selected"] = f"Failed: {e}"

    def duplicate_row(self):
        try:
          duplicate_row(self)
          self.results["In the Builder Row has been duplicated"] = "Passed"
        except Exception as e:
            self.results["In the Builder Row is not duplicated"] = f"Failed: {e}"

    def delete_row(self):
        try:
          delete_row(self)
          self.results["In the Builder Row has been deleted"] = "Passed"
        except Exception as e:
            self.results["In the Builder Row is not deleted"] = f"Failed: {e}"

    def duplicate_column(self):
        try:
         duplicate_column(self)
         self.results["In the Builder section Column has been duplicated"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Column is not duplicated"] = f"Failed: {e}"

    def delete_column(self):
        try:
         delete_column(self)
         self.results["In the Builder section Column has been deleted"] = "Passed"
        except Exception as e:
         self.results["In the Builder section Column is not deleted"] = f"Failed: {e}"


    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Footer Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Footer Screen are not Saved"] = f"Failed: {e}"

    def write_to_excel(self):
        excel_path = "footer_results.xlsx"  # Path to the Excel file
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Footer_Test Results"
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

#————————————————————————————————————————————————————————————————
class TestFathershopTheme:
    @pytest.fixture(scope='class')
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()

        yield driver
        driver.quit()
#————————————————————————————————————————————————————————————
    def test_footer_functions(self, setup):
        driver = setup

        footer = Footer(driver)
        footer.login()
        footer.write_to_excel()
        footer.navigate_to_footer_screen()
        footer.write_to_excel()
        footer.check_cache_btn()
        footer.write_to_excel()

        footer.duplicate()
        footer.write_to_excel()

        footer.filter_search("Footer")
        footer.write_to_excel()

        footer.create_new_btn()
        footer.write_to_excel()

        footer.footer_name(" Test123")

        footer.color()
        footer.write_to_excel()

        footer.gradient()
        footer.write_to_excel()

        footer.camera()
        footer.write_to_excel()

        footer.add_Margin("10")
        footer.write_to_excel()
        footer.add_Padding("10")
        footer.write_to_excel()
        footer.add_Border("10")
        footer.write_to_excel()
        footer.max_width_btn()
        footer.footer_type()
        footer.add_row_btn()
        footer.duplicate_row()
        footer.add_column_btn()
        footer.delete_column()
        footer.select_module()
        footer.delete_row()
        footer.save()
        footer.edit()
        footer.edit_color()
        footer.edit_gradient()
        footer.save()
        footer.write_to_excel()
        footer.delete()
        footer.write_to_excel()
        footer.click_back_btn()
        footer.write_to_excel()







