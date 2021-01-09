import time
import keyboard as keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome(executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\chromedriver.exe")
driver.get("http://output.jsbin.com/osebed/2")
driver.maximize_window()

fruit = driver.find_element(By.ID, "fruits")

s=Select(fruit)

#fetch all option
op = s.options

#select  all value  by index
for  i in range(0,len(op)):
    s.select_by_index(i)

#de select value
s.deselect_by_index(0)

s.deselect_by_value("orange")

#fetch only selected option
p = s.all_selected_options
l=type(p)
print(l)

for i in p:
    print(i)
    t = i.text
    print(t)
