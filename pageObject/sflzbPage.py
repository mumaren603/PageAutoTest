#封装流程受理（收费领证表）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools

class sflzbPage():
    def __init__(self,driver):
        self.driver = driver

    def sflzbHandle(self,sfTemplate):
        WebTools(self.driver).mouse_click('link_text', '收费领证表')
        time.sleep(2)

        #将页面滚动条拖到顶部
        js= "var q = document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        time.sleep(1)

        if sfTemplate == 'wx':         #无锡收费是单独一套模板
            WebTools(self.driver).mouse_click('xpath',"//span[@xid='initChargeBtn']")
            #收费明细未配置，alert弹出框处理,新增收费,需处理
        elif sfTemplate == 'tz':
            WebTools(self.driver).choose_droplist_value('jfkm','xpath',"//select[@name='jfkm']/option[2]")

            WebTools(self.driver).mouse_click('xpath',"//span[@xid='addnew']")

            WebTools(self.driver).choose_droplist_value('SFXMLXMC','xpath',"//select[@name='SFXMLXMC']/option[2]")

            WebTools(self.driver).mouse_click('link_text','保存')
        else:
            pass

        #证书生成
        WebTools(self.driver).mouse_click('xpath', "//span[@xid='create']")
        time.sleep(3)
