import unittest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import HtmlTestRunner


class otherpage(unittest.TestCase):
# 크롬, 최대화, 접속
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.helloludi.com")
        self.driver.implicitly_wait(10)

# 메인페이지 3일 무료 체험 바로 시작하기 // 현재 작동 안함

# 메인페이지 3일 무료 체험 자세히 보기
    def test_001_Days3detail_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="popupCode_layer_3_form"]/div/div[1]/div/a[3]/img').click()        
        self.driver.implicitly_wait(10)

        get_url = self.driver.current_url
        site1 = "https://www.helloludi.com/board/view.php?&bdId=notice&sno=15"

        response = requests.get(site1)

        self.assertTrue (get_url == site1, response.status_code == 200)


# 플로팅 - 1:1 문의하기(카카오 = 새탭)
    def test_002_kakaoqa_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="footer_wrap"]/div[3]/div[1]/a/img').click()
        self.driver.implicitly_wait(10)

        self.driver.switch_to.window(self.driver.window_handles[-1])

        get_url = self.driver.current_url
        site2 = "https://pf.kakao.com/_xcAqxms"

        response = requests.get(site2)

        self.assertTrue (get_url == site2, response.status_code == 200)

#헬로 루디 다운로드 - Android
    def test_003_Download_Android_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="footerFixBanner"]').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH, '//*[@id="downloadModal"]/div/div[2]/a[1]').click()
        self.driver.implicitly_wait(10)        

        self.driver.switch_to.window(self.driver.window_handles[-1])
        get_url = self.driver.current_url
        site3 = "https://play.google.com/store/apps/details?id=com.archipin.helloludi"

        response = requests.get(get_url)

        self.assertTrue(get_url == site3, response.status_code == 200)


#헬로 루디 다운로드 - iOS
    def test_004_Download_iOS_Check_Url(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="footerFixBanner"]').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH, '//*[@id="downloadModal"]/div/div[2]/a[2]').click()
        self.driver.implicitly_wait(10)        

        self.driver.switch_to.window(self.driver.window_handles[-1])
        get_url = self.driver.current_url
        site4 = "https://apps.apple.com/kr/app/%ED%97%AC%EB%A1%9C%EB%A3%A8%EB%94%94/id1662411884"

        response = requests.get(get_url)

        self.assertTrue (get_url == site4, response.status_code == 200)


#헬로 루디 다운로드 - PC(알럿 출력 되고 텍스트 유효성 검사로 종료)
    def test_005_Download_PC_Check_Alert(self):
       
        self.driver.find_element(By.XPATH, '//*[@id="footerFixBanner"]').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH, '//*[@id="downloadModal"]/div/div[2]/a[3]').click()
        
        #time.sleep(3)   

        get_alret = self.driver.switch_to.alert
        alret = get_alret.text
        alret_result = "준비중입니다"

        self.assertTrue(alret == alret_result)


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
