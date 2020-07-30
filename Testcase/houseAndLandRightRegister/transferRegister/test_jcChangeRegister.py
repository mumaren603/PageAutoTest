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
from dataCheck.dataResCheck import dataResCheck
from utils.getTestdata import getTestcaseData,getTestdataPath
from pageObject.submitPage import submitPage

class Test_jcChangeRegister():
    def setup(self):
        '''初始化用户数据获取'''
        current_file_path = os.path.abspath(__file__).replace('\\', '/')
        print("当前测试用例路径是:%s" % current_file_path)
        data = getTestcaseData(getTestdataPath(current_file_path))
        self.qllx = data.get('initdata').get('qllx', None)
        self.djlx = data.get('initdata').get('djlx', None)
        self.ywlx = data.get('initdata').get('ywlx', None)
        self.sfTemplate = data.get('initdata').get('sfTemplate')
        self.params = data.get('initdata').get('params')
        self.splc = data.get('initdata').get('splc')
        self.qlrParams = {
            "ywlxNode": "changeRegister",
            "qlrmc": generateQLRName(),
            "qlrzjhm": generateCertNum(),
            "qlrdhhm": generateTelnum(),
            "qlrtxdz": generateAddr()
        }

    def test_jcChangeRegister(self,login,cmdopt):
        '''
        :流程 国有建设用地使用权及房屋所有权--转移登记--继承（02204）
        :return:
        '''
        self.driver = login[0]
        dbInfo = login[1]
        # 获取办件数据
        bdcdyh = dataInit(dbInfo).getSpfOrClfChangeRegisterData()
        print("办件受理数据为：%s" % bdcdyh)

        # 办件中心
        taskCenter(self.driver).common()
        # 选择流程
        taskCenter(self.driver).chooseNode(self.qllx, self.djlx, self.ywlx)
        # 发起查询
        queryFunc(self.driver).query(bdcdyh, self.qllx, self.djlx)
        # 收件单
        sjdPage(self.driver).sjdHandle(bdcdyh, self.qllx, **self.params)
        # 申请人情况
        sqrqkPage(self.driver).sqrqkHandle(**self.qlrParams)
        # 申请表
        sqbPage(self.driver).sqbHandle(self.qllx, self.ywlx)
        # 不动产基本信息
        bdcjbxxPage(self.driver).bdcjbxxHandle(self.ywlx)
        # 收费领证表
        sflzbPage(self.driver).sflzbHandle(self.sfTemplate)
        # 办理意见表
        blyjPage(self.driver).blyjHandle()
        # 受理
        submitPage(self.driver).slHandle()
        # 审核
        submitPage(self.driver).shHandle(bdcdyh, cmdopt, self.splc)
        # 登簿
        submitPage(self.driver).dbHandle(bdcdyh)

        qlrmc = self.qlrParams.get("qlrmc")
        if qlrmc:
            try:
                resDataCheck = dataResCheck(dbInfo).houseRegisterDataCheck(bdcdyh, qlrmc)
                print("数据库检查结果是：", resDataCheck)
                assert resDataCheck
            except AssertionError:
                raise

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-v','test_jcChangeRegister'])