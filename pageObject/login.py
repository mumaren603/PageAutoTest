#Author: ls Liu
'''
封装登录模块
'''
import time
from selenium.webdriver.support.ui import WebDriverWait
from Common.CommonFunc import WebTools

chrome_driver = r"D:\python\testPage\chromeDriver\chromedriver.exe"
testLoginURL='http://192.168.1.3:8080'



class login():
    def __init__(self,driver):
        self.driver = driver

    def setBrowser(self,testUrl):
        WebTools(self.driver).set_browser(testUrl)

    def userLogin(self):
        WebTools(self.driver).input_clear('xpath',"//input[contains(@id,'_name')]")
        WebTools(self.driver).input_clear('xpath', "//input[contains(@id,'_password')]")
        WebTools(self.driver).input_content('xpath',"//input[contains(@id,'_name')]",'zcy')
        WebTools(self.driver).input_content('xpath', "//input[contains(@id,'_password')]", '123456')
        WebTools(self.driver).mouse_click('xpath',"//div[contains(@id,'_btnlogin')]")
        time.sleep(3)
        #进入首页判断是否超时
        try:
            element = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath("//div[contains(text(),'办件中心')]"))
        except:
            print("NoSuchElementException")
