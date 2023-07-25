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
from Config_class import Mysites
from Config_class import Config


class Mypage(setUp,page_locators,Mysites,Config):
      
#학습자 관리 URL 및 Response 200 확인
    def test_001_Index_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My001_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My001_site, response.status_code == 200)

#학습자 리포트 및 학습 설정 URL 및  Response 200 확인
    def test_002_Report_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My002_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My002_site, response.status_code == 200)

#쿠폰 관리 URL 및 Response 200 확인
    def test_003_Coupon_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My003_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My003_site, response.status_code == 200)

#구매하기 URL 및 Response 200 확인
    def test_004_Goodslist_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My004_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My004_site, response.status_code == 200)

#장바구니 URL 및 Response 200 확인
    def test_005_Cart_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My005_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My005_site, response.status_code == 200)

#주문목록/배송조회 URL 및 Response 200 확인
    def test_006_Orderlist_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My006_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My006_site, response.status_code == 200)

#취소/반품/교환 내역 URL 및 Response 200 확인
    def test_007_Cancellist_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My007_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My007_site, response.status_code == 200)

#환불/입금 내역 URL 및 Response 200 확인
    def test_008_Refundlist_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My008_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My008_site, response.status_code == 200)

#배송지 관리 URL 및 Response 200 확인
    def test_009_Shipping_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My009_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My009_site, response.status_code == 200)

#회원정보 변경 URL 및 Response 200 확인
    def test_010_Shipping_Check_Url(self):
        
        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My010_1_btn.click_button()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        #카카오 인증 페이지
        get_url1 = self.driver.current_url
        response1 = requests.get(get_url1)
        
        self.driver.implicitly_wait(10)

        if (get_url1 == Mysites.My010_1_site) & (response1.status_code == 200):
            
            self.My010_2_btn.click_button()
            
            #새로운 창 핸들링
            time.sleep(1.5)
                        
            self.driver.switch_to.window(self.driver.window_handles[1])
                        
            get_url2 = self.driver.current_url
            response2 = requests.get(get_url2)

            self.driver.implicitly_wait(10)

            self.My010_3_box.set_text(Config.kakao_id)
            self.My010_4_box.set_text(Config.kakao_pw)
            self.My010_5_btn.click_button()

            time.sleep(1.5)

            #기존 창 핸들링
            self.driver.switch_to.window(self.driver.window_handles[0])

            if response2.status_code == 200:

                get_url3 = self.driver.current_url
                response3 = requests.get(get_url3)
                
                self.driver.implicitly_wait(10)

                self.assertTrue(get_url3 == Mysites.My010_2_site, response3.status_code == 200)
            
            else:
                print("카카오 로그인 프로세스 실패(Fail)2-010_2")
       
        else:
            print("마이페이지에서 회원정보 변경 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail)2-010_1")

#1:1 문의 URL 및 Response 200 확인
    def test_011_Mypageqa_Check_Url(self):

        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My011_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My011_site, response.status_code == 200)


#상품 문의 URL 및 Response 200 확인
    def test_012_Mypagegoods_Check_Url(self):
        
        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My012_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My012_site, response.status_code == 200)


#상품 후기 URL 및 Response 200 확인
    def test_013_Mypagegoodsreview_Check_Url(self):
    
        Mylogin = page_locators(self.driver)
        Mylogin.Mypage_login()

        self.My013_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue(get_url == Mysites.My013_site, response.status_code == 200)
  

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))
