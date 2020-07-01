'封装流程中查询功能'
import time
from Common.CommonFunc import WebTools
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class queryFunc():
    def __init__(self,driver):
        self.driver = driver

    def query(self,bdcdyh,qllx,djlx,*cqType):
        '''
        业务办理查询界面
        :param queryBDCDYH: 查询条件
        :param args: 净地，房屋
        :return:
        '''
        #部分流程查询界面区分净地和房屋
        if cqType:
            if "净地" in cqType:
                WebTools(self.driver).mouse_click('xpath', "//span[@xid='landBtn']")
            elif "房屋" in cqType:
                WebTools(self.driver).mouse_click('xpath', "//span[@xid='houseBtn']")
            else:
                print("入参%s定义错误" %cqType)
        WebTools(self.driver).input_content('xpath',"//input[@xid='bdcdyh']",bdcdyh)
        WebTools(self.driver).mouse_click('xpath',"//div[@xid='mainContent']//span[contains(text(),'查询')]")
        WebTools(self.driver).mouse_click('xpath',"//table[@xid='resultTable']//input[@type='checkbox']")
        WebTools(self.driver).mouse_click('id',"confirmBtn")

        if qllx == "抵押权" and djlx == '转移登记' or(qllx == "抵押权" and djlx == '变更登记'):
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'BeAlert_box')))
                WebTools(self.driver).mouse_click('xpath', "//button[@class='BeAlert_confirm']")
            except Exception as e:
                # self.driver.save_screenshot('D:/python/pageAutoTest/error111222.jpg')
                raise  NoAlertPresentException
        else:
            pass

        time.sleep(12)








