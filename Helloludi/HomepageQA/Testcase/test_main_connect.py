#테스트 관련 모듈 : 유닛테스트, 대기, Status_code, Html 결과 보고서
import unittest
import time
import requests
import HtmlTestRunner

#필요 모듈 : setUp(+tearDown), Pagefactory(Locator), Config
import sys
sys.path.append('Setup')
sys.path.append('Pagefactory')
sys.path.append('Config')

from Setup import setUp
from Locator import page_locators
from Config_class import Mainsites
from Config_class import Config

#메인페이지에 대한 URL 및 Status code 비교 Testcase
class Mainpage(setUp,page_locators,Mainsites,Config):
           
# 메인 페이지에서 로고 클릭 시 URL 이동 및 확인, Status Code 200 비교
    def test_001_Mainpage_Check_Url(self):
                
        self.Main001_btn.click_button()
       
        get_url = self.driver.current_url
        response = requests.get(get_url)
        
        self.assertTrue(get_url == Mainsites.Main001_site, response.status_code == 200)

#메인 페이지에서 헬로루디 클릭 시 URL 이동 및 확인, Status Code 200 비교
    def test_002_Introduce_Check_Url(self):

        self.Main002_btn.click_button()
       
        get_url = self.driver.current_url
        response = requests.get(get_url)
        
        self.assertTrue(get_url == Mainsites.Main002_site, response.status_code == 200)

#메인 페이지에서 커리큘럼 클릭 시 URL 이동 및 확인  
    def test_003_Curriculum_Check_Url(self):

        self.Main003_btn.click_button()
       
        get_url = self.driver.current_url
        response = requests.get(get_url)
        
        self.assertTrue(get_url == Mainsites.Main003_site, response.status_code == 200)

#메인 페이지에서 학습후기 클릭 시 URL 이동 및 확인   
    def test_004_Confirmedreview_Check_Url(self):
        
        self.Main004_btn.click_button()
       
        get_url = self.driver.current_url
        response = requests.get(get_url)
        
        self.assertTrue(get_url == Mainsites.Main004_site, response.status_code == 200)

#메인 페이지에서 루디보드 클릭 시 URL 이동 및 확인
    def test_005_Ludiboard_Check_Url(self):

        self.Main005_btn.click_button()
       
        get_url = self.driver.current_url
        response = requests.get(get_url)
        
        self.assertTrue(get_url == Mainsites.Main005_site, response.status_code == 200)

# 메인 페이지에서 학부모페이지 클릭 후 로그인을 거쳐 다시 한번 클릭 했을 때 URL 확인
    def test_006_Mypage_Check_Url(self):

        self.Main006_1_btn.click_button()
        
        #로그인
        self.Main006_2_box.set_text(Config.Helloludi_id)
        self.Main006_3_box.set_text(Config.Helloludi_pw)
        self.Main006_4_btn.click_button()
        
        time.sleep(3)

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mainsites.Main006_site, response.status_code == 200)

#상단 굿즈 배너 이동 및 URL 확인
    def test_007_Goods_Check_Url(self):
        
        self.Main007_btn.click_button()
       
        get_url = self.driver.current_url
        goodsmain_response = requests.get(get_url)

        time.sleep(2)
        
        self.assertTrue(get_url == Mainsites.Main007_site, goodsmain_response.status_code == 200)

#굿즈 페이지 패스365 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_008_Goods_Pass365_Check_Url(self):
        
        goods = self.test_007_Goods_Check_Url()

        if goods == None:
            self.driver.get(Mainsites.Main007_site)
            self.Main008_btn.click_button()

            get_url = self.driver.current_url           
            pass_365_response = requests.get(get_url)

        self.assertTrue(get_url == Mainsites.Main008_site, pass_365_response.status_code == 200)

#굿즈 페이지 패스300 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_009_Goods_Pass300_Check_Url(self):
        
        goods = self.test_007_Goods_Check_Url()
                
        if goods == None:
            self.driver.get(Mainsites.Main007_site)
            self.Main009_btn.click_button()

            get_url = self.driver.current_url
            pass_300_response = requests.get(get_url)

        self.assertTrue(get_url == Mainsites.Main009_site, pass_300_response.status_code == 200)
        
#굿즈 페이지 패스30 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_010_Goods_Pass30_Check_Url(self):
       
        goods = self.test_007_Goods_Check_Url()
        
        if goods == None:
            self.driver.get(Mainsites.Main007_site)
            self.Main010_btn.click_button()

            get_url = self.driver.current_url          
            pass_30_response = requests.get(get_url)

        self.assertTrue(get_url == Mainsites.Main010_site, pass_30_response.status_code == 200)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))
