#封装流程受理（申请人情况）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools

class sqrqkPage():
    def __init__(self,driver):
        self.driver = driver

    def sqrqkHandle(self,**qlrParams):
        WebTools(self.driver).mouse_click('link_text', '申请人情况')
        time.sleep(2)

        # 将页面滚动条拖到顶部
        js1 = "var q = document.documentElement.scrollTop=0"
        self.driver.execute_script(js1)
        time.sleep(1)
        ywlxNode = qlrParams.get("ywlxNode")
        qlrmc = qlrParams.get("qlrmc")
        qlrzjhm = qlrParams.get("qlrzjhm")
        qlrdhhm = qlrParams.get("qlrdhhm")
        qlrtxdz = qlrParams.get("qlrtxdz")
        # --========新增权利人========--
        # 首次登记为新增申请人，转移/变更登记为新增权利人,抵押业务为新增抵押权人
        if ywlxNode == 'firstRegister':
            WebTools(self.driver).mouse_click('xpath', "//div[contains(text(),'申请人信息')]/../div[2]/span[1]")
            time.sleep(1)
            # 共有方式
            WebTools(self.driver).choose_droplist_value('GYFS', 'xpath', "//select[@name='GYFS']/option[2]")
        elif ywlxNode == 'changeRegister':
            WebTools(self.driver).mouse_click('xpath', "//div[contains(text(),'权利人列表')]/../div[2]/span[1]")
            time.sleep(1)
            # 共有方式
            WebTools(self.driver).choose_droplist_value('GYFS', 'xpath', "//select[@name='GYFS']/option[2]")
        elif ywlxNode == 'dyRegister':
            WebTools(self.driver).mouse_click('xpath', "//div[contains(text(),'抵押权人列表')]/../div[2]/span[3]")
            time.sleep(1)
            WebTools(self.driver).choose_droplist_value('GYFS', 'xpath', "//select[@name='GYFS']/option[2]")

        # 姓名
        WebTools(self.driver).input_content('xpath',"//input[@xid='SQRMC']",qlrmc)
        # 是否通知
        WebTools(self.driver).mouse_click('name', 'SFTZR')
        # 证件类型
        WebTools(self.driver).choose_droplist_value('SQRZJZL', 'xpath', "//select[@name='SQRZJZL']/option[4]")
        # 证件号码
        WebTools(self.driver).input_content('xpath',"//input[@xid='SQRZJH']",qlrzjhm)
        # 电话
        WebTools(self.driver).input_content('xpath',"//input[@xid='SQRDHHM']",qlrdhhm)
        # 通讯地址
        WebTools(self.driver).input_content('xpath',"//input[@xid='SQRTXDZ']",qlrtxdz)
        # 将页面滚动条拖到顶部
        js1 = "var q = document.documentElement.scrollTop=0"
        self.driver.execute_script(js1)
        time.sleep(1)
        # 保存
        WebTools(self.driver).mouse_click('xpath', "//span[@xid='saveBtn']")
        time.sleep(2)




