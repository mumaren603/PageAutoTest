'''
复审、审核等簿页面
:param driver  浏览器驱动
:param queryBDCDYH  受理不动产单元号
'''
import time
from Common.CommonFunc import WebTools

class FsOrShPage():
    def __init__(self,driver):
        self.driver = driver

    def FsOrShHandle(self,bdcdyh):
        WebTools(self.driver).mouse_doubleClick('xpath',"//div[contains(text(),'"+bdcdyh+"')]/../..")
        time.sleep(2)

        #复审/审核等簿意见
        WebTools(self.driver).input_content('xpath',"//textarea[@xid='currentShyj']",'同意')


