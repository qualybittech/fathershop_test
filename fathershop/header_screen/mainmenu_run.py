import pytest
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium_helpers import login,check_cache_btn,no_element_dropdown,create_new_btn,duplicate,delete,filter_search,gradient,camera,save,\
    image_options
from mainmenu_helper import click_main_menu,enter_modulename,mainmenu_name,click_styles_override,item_padding,item_border_radius,text_border,text_padding,min_width_btn,\
    click_dropdown_triangle,add_offset,click_menulabel,enter_menulabel,create_newstyle_btn,click_tab2,enter_stylelabel,text_border_dropdown
from header_helpers import navigate_to_header_screen,Top_menu_addNewItem,topmenu_addstatus,click_hovertab,select_icon,select_size,additional_option1,additional_option2,\
top_menu_edit,edit_select_icon,header_color

class MainMenu:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
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

    def click_main_menu(self):
        try:
            click_main_menu(self.wait)
            self.results["Main Menu Screen is opened"] = "Passed"
        except Exception as e:
            self.results["Main Menu Screen is not opened"] = f"Failed: {e}"

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
            self.results["Clicking on Header duplicate button is successful"] = "Passed"
        except Exception as e:
            self.results["Header duplicate button clicking is not successful"] = f"Failed: {e}"

    def delete(self):
        try:
            delete(self.wait)
            self.results["Clicking on Main Menu delete button is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on Main Menu  delete button is successful"] = f"Failed: {e}"

    def filter_search(self, search_term):
        try:
            filter_search(self.wait, search_term)
            self.results["Main Menu  Search is showing the desired result"] = "Passed"
        except Exception as e:
            self.results["Main Menu  Filter Search is not working"] = f"Failed: {e}"

    def create_new_btn(self):
        try:
            create_new_btn(self.wait)
            self.results["Create New Button is clicked "] = "Passed"
        except Exception as e:
            self.results["Create New Button is not clicked "] = f"Failed: {e}"

    def top_menu_edit(self):
        try:
            top_menu_edit(self.wait)
            self.results["Top menu data is Edited"] = "Passed"
        except Exception as e:
            self.results["Top menu data is not Edited"] = f"Failed: {e}"

    def enter_modulename(self, variable_name):
        try:
            enter_modulename(self.wait, variable_name)
            self.results["Module name is entered"] = "Passed"
        except Exception as e:
            self.results["Module name is not entered"] = f"Failed: {e}"

    def Top_menu_addNewItem(self):
        try:
            Top_menu_addNewItem(self.wait)
            self.results["New Item button is clicked"] = "Passed"
        except Exception as e:
            self.results["New item button is not clicked"] = f"Failed: {e}"

    def mainmenu_name(self, variable_name1, variable_name2):
        try:
            mainmenu_name(self.wait, variable_name1, variable_name2)  # pass self.wait instead of self
            self.results["Item Name & Menu Title are entered"] = "Passed"
        except Exception as e:
            self.results["Item Name & Menu Title are not entered"] = f"Failed: {e}"

    def topmenu_addstatus(self):
        try:
            topmenu_addstatus(self.wait, )  # pass self.wait instead of self
            self.results["Navigating on Status Tabs"] = "Passed"
        except Exception as e:
            self.results["Navigation on Status Tabs are not successful"] = f"Failed: {e}"

    def select_icon(self):
        try:
            select_icon(self.wait)
            self.results["Icon image is uploaded"] = "Passed"
        except Exception as e:
            self.results["Icon image is not uploaded"] = f"Failed: {e}"

    def edit_select_icon(self):
        try:
            edit_select_icon(self.wait)
            self.results["Icon image is edited"] = "Passed"
        except Exception as e:
            self.results["Icon image is not edited"] = f"Failed: {e}"

    def select_size(self, size):
        try:
            select_size(self.wait, size)
            self.results["Icon Size is added"] = "Passed"
        except Exception as e:
            self.results["Icon Size is not added"] = f"Failed: {e}"

    def click_hovertab(self):
        try:
            click_hovertab(self.wait)
            self.results["Icon Hover tab is clicked"] = "Passed"
        except Exception as e:
            self.results["Icon Hover tab is not clicked"] = f"Failed: {e}"

    def additional_option1(self, X, Y):
        try:
            additional_option1(self.wait, X, Y)  # pass self.wait instead of self
            self.results["additional_option1 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option1 values are not entered"] = f"Failed: {e}"

    def additional_option2(self, x, y, z):
        try:
            additional_option2(self.wait, x, y, z)  # pass self.wait instead of self
            self.results["additional_option2 values are entered"] = "Passed"
        except Exception as e:
            self.results["additional_option2 values are not entered"] = f"Failed: {e}"

    def header_color(self):
        try:
            header_color(self.wait)
            self.results["The Icon Color has been selected"] = "Passed"
        except Exception as e:
            self.results["The Icon Color has not been selected"] = f"Failed: {e}"

    def gradient(self):
        try:
         gradient(self.wait)
         self.results["In Item Background Gradient has been selected"] = "Passed"
        except Exception as e:
            self.results["In Item Background Gradient has not been selected"] = f"Failed: {e}"

    def camera(self):
        try:
         camera(self.wait)
         self.results["In Item Background Camera Image has been selected"] = "Passed"
        except Exception as e:
            self.results["In Item Background Camera Image has not been selected"] = f"Failed: {e}"

    def save(self):
        try:
            save(self.wait)
            self.results["All the Changes made in the Top menu Screen has been Saved"] = "Passed"
        except Exception as e:
            self.results["All the Changes made in the Top menu Screen are not Saved"] = f"Failed: {e}"

    def click_styles_override(self):
        try:
            click_styles_override(self.wait)
            self.results["Clicking on styles_override tab is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on styles_override tab button is not successful"] = f"Failed: {e}"


    def  click_dropdown_triangle(self):
        try:
            click_dropdown_triangle(self.wait)
            self.results["Clicking on dropdown triangle tab is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on dropdown triangle tab is not successful"] = f"Failed: {e}"

    def  click_menulabel(self):
        try:
            click_menulabel(self.wait)
            self.results["Clicking on Menu label tab is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on Menu label  tab is not successful"] = f"Failed: {e}"


    def item_padding(self,value):
        try:
            item_padding(self.wait,value)
            self.results["Item padding value is added"] = "Passed"
        except Exception as e:
            self.results["Item padding value is not added"] = f"Failed: {e}"

    def item_border_radius(self,value):
        try:
            item_border_radius(self.wait,value)
            self.results["Item Border Radius value is added"] = "Passed"
        except Exception as e:
            self.results["Item Border Radius  value is not added"] = f"Failed: {e}"

    def text_border(self,value):
        try:
            text_border(self.wait,value)
            self.results["Text Border value is added"] = "Passed"
        except Exception as e:
            self.results["Text Border value is not added"] = f"Failed: {e}"

    def text_border_dropdown(self):
        try:
            text_border_dropdown(self)
            self.results["Text Border dropdown option is selected"] = "Passed"
        except Exception as e:
            self.results["Text Border dropdown option is not selected"] = f"Failed: {e}"

    def text_padding(self,value):
        try:
            text_padding(self.wait,value)
            self.results["Text Padding value is added"] = "Passed"
        except Exception as e:
            self.results["Text Padding value is not added"] = f"Failed: {e}"


    def min_width_btn(self):
        try:
            text_padding(self.wait)
            self.results["Min Width is added"] = "Passed"
        except Exception as e:
            self.results["Min Width is not added"] = f"Failed: {e}"

    def add_offset(self,x_value, y_value):
        try:
            add_offset(self.wait,x_value, y_value)
            self.results["Text Padding value is added"] = "Passed"
        except Exception as e:
            self.results["Text Padding value is not added"] = f"Failed: {e}"

    def enter_menulabel(self, variable_name):
        try:
            enter_menulabel(self.wait, variable_name)
            self.results["Menu label is entered"] = "Passed"
        except Exception as e:
            self.results["Menu label is not entered"] = f"Failed: {e}"

    def  create_newstyle_btn(self):
        try:
            create_newstyle_btn(self.wait)
            self.results["Clicking on Create New Style button is successful"] = "Passed"
        except Exception as e:
            self.results["Clicking on Create New Style button  is not successful"] = f"Failed: {e}"

    def click_tab2(self, tab_name):
        try:
            click_tab2(self.wait, tab_name)
            self.results["Tabs of main menu are opened"] = "Passed"
        except Exception as e:
            self.results["Tabs of main menu are opened"] = f"Failed: {e}"

    def enter_stylelabel(self, variable_name):
        try:
            enter_stylelabel(self.wait, variable_name)
            self.results["Style label is entered"] = "Passed"
        except Exception as e:
            self.results["Style label is not entered"] = f"Failed: {e}"




    def write_to_excel(self):
        excel_path = "main_menu_results.xlsx"  # Path to the Excel file
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
        driver.set_window_size(1380, 1200)  # Set to a reasonable size

        yield driver
        driver.quit()

    def test_MainMEnu_functions(self, setup):
        driver = setup

        main= MainMenu(driver)
        main.login()
        main.navigate_to_header_screen()
        main.write_to_excel()
        main.click_main_menu()
        main.check_cache_btn()
        main.write_to_excel()
        main.duplicate()
        main.filter_search("Def")
        main.write_to_excel()
        main.create_new_btn()
        main.Top_menu_addNewItem()
        main.write_to_excel()
        main.mainmenu_name(" Test1", " Test2")
        main.write_to_excel()
        main.topmenu_addstatus()
        main.select_icon()
        main.header_color()
        main.select_size("20")
        main.write_to_excel()
        main.additional_option1("10", "10")
        main.write_to_excel()
        main.click_tab2("Styles Override")
        main.header_color()
        main.gradient()
        main.write_to_excel()
        main.camera()
        main.item_padding("10")
        main.text_padding("10")
        main.click_dropdown_triangle()
        main.write_to_excel()
        main.add_offset("10","10")
        main.write_to_excel()
        main.click_tab2("Menu Label")
        main.write_to_excel()
        main.enter_menulabel("Menu Test")
        main.write_to_excel()
        main.add_offset("10", "10")
        main.write_to_excel()
        main.save()




