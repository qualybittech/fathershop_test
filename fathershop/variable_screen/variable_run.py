import pytest
from selenium.webdriver.common.alert import Alert
from openpyxl import Workbook
from openpyxl.styles import Alignment
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from constants import USERNAME, PASSWORD, LOGIN_URL
from selenium_helpers import login, check_cache_btn, create_new_btn, duplicate, delete, filter_search, edit,save, no_element_dropdown,add_breakpoint_btn
from variable_helper import navigate_to_variable_screen,new_breakpoint,edit_breakpoint, select_Colours, new_colors,edit_colors, selectFontFamily, new_font, edit_font,select_size ,new_fontsize,\
edit_fontsize,select_spacing,new_spacing,edit_spacing,select_radius , new_radius, edit_radius,select_gradient,new_gradient,edit_gradient,select_shadow,new_shadow,edit_shadow, select_items, new_items


class Variables:

    def __init__(self, driver):  # def __init__(self, driver, excel_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.results = {}

    def login(self):
        login(self.wait, self.driver, USERNAME, PASSWORD)
    def navigate_to_variable_screen(self):
        navigate_to_variable_screen(self)


    def check_cache_btn(self):
        check_cache_btn(self.wait)

    def filter_search(self, search_term):
        filter_search(self.wait, search_term)

    def create_new_btn(self):
        create_new_btn(self.wait)

    def new_breakpoint(self, variable_name, variable_value):
        new_breakpoint(self.wait, variable_name, variable_value)

    def save(self):
        save(self.wait)


    def edit(self):
        edit(self.wait)

    def edit_breakpoint(self, new_value):
        edit_breakpoint(self.wait, new_value)


class Colors:
    def __init__(self, wait):
        self.wait = wait
    def select_Colours(self):
        select_Colours(self.wait)

    def no_element_dropdown(self):
        no_element_dropdown(self.wait)

    def new_colors(self, variable_name):
        new_colors(self.wait, variable_name)

    def edit_colors(self):
        edit_colors(self.wait)

    def write_to_excel(self):
        excel_path = "topmenu_results.xlsx"  # Path to the Excel file
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Topmenu_Test Results"
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

class FontFamily:
    def __init__(self, wait):
        self.wait = wait
    def selectFontFamily(self):
        selectFontFamily(self.wait)

    def new_font(self, variable_name):
        new_font(self.wait, variable_name)
    def edit_font(self):
        edit_font(self.wait)


def write_to_excel(self):
    excel_path = "topmenu_results.xlsx"  # Path to the Excel file
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Topmenu_Test Results"
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
class FontSize:
    def __init__(self, wait):
        self.wait = wait

    def select_size(self):
        select_size(self.wait)

    def new_fontsize(self, variable_name, variable_value):
        new_fontsize(self.wait, variable_name, variable_value)

    def edit_fontsize(self, variable_value):
        edit_fontsize(self.wait, variable_value)
class Spacing:
    def __init__(self, wait):
        self.wait = wait

    def select_spacing(self):
        select_spacing(self.wait)

    def new_spacing(self, variable_name, variable_value):
        new_spacing(self.wait, variable_name, variable_value)

    def edit_spacing(self, variable_value):
        edit_spacing(self.wait, variable_value)


class Radius:
    def __init__(self, wait):
        self.wait = wait

    def select_radius(self):
        select_radius(self.wait)

    def new_radius(self, variable_name, variable_value):
        new_radius(self.wait, variable_name, variable_value)

    def edit_radius(self, variable_value):
        edit_radius(self.wait, variable_value)

class Gradient:
    def __init__(self, wait):
        self.wait = wait

    def select_gradient(self):
        select_gradient(self.wait)

    def new_gradient(self, variable_name):
        new_gradient(self.wait, variable_name)

    #def edit_gradient(self):
        #edit_gradient(self.wait)

class Shadow:
    def __init__(self, wait):
        self.wait = wait

    def select_shadow(self):
        select_shadow(self.wait)

    def new_shadow(self, variable_name, variable_value):
        new_shadow(self.wait, variable_name, variable_value)

    def edit_shadow(self):
        edit_shadow(self.wait)

class ItemsPerRow:
    def __init__(self, wait):
        self.wait = wait

    def select_items(self):
         select_items(self.wait)

    def duplicate(self):
         duplicate(self.wait)
    def delete(self):
        delete(self.wait)

    def new_items(self, variable_name):
        new_items(self.wait, variable_name)

    def breakpoint(self):
        breakpoint(self.wait)


    #def edit_items(self):
        #edit_items(self.wait)
class TestFathershopTheme:
    @pytest.fixture
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_styles_functions(self, setup):
        driver = setup
        variable = Variables(driver)
        variable.login()
        variable.navigate_to_variable_screen()

        # ———————————————————————————-
        variable.check_cache_btn()
        variable.filter_search("Test")
        variable.create_new_btn()
        variable.new_breakpoint(" Tests", "10")
        variable.save()
        #variable.edit()
        #variable.edit_breakpoint("2")
        #variable.save()
        # --------------------------------------------------------------
        color = Colors(variable.wait)
        color.select_Colours()
        color.no_element_dropdown()
        variable.filter_search("Action")
        variable.create_new_btn()
        color.new_colors(" Test")
        variable.save()
        #variable.edit()
        #color.edit_colors()
        variable.save()

        # --------------------------------------------------------------

        font = FontFamily(variable.wait)
        font.selectFontFamily()
        variable.filter_search("Def")
        variable.create_new_btn()
        font.new_font("Test")
        variable.save()
        variable.edit()
        font.edit_font()
        variable.save()
        # --------------------------------------------------------------

        size = FontSize(variable.wait)
        size.select_size()
        variable.filter_search("Def")
        variable.create_new_btn()
        size.new_fontsize(" Test", "1")
        variable.save()
        variable.edit()
        size.edit_fontsize("2")
        variable.save()
        # ----------------------------------------------------------------
        spacing = Spacing(variable.wait)
        spacing.select_spacing()
        variable.filter_search("Def")
        variable.create_new_btn()
        spacing.new_spacing(" Test", "1")
        variable.save()
        variable.edit()
        spacing.edit_spacing("3")
        variable.save()

        # ----------------------------------------------------------------
        radius = Radius(variable.wait)
        radius.select_radius()
        variable.filter_search("Small")
        variable.create_new_btn()
        radius.new_radius(" Test", "1")
        variable.save()
        variable.edit()
        radius.edit_radius("3")
        variable.save()

        # -----------------------------------------------------------------

        gradient = Gradient(variable.wait)
        gradient.select_gradient()
        # variable.filter_search("Over")
        variable.create_new_btn()
        gradient.new_gradient(" Test", )
        variable.save()
        # variable.edit()
        # gradient.edit_gradient("s")
        # variable.save()
        # ————————————————————————————————


#_________________________________________________________________________________________
        shadow = Shadow(variable.wait)
        shadow.select_shadow()
        variable.filter_search("Lar")
        variable.create_new_btn()
        shadow.new_shadow(" Test", "1")
        variable.save()
        variable.edit()
        shadow.edit_shadow()
        variable.save()


#------------------------------------------------------------------
        items_row = ItemsPerRow(variable.wait)
        items_row.select_items()
        variable.filter_search("Testi")
        variable.create_new_btn()
        items_row.new_items(" Test")
        variable.save()
        items_row.duplicate()
        items_row.delete()









