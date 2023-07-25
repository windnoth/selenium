from seleniumpagefactory import PageFactory

class Mainpage_locators(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    locators = {
        "Main001_btn" : ('XPATH', '//*[@id="header_warp"]/div/div[2]/div[1]'), # GNB - 로고
        "Main002_btn" : ('XAPTH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[1]'), #GNB - 헬로루디
        "Main003_btn" : ('XAPTH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[2]'), #GNB - 커리큘럼
        "Main004_btn" : ('XAPTH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]'), #GNB - 학습후기
        "Main005_btn" : ('XAPTH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[3]'), #GNB - 루디보드
        "Main006_1_btn" : ('XAPTH', '//*[@id="header_warp"]/div/div[2]/div[3]/ul/li[5]'), #GNB - 학부모페이지
        "Main006_2_box" : ('XAPTH', '//*[@id="loginId"]'), # 로그인 화면 - ID 텍스트 박스
        "Main006_3_box" : ('XAPTH', '//*[@id="loginPwd"]'), # 로그인 화면 - PW 텍스트 박스
        "Main006_4_btn" : ('XAPTH', '//*[@id="formLogin"]/div[1]/div[2]/button'), #로그인 화면 - 로그인 버튼
        "Main007_btn" : ('XAPTH', '//*[@id="TopBanner"]/a'), # 상단 굿즈 배너
        "Main008_btn" : ('//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[1]/div[1]'), #굿즈 - 365 패스
        "Main009_btn" : ('XAPTH', '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[2]/div[1]'), #굿즈 - 300 패스
        "Main010_btn" : ('XAPTH', '//*[@id="wrap"]/div[3]/div/div/div[2]/div[3]/div/div[1]/ul/li[3]/div[1]'), #굿즈 - 30 패스

    }
