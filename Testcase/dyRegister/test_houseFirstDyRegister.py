'''
抵押权-- 首次登记 -- 不动产抵押
'''
import pytest
from dataInit.dataInit import dataInit
from pageObject.taskCenter import taskCenter
from pageObject.queryFunc import queryFunc
from pageObject.sjdPage import sjdPage
from pageObject.sqrqkPage import sqrqkPage
from init.userInfoInit import generateAddr,generateCertNum,generateDYQLRName,generateTelnum
from pageObject.sqbPage import sqbPage
from pageObject.bdcjbxxPage import bdcjbxxPage
from pageObject.sflzbPage import sflzbPage
from pageObject.blyjPage import blyjPage
from pageObject.common.submitFunc import submitFunc
from pageObject.common.FsOrShPage import FsOrShPage
from pageObject.common.dbPage import dbPage
from dataCheck.dataResCheck import dataResCheck

# 参数
qllx = "抵押权"
djlx = "首次登记"
ywlx = "不动产抵押（03102）"
params = {"fwlb": "商品房"}
qlrParams = {"ywlxNode": "dyRegister", "qlrmc": generateDYQLRName(), "qlrzjhm": generateCertNum(),
             "qlrdhhm": generateTelnum(), "qlrtxdz": generateAddr()}
sfTemplate = "tz"  # 收费模板 目前支持泰州、无锡模板

class Test_houseFirstDyRegister():
    def setup(self):
        # 获取办件受理数据数据
        self.bdcdyh = dataInit().getHouseFirstDyRegisterData()
        print("办件受理数据为：%s" % self.bdcdyh)

    def test_houseFirstDyRegister(self,login):
        self.driver = login

        #办件中心
        taskCenter(self.driver).common()
        #选择流程
        taskCenter(self.driver).chooseNode(qllx,djlx,ywlx)
        #发起查询
        queryFunc(self.driver).query(self.bdcdyh, qllx, djlx)
        #收件单
        sjdPage(self.driver).sjdHandle(self.bdcdyh, qllx,**params)
        #申请人情况
        sqrqkPage(self.driver).sqrqkHandle(**qlrParams)
        #申请表
        sqbPage(self.driver).sqbHandle(qllx, ywlx)
        #不动产基本信息
        bdcjbxxPage(self.driver).bdcjbxxHandle(qllx,ywlx)
        #收费领证表
        sflzbPage(self.driver).sflzbHandle(sfTemplate)
        #受理意见表
        blyjPage(self.driver).blyjHandle()
        #受理提交
        submitFunc(self.driver).submitHandle('sl')
        #复审环节
        FsOrShPage(self.driver).FsOrShHandle(self.bdcdyh)
        #复审提交
        submitFunc(self.driver).submitHandle('fs')
        #等簿环节
        FsOrShPage(self.driver).FsOrShHandle(self.bdcdyh)
        #等簿提交
        dbPage(self.driver).dbHandle()

        # 校验数据库(后期可以把数据库连接串配置化，这样可以针对不同环境校验)
        qlrmc = qlrParams.get("qlrmc")
        if qlrmc:
            try:
                resDataCheck = dataResCheck().dyRegisterDataCheck(self.bdcdyh, qlrmc)
                print("数据库检查结果是：", resDataCheck)
                assert resDataCheck
            except AssertionError:
                raise

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-v', 'test_houseFirstDyRegister'])
