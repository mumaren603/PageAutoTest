'''
国有建设用地使用权及房屋所有权 -- 首次登记 -- 商品房、征地拆迁安置房、经适房、房改售房（02101）
'''
import unittest
from selenium import webdriver
from dataInit.dataInit import dataInit
from pageObject.login import login
from pageObject.taskCenter import taskCenter
from pageObject.queryFunc import queryFunc
from pageObject.sqrqkPage import sqrqkPage
from init.userInfoInit import generateAddr,generateCertNum,generateQLRName,generateTelnum
from pageObject.sqbPage import sqbPage
from pageObject.bdcjbxxPage import bdcjbxxPage
from pageObject.sflzbPage import sflzbPage
from pageObject.blyjPage import blyjPage
from pageObject.common.submitFunc import submitFunc
from pageObject.common.FsOrShPage import FsOrShPage
from pageObject.common.dbPage import dbPage
from dataCheck.dataResCheck import dataResCheck

chrome_driver = r"D:\python\testPage\chromeDriver\chromedriver.exe"
testLoginURL='http://192.168.1.3:8080'

class test_spfFirstRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=chrome_driver)

    def test_spfFristRegister(self):
        #参数
        qllx="国有建设用地使用权及房屋所有权"
        djlx="首次登记"
        ywlx="自建房屋（02102）"
        qlrParams = {"ywlxNode":"firstRegister","qlrmc":generateQLRName(),"qlrzjhm":generateCertNum(),"qlrdhhm":generateTelnum(),"qlrtxdz":generateAddr()}
        sfTemplate = "tz"   #收费模板 目前支持泰州、无锡模板

        #获取查询数据
        try:
            bdcdyh = dataInit().getSpfFirstRegisterData()
            print("queryRes:",bdcdyh)
        except ValueError as e:
            print(e)

        #浏览器操作
        login(self.driver).setBrowser(testLoginURL)
        #登录
        login(self.driver).userLogin()
        #办件中心
        taskCenter(self.driver).common()
        #选择流程
        taskCenter(self.driver).chooseNode(qllx, djlx, ywlx)
        #发起查询
        queryFunc(self.driver).query(bdcdyh, qllx, djlx)
        #申请人情况
        sqrqkPage(self.driver).sqrqkHandle(**qlrParams)
        #申请表
        sqbPage(self.driver).sqbHandle(qllx,ywlx)
        #不动产基本信息
        bdcjbxxPage(self.driver).bdcjbxxHandle(qllx,ywlx)
        #收费领证表
        sflzbPage(self.driver).sflzbHandle(sfTemplate)
        #办理意见表
        blyjPage(self.driver).blyjHandle()
        #受理提交
        submitFunc(self.driver).submitHandle('sl')
        #等簿环节
        FsOrShPage(self.driver).FsOrShHandle(bdcdyh)
        #等簿提交
        dbPage(self.driver).dbHandle()

        #校验数据库(后期可以把数据库连接串配置化，这样可以针对不同环境校验)
        qlrmc = qlrParams.get("qlrmc")
        if qlrmc:
            try:
                resDataCheck = dataResCheck().houseRegisterDataCheck(self.bdcdyh, qlrmc)
                print("数据库检查结果是：",resDataCheck)
                self.assertTrue(resDataCheck)
            except AssertionError as e:
                print(e)
                raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()