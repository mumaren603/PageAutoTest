#封装流程受理（不动产基本信息）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools

class bdcjbxxPage():
    def __init__(self,driver):
        self.driver = driver

    def bdcjbxxHandle(self,ywlx):
        WebTools(self.driver).mouse_click('link_text', '不动产基本信息')
        time.sleep(2)

        # if ywlx != '自建房屋（02102）' and ywlx != '建筑物区分业主共有部分（02103）':
        #     #房屋  交易价格 必填项
        #     WebTools(self.driver).input_content('xpath',"//input[@xid='QDJG']",'90')



