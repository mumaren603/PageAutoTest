'''
国有建设用地使用权及房屋所有权 -- 首次登记 -- 自建房屋（02102）
'''
import pytest,os
from dataInit.dataInit import dataInit
from pageObject.taskCenter import taskCenter
from pageObject.queryFunc import queryFunc
from pageObject.sjdPage import sjdPage
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
from utils.getTestdata import getTestcaseData,getTestdataPath


class Test_zjfwFirstRegister():
    def setup(self):
        '''初始化用户数据获取'''
        current_file_path = os.path.abspath(__file__).replace('\\','/')
        print("当前测试用例路径是:%s" % current_file_path)
        data = getTestcaseData(getTestdataPath(current_file_path))
        self.qllx = data.get('initdata').get('qllx', None)
        self.djlx = data.get('initdata').get('djlx', None)
        self.ywlx = data.get('initdata').get('ywlx', None)
        self.sfTemplate = data.get('initdata').get('sfTemplate')
        self.params = data.get('initdata').get('params')
        self.qlrParams = {
            "ywlxNode": "firstRegister",
            "qlrmc": generateQLRName(),
            "qlrzjhm": generateCertNum(),
            "qlrdhhm": generateTelnum(),
            "qlrtxdz": generateAddr()
        }



    def test_zjfwFristRegister(self,login):
        '''
        :流程 国有建设用地使用权及房屋所有权--首次登记--自建房屋（02102）
        :param login: 装饰器，登录操作封装，返回信息：(1) webdriver对象（2）数据库配置信息 例如：(<selenium.webdriver.chrome.webdriver.WebDriver (session="f8c32afd6fd5c944984d9aeaadfa9341")>,
         {'dj': '172.0.0.247:1521/tzdj', 'qj': '172.0.0.247:1521/tzkjk'})
        :return:
        '''
        self.driver = login[0]
        dbInfo = login[1]
        # 获取办件数据
        bdcdyh = dataInit(dbInfo).getzjfwFirstRegisterData()
        print("办件受理数据为：%s" % bdcdyh)

        #办件中心
        taskCenter(self.driver).common()
        #选择流程
        taskCenter(self.driver).chooseNode(self.qllx, self.djlx, self.ywlx)
        #发起查询
        queryFunc(self.driver).query(bdcdyh, self.qllx, self.djlx)
        #申请人情况
        sqrqkPage(self.driver).sqrqkHandle(**self.qlrParams)
        #申请表
        sqbPage(self.driver).sqbHandle(self.qllx,self.ywlx,**self.params)
        #不动产基本信息
        bdcjbxxPage(self.driver).bdcjbxxHandle(self.qllx,self.ywlx)
        #收费领证表
        sflzbPage(self.driver).sflzbHandle(self.sfTemplate)
        #办理意见表
        blyjPage(self.driver).blyjHandle()
        #受理提交
        submitFunc(self.driver).submitHandle('sl')
        # #复审环节
        # FsOrShPage(self.driver).FsOrShHandle(bdcdyh)
        # #复审提交
        # submitFunc(self.driver).submitHandle('fs')
        # #等簿环节
        FsOrShPage(self.driver).FsOrShHandle(bdcdyh)
        #等簿提交
        dbPage(self.driver).dbHandle()

        #校验数据库(后期可以把数据库连接串配置化，这样可以针对不同环境校验)
        qlrmc = self.qlrParams.get("qlrmc")
        if qlrmc:
            try:
                resDataCheck = dataResCheck(dbInfo).houseRegisterDataCheck(bdcdyh,qlrmc)
                print("数据库检查结果是：",resDataCheck)
                assert resDataCheck
            except AssertionError:
                raise
    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-v', 'test_zjfwFristRegister'])