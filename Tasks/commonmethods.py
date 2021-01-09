import keyboard
import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class Common:
    def read_data(self,row_no,col_no,sheet_name):
        excel_loc = r"C:\Users\KrishnaPriya\Desktop\Selenium\HotelBookingTestData.xlsx"
        workbook=openpyxl.load_workbook(excel_loc)
        sheet=workbook[sheet_name]
        data=sheet.cell(row_no,col_no).value
        return data

    def get_driver_chrome(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\chromedriver.exe")
        self.driver.maximize_window()
        return self.driver

    def get_driver_firefox(self):
        self.driver_firefox= webdriver.Firefox(
            executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\geckodriver.exe")
        self.driver_firefox.maximize_window()
        return self.driver_firefox

    def get_driver_IE(self):
        self.driver_firefox = webdriver.Firefox(
            executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\IEDriverServer.exe")
        self.driver_firefox.maximize_window()
        return self.driver_firefox

    def url(self,url):
        self.driver.get(url)

    def send_values(self,element,value):
        element.send_keys(value)

    def btn_click(self,element):
        element.click()

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def getattribute(self,element,attributename):
        attribute=element.get_attribute(attributename)
        return attribute

    def mousehover(self,element):
        acc=ActionChains(self.driver)
        acc.move_to_element(element).perform()

    def draganddrop(self,source,destination):
        acc = ActionChains(self.driver)
        acc.drag_and_drop(source,destination).perform()

    def rightclick(self,element):
        acc = ActionChains(self.driver)
        acc.context_click(element).perform()

    def doubleclick(self,element):
        acc = ActionChains(self.driver)
        acc.double_click(element).perform()

    def keyboard_downarrow(self):
        keyboard.press("down arrow")
        keyboard.release("down arrow")

    def keyboard_enter(self):
        keyboard.press("enter")
        keyboard.release("enter")

    def alert_OK(self):
        element=self.driver.switch_to.alert
        element.accept()

    def alert_Cancel(self):
        element = self.driver.switch_to.alert
        element.dismiss()

    def switchtoframe(self,element):
        self.driver.switch_to.frame(element)

    def switchtoframebyindex(self,index):
        self.driver.switch_to.frame(index)

    def switchtoframebyname(self,name):
        self.driver.switch_to.frame(name)

    def switchto_mainwindow(self):
        self.driver.switch_to.default_content()

    def switchto_parentframe(self):
        self.driver.switch_to.parent_frame()

    def dropdown_selectbyvalue(self,element,value):
        varA=Select(element)
        varA.select_by_value(value)

    def dropdown_selecbytext(self,element,text):
        varA = Select(element)
        varA.select_by_visible_text(text)

    def dropdown_selectbyindex(self,element,index):
        varA = Select(element)
        varA.select_by_index(index)

    def dropdown_firstselect(self,element):
        varA = Select(element)
        varA.first_selected_option()

    def dropdown_selectall(self,element):
        varA=Select(element)
        varA.all_selected_options()

    def dropdown_deselectbyvalue(self,element,value):
        varA=Select(element)
        varA.deselect_by_value(value)

    def dropdown_deselecbytext(self,element,text):
        varA = Select(element)
        varA.deselect_by_visible_text(text)

    def dropdown_deselectbyindex(self,element,index):
        varA = Select(element)
        varA.deselect_by_index(index)

    def dropdown_deselectall(self,element):
        varA = Select(element)
        varA.deselect_all()

    def parent_windowid(self):
        element=self.driver.current_window_handle
        print(element)

    def getallwindowid(self):
        element=self.driver.window_handles
        print(element)

    def switch2_child_window(self,windowno):
        element = self.driver.window_handles
        childwindow=element[windowno]
        self.driver.switch_to.window(childwindow)

    def switch2_parent_window(self):
        element = self.driver.current_window_handle
        self.driver.switch_to.window(element)

    def screenshot(self,location):
        self.driver.save_screenshot(location)
