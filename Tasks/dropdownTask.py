import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\chromedriver.exe")
driver.get("https://www.facebook.com/")

txt_user = driver.find_element(By.ID, "email")

driver.execute_script("arguments[0].setAttribute('value','Nisha')",txt_user)

txt_getUser = driver.execute_script("arguments[0].getAttribute('value')",txt_user)

print(str(txt_getUser))

txt_pass = driver.find_element(By.NAME, "pass")

driver.execute_script("arguments[1].setAttribute('value','Nisha@123')",txt_user,txt_pass)

btn_login = driver.find_element(By.NAME, "login")

driver.execute_script("arguments[0].click()",btn_login)