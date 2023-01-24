import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)

        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")