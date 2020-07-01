'''
查封登记（包括轮候查封）（净地）
'''
import unittest,time
from selenium import webdriver
from dataInit.dataInit import dataInit
from pageObject.login import login
from pageObject.taskCenter import taskCenter
from pageObject.queryFunc import queryFunc
from pageObject.sjdPage import sjdPage
from init.userInfoInit import generateCfwj
from pageObject.sqbPage import sqbPage
from pageObject.blyjPage import blyjPage
from pageObject.common.submitFunc import submitFunc
from pageObject.common.FsOrShPage import FsOrShPage
from pageObject.common.dbPage import dbPage
from testResDataCheck.seizureRegisterDataCheck import seizureRegisterDataCheck

chrome_driver = r"D:\python\testPage\chromeDriver\chromedriver.exe"
testLoginURL='http://192.168.1.3:8080'

class testLandMortgageRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=chrome_driver)

    def test_landFristRegister(self):
        # 参数
        qllx = "查封登记"
        djlx = ""
        ywlx = "查封登记（包括轮候查封）（05001）"
        params = {"fwlb": "商品房","ywxl":"查封登记"}  # dict
        cqType = "净地"
        #获取查询数据
        try:
            queryBDCDYH = dataInit().getLandSeizureRegisterData()
            print("queryRes:",queryBDCDYH)
        except ValueError as e:
            print(e)

        #浏览器操作
        login(self.driver).setBrowser(testLoginURL)
        #登录
        login(self.driver).userLogin()
        #办件中心
        taskCenter(self.driver).common()
        #选择流程
        taskCenter(self.driver).chooseNode(qllx,djlx,ywlx)
        #发起查询
        queryFunc(self.driver).query(queryBDCDYH,qllx,djlx,cqType)
        #收件单
        sjdPage(self.driver).sjdHandle(qllx,queryBDCDYH,**params)
        #申请表
        cfwj=generateCfwj() #查封文件
        sqbPage(self.driver).sqbHandle(qllx,cfwj)
        #受理意见表
        blyjPage(self.driver).blyjHandle()
        #受理提交
        submitFunc(self.driver).submitHandle('sl')
        #等簿环节
        FsOrShPage(self.driver).FsOrShHandle(queryBDCDYH)
        #等簿提交
        dbPage(self.driver).dbHandle()

        #校验数据库(后期可以把数据库连接串配置化，这样可以针对不同环境校验)
        # try:
        #     resDataCheck = seizureRegisterDataCheck().dataCheck(queryBDCDYH,cfwj)
        #     print("数据库检查结果是：",resDataCheck)
        #     self.assertTrue(resDataCheck)
        # except AssertionError as e:
        #     print(e)
        #     raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()