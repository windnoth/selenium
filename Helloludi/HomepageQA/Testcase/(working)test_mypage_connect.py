import unittest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import HtmlTestRunner

class mypage(unittest.TestCase):

#크롬, 최대화,로그인페이지로 이동 - 로그인 - 학부모 페이지 이동
    def setUp(self):
        
        global userid
        global userpw
        userid = "@@@" /사용자 ID
        userpw = "@@@" /사용자 PW

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.helloludi.com/member/login.php")
        
        self.driver.implicitly_wait(10)

        textbox_id = self.driver.find_element(By.XPATH, '//*[@id="loginId"]')
        textbox_id.click()
        textbox_id.send_keys(userid)

        textbox_pw = self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]')
        textbox_pw.click()
        textbox_pw.send_keys(userpw)
        
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[1]/div[2]/button').click()


        time.sleep(1.5)
        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[5]').click()

        self.driver.implicitly_wait(10)
        
#학습자 관리 URL 및 Response 200 확인
    def test_001_Index_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[1]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site1 = "https://www.helloludi.com/mypage/index.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site1, response.status_code == 200)

#학습자 리포트 및 학습 설정 URL 및  Response 200 확인
    def test_002_Report_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[2]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site2 = "https://www.helloludi.com/mypage/report.php"

        response = requests.get(get_url)
 
        self.assertTrue(get_url == site2, response.status_code == 200)

#쿠폰 관리 URL 및 Response 200 확인
    def test_003_Coupon_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[3]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site3 = "https://www.helloludi.com/mypage/coupon.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site3, response.status_code == 200)

#구매하기 URL 및 Response 200 확인
    def test_004_Goodslist_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[1]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site4 = "https://www.helloludi.com/goods/goods_list.php?cateCd=004001"

        response = requests.get(get_url)

        self.assertTrue(get_url == site4, response.status_code == 200)

#장바구니 URL 및 Response 200 확인
    def test_005_Cart_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[2]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site5 = "https://www.helloludi.com/order/cart.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site5, response.status_code == 200)

#주문목록/배송조회 URL 및 Response 200 확인
    def test_006_Orderlist_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[3]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site6 = "https://www.helloludi.com/mypage/order_list.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site6, response.status_code == 200)

#취소/반품/교환 내역 URL 및 Response 200 확인
    def test_007_Cancellist_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[4]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        get_url = self.driver.current_url
        site7 = "https://www.helloludi.com/mypage/cancel_list.php"
        
        response = requests.get(get_url)
   
        self.assertTrue(get_url == site7, response.status_code == 200)

#환불/입금 내역 URL 및 Response 200 확인
    def test_008_Refundlist_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[5]/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)
 
        get_url = self.driver.current_url
        site8 = "https://www.helloludi.com/mypage/refund_list.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site8, response.status_code == 200)

#배송지 관리 URL 및 Response 200 확인
    def test_009_Shipping_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[6]/a').click()
       
        self.driver.implicitly_wait(10)
        time.sleep(1.5)

        get_url = self.driver.current_url
        site9 = "https://www.helloludi.com/mypage/shipping.php"

        response = requests.get(get_url)

        self.assertTrue(get_url == site9, response.status_code == 200)

#회원정보 변경 URL 및 Response 200 확인
    def test_010_Shipping_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[4]/ul/li/a').click()

        self.driver.implicitly_wait(10)
        time.sleep(1)

        #카카오 인증 페이지
        get_url1 = self.driver.current_url
        site10 = "https://www.helloludi.com/mypage/my_page_password.php"

        response1 = requests.get(get_url1)
        
        self.driver.implicitly_wait(10)

        if (get_url1 == site10) & (response1.status_code == 200):
            
            self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[2]/div/div/div[3]/button/em').click()
            
            #새로운 창 핸들링
            self.driver.switch_to.window(self.driver.window_handles[1])
                        
            get_url2 = self.driver.current_url
            response2 = requests.get(get_url2)

            self.driver.implicitly_wait(10)

            textbox_id2 = self.driver.find_element(By.XPATH, '//*[@id="loginKey--1"]')
            textbox_id2.click()
            textbox_id2.send_keys("@@@") /카카오톡 ID

            textbox_pw2 = self.driver.find_element(By.XPATH, '//*[@id="password--2"]')
            textbox_pw2.click()
            textbox_pw2.send_keys("@@@") /카카오톡 PW

            login_btn2 = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]')
            login_btn2.click()

            time.sleep(1.5)

            #기존 창 핸들링
            self.driver.switch_to.window(self.driver.window_handles[0])

            if response2.status_code == 200:

                get_url3 = self.driver.current_url
                site10 = "https://www.helloludi.com/mypage/my_page.php"
                
                response3 = requests.get(get_url3)
                
                self.driver.implicitly_wait(10)

                self.assertTure(get_url3 == site10, response3.status_code == 200)
            
            else:
                print("카카오 로그인 프로세스 실패(Fail)2-010_2")
       
        else:
            print("마이페이지에서 회원정보 변경 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail)2-010_1")

#1:1 문의 URL 및 Response 200 확인
    def test_011_Mypageqa_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[1]/a').click()

        self.driver.implicitly_wait(10)     
        time.sleep(1)

        get_url = self.driver.current_url
        site11 = "https://www.helloludi.com/board/list.php?bdId=qa&memNo=194&mypageFl=y&target=_parent&nocategory=y"

        response = requests.get(get_url)

        self.assertTrue (get_url == site11, response.status_code == 200)


#상품 문의 URL 및 Response 200 확인
    def test_012_Mypagegoods_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[2]/a').click()
        self.driver.implicitly_wait(10)        
        time.sleep(1)

        get_url = self.driver.current_url
        site12 = "https://www.helloludi.com/board/list.php?bdId=goodsqa&memNo=194&mypageFl=y&target=_parent&nocategory=y"

        response = requests.get(get_url)

        self.assertTrue (get_url == site12, response.status_code == 200)


#상품 후기 URL 및 Response 200 확인
    def test_013_Mypagegoodsreview_Check_Url(self):
    
        self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[3]/a').click()

        self.driver.implicitly_wait(10)     
        time.sleep(1)

        get_url = self.driver.current_url
        site13 = "https://www.helloludi.com/board/list.php?bdId=goodsreview&memNo=194&mypageFl=y&target=_parent&nocategory=y"

        response = requests.get(get_url)

        self.assertTrue(get_url == site13, response.status_code == 200)
  

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))

##슈트 전용
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(mainpage('test_010_Goods_Pass30_Check_Url'))
    
#     return suite

##슈트 전용
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
