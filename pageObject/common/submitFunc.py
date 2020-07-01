'''
提交环节，包括受理，复审，审核等簿环节提交
：param link  流程环节（受理、复审、审核等簿），点击提交后弹出框不一样，通过传入不同参数来确定。
'''

import time
from Common.CommonFunc import WebTools

class submitFunc():
    def __init__(self,driver):
        self.driver = driver

    def submitHandle(self,link):  #环节
        '''
        :param link: 受理环节 包括受理 复审 审核（核定） 登簿
        :return:
        '''
        #提交
        WebTools(self.driver).mouse_click('xpath',"//div[@id='applicationHost']/div[1]/div[2]/div/section[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[2]")
        time.sleep(3)

        if link == 'sl':         #受理提交弹出框
            WebTools(self.driver).mouse_click('xpath',"//span[@xid='span31_1']")
            time.sleep(5)
        elif link == 'fs':      #复审提交弹出框
            WebTools(self.driver).mouse_click('xpath', "//a[@xid='okBtn']")
            time.sleep(3)



