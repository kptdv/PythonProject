import unittest
from datetime import time

from Tasks.commonmethods import Common
from selenium.webdriver.common.by import By

class Emp(unittest.TestCase):
    def setUp(self):
        c = Common()
        driver = c.get_driver_chrome()
        c.url("http://adactinhotelapp.com/")
        time.sleep(5)
        txt_username = driver.find_element(By.ID, "username")
        c.send_values(txt_username, "kptdv1990")
        txt_pwd = driver.find_element(By.ID, "password")
        c.send_values(txt_pwd, "Password@123")
        btn_login = driver.find_element(By.ID, "login")
        c.btn_click(btn_login)
        time.sleep(5)
unittest.main()