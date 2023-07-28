#테스트 관련 모듈 : 유닛테스트, Status_code, Html 결과 보고서
import unittest
import requests
import HtmlTestRunner

#필요 모듈 : setUp(+tearDown), Pagefactory(Locator), Config
import sys
sys.path.append('Setup')
sys.path.append('Pagefactory')
sys.path.append('Config')

from Setup import setUp
from Locator import page_locators
from Config_class import Othersites
from Config_class import Config



class Otherpage(setUp,page_locators,Othersites,Config):
    
# 메인페이지 3일 무료 체험 바로 시작하기 // 현재 작동 안함

# 메인페이지 3일 무료 체험 자세히 보기
    def test_001_Days3detail_Check_Url(self):
        
        self.Other001_btn.click_button()

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue (get_url == Othersites.Other001_site, response.status_code == 200)


# 플로팅 - 1:1 문의하기(카카오 = 새탭)
    def test_002_kakaoqa_Check_Url(self):
        
        self.Other002_btn.click_button()
        
        self.driver.switch_to.window(self.driver.window_handles[-1])

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue (get_url == Othersites.Other002_site, response.status_code == 200)

#헬로 루디 다운로드 - Android
    def test_003_Download_Android_Check_Url(self):
        
        self.Other003_1_btn.click_button()
        self.Other003_2_btn.click_button()

        self.driver.switch_to.window(self.driver.window_handles[-1])

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue (get_url == Othersites.Other003_site, response.status_code == 200)


#헬로 루디 다운로드 - iOS
    def test_004_Download_iOS_Check_Url(self):
        
        self.Other003_1_btn.click_button()
        self.Other004_btn.click_button()

        self.driver.switch_to.window(self.driver.window_handles[-1])

        get_url = self.driver.current_url
        response = requests.get(get_url)

        self.assertTrue (get_url == Othersites.Other004_site, response.status_code == 200)


#헬로 루디 다운로드 - PC(알럿 출력 되고 텍스트 유효성 검사로 종료)
    def test_005_Download_PC_Check_Alert(self):
       
        self.Other003_1_btn.click_button()
        self.Other005_btn.click_button()
        
        get_alret = self.driver.switch_to.alert
        alret = get_alret.text
        alret_result = "준비중입니다"

        self.assertTrue(alret == alret_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))
