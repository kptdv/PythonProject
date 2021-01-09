import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

class Emp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r"C:\Users\KrishnaPriya\PycharmProjects\SeleniumWIthPython\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://adactinhotelapp.com/index.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print(datetime.now())

    def tearDown(self):
        print(datetime.now())

    def test_login(self):
        txt_username = self.driver.find_element(By.ID, "username")
        txt_username.send_keys("kptdv1990")
        txt_pwd = self.driver.find_element(By.ID, "password")
        txt_pwd.send_keys("Password@123")
        btn_login = self.driver.find_element(By.ID, "login")
        btn_login.click()

unittest.main()