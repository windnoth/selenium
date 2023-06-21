import unittest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests



class mainpage(unittest.TestCase, unittest.TestResult):
# 크롬, 최대화, 접속
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.helloludi.com")
           
# 메인 페이지에서 로고 클릭 시 URL 이동 및 확인, Status Code 200 비교
    def test_001_Mainpage_Check_Url(self):
                
        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[1]').click()
       
        get_url = self.driver.current_url
        site1 = "https://www.helloludi.com/"

        print("1-001 메인 페이지 로고 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-001 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site1, response.status_code == 200)
        
        except:
            print("메인 페이지에서 로고 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-001)")

#메인 페이지에서 헬로루디 클릭 시 URL 이동 및 확인, Status Code 200 비교
    def test_002_Introduce_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[1]').click()

        get_url = self.driver.current_url
        site2 = "https://www.helloludi.com/main/index.php"

        print("1-002 메인 페이지 헬로루디 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-002 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site2, response.status_code == 200)
        
        except:
            print("메인 페이지에서 헬로루디 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-002)/Fail")


#메인 페이지에서 커리큘럼 클릭 시 URL 이동 및 확인  
    def test_003_Curriculum_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[2]').click()

        get_url = self.driver.current_url
        site3 = "https://www.helloludi.com/main/curriculum.php"

        print("1-003 메인 페이지 커리큘럼 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-003 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site3, response.status_code == 200)
        
        except:
            print("메인 페이지에서 커리큘럼 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-003)/Fail")


#메인 페이지에서 학습후기 클릭 시 URL 이동 및 확인   
    def test_004_Confirmedreview_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]').click()

        get_url = self.driver.current_url
        site4 = "https://www.helloludi.com/board/list.php?bdId=confirmedreview"

        print("1-004 메인 페이지 학습후기 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-004 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site4, response.status_code == 200)
        
        except:
            print("메인 페이지에서 학습후기 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-004)/Fail")

#메인 페이지에서 루디보드 클릭 시 URL 이동 및 확인
    def test_005_Ludiboard_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]').click()

        get_url = self.driver.current_url
        site5 = "https://www.helloludi.com/board/list.php?bdId=confirmedreview"

        print("1-005 메인 페이지 루디보드 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-005 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site5, response.status_code == 200)
        
        except:
            print("메인 페이지에서 커리큘럼 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-005)/Fail")

# 메인 페이지에서 학부모페이지 클릭 후 로그인을 거쳐 다시 한번 클릭 했을 때 URL 확인
    def test_006_Mypage_Check_Url(self):

        self.driver.find_element(By.XPATH, '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[5]').click()
        
        textbox_id = self.driver.find_element(By.XPATH, '//*[@id="loginId"]')
        textbox_id.click()
        textbox_id.send_keys("@@@") #사용자 ID

        textbox_pw = self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]')
        textbox_pw.click()
        textbox_pw.send_keys("@@@") #사용자 PW

        self.driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[1]/div[2]/button').click()

        time.sleep(3)

        get_url = self.driver.current_url
        site6 = "https://www.helloludi.com/mypage/index.php"        
        
        print("1-006 메인 페이지 학부모페이지 클릭 후 로그인을 거쳐 다시 한번 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        response = requests.get(get_url)
        print("1-006 Status code : " + str(response))

        try:
            self.assertTrue(get_url == site6, response.status_code == 200)
            
        except:
            print("메인 페이지 학부모페이지 클릭 후 로그인을 거쳐 다시 한번 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-006)")

#상단 굿즈 배너 이동 및 URL 확인
    def test_007_Goods_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="TopBanner"]/a').click()
        
        get_url = self.driver.current_url
        site7 = "https://www.helloludi.com/goods/goods_list.php?cateCd=004001"
        
        print("1-007 상단 굿즈 배너 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

        goodsmain_response = requests.get(get_url)
        print("1-007 Status code : " + str(goodsmain_response))
        
        time.sleep(2)

        try:
            self.assertTrue(get_url == site7, goodsmain_response.status_code == 200)
        
        except:
            print("상단 굿즈 배너 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-007)")

#굿즈 페이지 패스365 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_008_Goods_Pass365_Check_Url(self):
        
        goods = self.test_007_Goods_Check_Url()

        if goods == None:
            self.driver.get("https://www.helloludi.com/goods/goods_list.php?cateCd=004001")
            self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[1]/div[1]').click()

            print("1-008 패스 365 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

            get_url = self.driver.current_url
            site8 = "https://www.helloludi.com/goods/goods_view.php?goodsNo=1000000000"
            
            pass_365_response = requests.get(get_url)
            print("1-008 Status code : " + str(pass_365_response))

        else:
            goodsmain_response = requests.get(get_url)
            print("1-007 Status code : " + str(goodsmain_response))            
            print("상단 굿즈 배너 클릭 시 지정한 URL 혹은 Status Code가 200이 아니므로 진행 불가(Fail, 1-007)")

        try: 
            self.assertTrue(get_url == site8, pass_365_response.status_code == 200)
                
        except:
            print("패스 365 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(1-008)/Fail") 

#굿즈 페이지 패스300 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_009_Goods_Pass300_Check_Url(self):
        
        goods = self.test_007_Goods_Check_Url()
                
        if goods == None:
            self.driver.get("https://www.helloludi.com/goods/goods_list.php?cateCd=004001")
            self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[2]/div[1]').click()
            
            print("1-009 패스 300 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

            get_url = self.driver.current_url
            site9 = "https://www.helloludi.com/goods/goods_view.php?goodsNo=1000000010"
            
            pass_300_response = requests.get(get_url)
            print("1-009 Status code : " + str(pass_300_response))

        else : 
            goodsmain_response = requests.get(get_url)
            print("1-007 Status code : " + str(goodsmain_response))            
            print("상단 굿즈 배너 클릭 시 지정한 URL 혹은 Status Code가 200이 아니므로 진행 불가(Fail, 1-007)")

        try: 
            self.assertTrue(get_url == site9, pass_300_response.status_code == 200)
                
        except:
            print("패스 300 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-009)") 
        

#굿즈 페이지 패스30 URL 및 확인(사전 조건 : test_Goods_Check_Url(self) = None)
    def test_010_Goods_Pass30_Check_Url(self):
       
        goods = self.test_007_Goods_Check_Url()
        
        if goods == None:
            self.driver.get("https://www.helloludi.com/goods/goods_list.php?cateCd=004001")
            self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[3]/div[1]').click()

            print("1-010 패스 30 클릭으로 지정한 URL 이동 확인 및 Status Code 200 비교 중..")

            get_url = self.driver.current_url
            site10 = "https://www.helloludi.com/goods/goods_view.php?goodsNo=1000000002"
            
            pass_30_response = requests.get(get_url)
            print("1-010 Status code : " + str(pass_30_response))    

        else : 
            goodsmain_response = requests.get(get_url)
            print("1-007 Status code : " + str(goodsmain_response))            
            print("상단 굿즈 배너 클릭 시 지정한 URL 혹은 Status Code가 200이 아니므로 진행 불가(Fail, 1-007)")

        try: 
            self.assertTrue(get_url == site10, pass_30_response.status_code == 200)
                
        except:
            print("패스 30 클릭 시 지정한 URL 혹은 Status Code가 200이 아님(Fail, 1-010)")     

    def tearDown(self):
        self.driver.implicitly_wait(10)
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()



# #슈트 전용
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(mainpage('test_010_Goods_Pass30_Check_Url'))
    
#     return suite

# #슈트 전용
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(suite())