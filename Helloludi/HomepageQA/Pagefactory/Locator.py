#테스트 관련 모듈 : 대기
import time

#POM 관련 모듈 : PageFactory
from seleniumpagefactory import PageFactory

#필요 모듈 : Config
import sys
sys.path.append('Config')
from Config_class import Config

class page_locators(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    
    locators = {
        "Main001_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[1]'), # GNB - 로고
        "Main002_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[1]'), #GNB - 헬로루디
        "Main003_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[2]'), #GNB - 커리큘럼
        "Main004_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]'), #GNB - 학습후기
        "Main005_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]'), #GNB - 루디보드
        "Main006_1_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[5]'), #GNB - 학부모페이지
        "Main006_2_box" : ('XPATH', '//*[@id="loginId"]'), # 로그인 화면 - ID 텍스트 박스
        "Main006_3_box" : ('XPATH', '//*[@id="loginPwd"]'), # 로그인 화면 - PW 텍스트 박스
        "Main006_4_btn" : ('XPATH', '//*[@id="formLogin"]/div[1]/div[2]/button'), #로그인 화면 - 로그인 버튼
        "Main007_btn" : ('XPATH', '//*[@id="TopBanner"]/a'), # 상단 굿즈 배너
        "Main008_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[1]/div[1]'), #굿즈 - 365 패스
        "Main009_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[2]/div[1]'), #굿즈 - 300 패스
        "Main010_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[3]/div[1]'), #굿즈 - 30 패스



        "My001_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[1]/a'), #마이페이지 - SNB - 학습자 관리
        "My002_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[2]/a'), #마이페이지 - SNB - 학습 리포트 및 학습 설정
        "My003_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/ul/li[3]/a'), #마이페이지 - SNB - 쿠폰 관리
        "My004_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[1]/a'), #마이페이지 - SNB - 구매하기
        "My005_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[2]/a'), #마이페이지 - SNB - 장바구니
        "My006_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[3]/a'), #마이페이지 - SNB - 주문목록/배송조회
        "My007_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[4]/a'), #마이페이지 - SNB - 취소/반품/교환 내역
        "My008_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[5]/a'), #마이페이지 - SNB - 환불/입금 내역
        "My009_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[2]/ul/li[6]/a'), #마이페이지 - SNB - 배송지 관리
        "My010_1_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div[1]/div/div[1]/div[1]/ul/li[4]/ul/li/a'), #마이페이지 - SNB - 회원 정보 변경
        "My010_2_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[2]/div/div/div[3]/button/em'), #마이페이지 - SNB - 회원 정보 변경 - 인증하기
        "My010_3_box" : ('XPATH', '//*[@id="loginId--1"]'), #마이페이지 - SNB - 회원 정보 변경 - 인증하기 - 카카오창 - ID 텍스트 박스
        "My010_4_box" : ('XPATH', '//*[@id="password--2"]'), #마이페이지 - SNB - 회원 정보 변경 - 인증하기 - 카카오창 - PW 텍스트 박스
        "My010_5_btn" : ('XPATH', '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'), #마이페이지 - SNB - 회원 정보 변경 - 인증하기 - 카카오창 - 로그인
        "My011_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[1]/a'), #마이페이지 - SNB - 1:1 문의
        "My012_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[2]/a'), #마이페이지 - SNB - 상품 문의
        "My013_btn" : ('XPATH', '//*[@id="wrap"]/div[3]/div/div/div/div[1]/div[1]/ul/li[5]/ul/li[3]/a'), #마이페이지 - SNB - 상품 후기



        "Other001_btn" : ('XPATH', '//*[@id="popupCode_layer_3_form"]/div/div[1]/div/a[3]/img'),
        "Other002_btn" : ('XPATH', '//*[@id="footer_wrap"]/div[3]/div[1]/a/img'),
        "Other003_1_btn" : ('XPATH', '//*[@id="footerFixBanner"]'),
        "Other003_2_btn" : ('XPATH', '//*[@id="downloadModal"]/div/div[2]/a[1]'),
        "Other004_btn" : ('XPATH', '//*[@id="downloadModal"]/div/div[2]/a[2]'),
        "Other005_btn" : ('XPATH', '//*[@id="downloadModal"]/div/div[2]/a[3]')
            }

#로그인 이후 마이페이지 접속
    def Mypage_login(self):
        self.Main006_1_btn.click_button()
        
        time.sleep(1.5)

        self.Main006_2_box.set_text(Config.Helloludi_id)
        self.Main006_3_box.set_text(Config.Helloludi_pw)
        self.Main006_4_btn.click_button()
        
        time.sleep(1.5)

        self.Main006_1_btn.click_button()
