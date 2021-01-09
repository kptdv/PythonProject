import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\chromedriver.exe")
driver.get("https://www.snapdeal.com/")
driver.maximize_window()
time.sleep(10)
hover_text=driver.find_element(By.XPATH,"//span[text()='Mobile & Tablets']")
acc=ActionChains(driver)
acc.move_to_element(hover_text).perform()

click_text=driver.find_element(By.XPATH,"//span[text()='New Launches Covers']")
click_text.click()


#driver.quit()
