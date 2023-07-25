#테스트 관련 모듈 : 유닛테스트, 웹 드라이버
import unittest
from selenium import webdriver

class setUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.helloludi.com")
    
    def tearDown(self):
        self.driver.quit()
