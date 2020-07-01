#封装流程受理（不动产基本信息）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools

class blyjPage():
    def __init__(self,driver):
        self.driver = driver

    def blyjHandle(self):
        WebTools(self.driver).mouse_click('link_text', '办理意见')
        time.sleep(2)
        WebTools(self.driver).input_content('xpath', "//textarea[@xid='currentShyj']",'同意')
