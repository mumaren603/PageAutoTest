'''
复审、审核等簿页面
:param driver  浏览器驱动
:param queryBDCDYH  受理不动产单元号
'''
import time
from Common.CommonFunc import WebTools
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class dbPage():
    def __init__(self,driver):
        self.driver = driver

    def dbHandle(self):
        #登簿
        WebTools(self.driver).mouse_click('link_text', '登簿')
        time.sleep(2)

        #登簿提交
        WebTools(self.driver).mouse_click('xpath',"//div[@id='applicationHost']/div[1]/div[2]/div/section[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[2]")

        #任务流转==>制证
        WebTools(self.driver).mouse_click('xpath',"//span[@xid='span31_1']")

        #等待跳转到办件中心
        try:
            WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located((By.XPATH, "//span[@xid='myTask']")))
        except TimeoutError:
            raise TimeoutError
