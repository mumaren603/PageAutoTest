#封装流程受理（收费领证表）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools

class sflzbPage():
    def __init__(self,driver):
        self.driver = driver

    def sflzbHandle(self,env):
        '''
        说明：无锡收费为一套模板，宜兴泰州为一套模板，宿迁一套模板（不收费）
        :param sfTemplate: 收费模板
        :return:
        '''

        # 收费信息
        if env == 'sqtest':
            WebTools(self.driver).mouse_click('link_text', '不动产证信息')
            time.sleep(2)
        else:
            # 将页面滚动条拖到顶部
            js = "var q = document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            WebTools(self.driver).mouse_click('link_text', '收费领证表')
            time.sleep(2)
            if env == 'wxtest':
                WebTools(self.driver).mouse_click('xpath', "//span[@xid='initChargeBtn']")
                # 收费明细未配置，alert弹出框处理,新增收费,需处理
            elif env == 'tztest' or env =='yxtest':
                WebTools(self.driver).choose_droplist_value('jfkm', 'xpath', "//select[@name='jfkm']/option[2]")
                WebTools(self.driver).mouse_click('xpath', "//span[@xid='addnew']")
                WebTools(self.driver).choose_droplist_value('SFXMLXMC', 'xpath', "//select[@name='SFXMLXMC']/option[2]")
                WebTools(self.driver).mouse_click('link_text', '保存')
            else:
                pass

        # 证书生成
        WebTools(self.driver).mouse_click('xpath', "//span[@xid='create']")
        time.sleep(3)




