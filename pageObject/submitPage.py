import time
from Common.CommonFunc import WebTools
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class submitFunc():
    def __init__(self,dirver):
        self.driver = dirver

    def slHandle(self):
        '''
        :param link: 受理环节 包括受理 复审 审核（核定） 登簿
        :return:
        '''
        # 提交
        WebTools(self.driver).mouse_click('xpath',"//div[@id='applicationHost']/div[1]/div[2]/div/section[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[2]")
        time.sleep(3)

        # 受理环节弹出框确定按钮
        WebTools(self.driver).mouse_click('xpath', "//span[@xid='span31_1']")
        time.sleep(5)

    def shHandle(self,bdcdyh,env,shCount):
        '''
        审核环节 不同环境同个流程审核环节不一致 ，需要特殊处理 。
        :param bdcdyh: 不动产单元号
        :param env:  环境
        :param shCount: 审核次数
        :return:
        '''

        for i in shCount:
            if i == env:
                count = shCount.get(env)
                print("count次数是",count)

        for i in range(count):
            # 进入流程
            WebTools(self.driver).mouse_doubleClick('xpath',"//div[contains(text(),'"+bdcdyh+"')]/../..")
            time.sleep(2)

            # 填写复审/审核等簿意见
            WebTools(self.driver).input_content('xpath',"//textarea[@xid='currentShyj']",'同意')

            # 提交
            WebTools(self.driver).mouse_click('xpath',"//div[@id='applicationHost']/div[1]/div[2]/div/section[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[2]")
            time.sleep(3)

            # 非受理环节弹出框确定按钮
            WebTools(self.driver).mouse_click('xpath', "//a[@xid='okBtn']")
            time.sleep(3)

    def dbHandle(self,bdcdyh):
        WebTools(self.driver).mouse_doubleClick('xpath',"//div[contains(text(),'"+bdcdyh+"')]/../..")
        time.sleep(2)

        #等簿意见
        WebTools(self.driver).input_content('xpath',"//textarea[@xid='currentShyj']",'同意')

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
