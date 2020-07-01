import pytest
from dataInit.dataInit import dataInit
from pageObject.taskCenter import taskCenter
from pageObject.queryFunc import queryFunc
from pageObject.cancleRegisterCommonPage import cancleRegisterCommonPage
from pageObject.common.submitFunc import submitFunc
from pageObject.common.FsOrShPage import FsOrShPage
from dataCheck.dataResCheck import dataResCheck

# 参数
qllx = "国有建设用地使用权"
djlx = "注销登记"
ywlx = "注销登记（01401）"
class Test_LandFirstRegister():
    def setup(self):
        # 获取办件受理数据数据
        self.bdcdyh = dataInit().getLandCancleRegisterData()
        print("办件受理数据为：%s" % self.bdcdyh)

    def test_landCancelRegister(self,login):
        self.driver = login

        #办件中心
        taskCenter(self.driver).common()
        #选择流程
        taskCenter(self.driver).chooseNode(qllx,djlx,ywlx)
        #发起查询
        queryFunc(self.driver).query(self.bdcdyh,qllx,djlx)
        #收件单
        cancleRegisterCommonPage(self.driver).sjdHandle()
        #申请人情况
        cancleRegisterCommonPage(self.driver).sqrqkHandle()
        #申请表
        cancleRegisterCommonPage(self.driver).sqbHandle()
        #不动产基本信息
        cancleRegisterCommonPage(self.driver).bdcjbxxHandle()
        #受理意见表
        cancleRegisterCommonPage(self.driver).blyjHandle()
        #受理提交
        submitFunc(self.driver).submitHandle('sl')
        #复审环节
        FsOrShPage(self.driver).FsOrShHandle(self.bdcdyh)
        #复审提交
        submitFunc(self.driver).submitHandle('fs')
        #登簿环节
        FsOrShPage(self.driver).FsOrShHandle(self.bdcdyh)
        #登簿提交
        cancleRegisterCommonPage(self.driver).dbHandle()

        #校验数据库(后期可以把数据库连接串配置化，这样可以针对不同环境校验)
        try:
            resDataCheck = dataResCheck().landCancleRegisterDataCheck(self.bdcdyh)
            print("数据库检查结果是：",resDataCheck)
            assert resDataCheck
        except AssertionError:
            raise

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-v', 'test_landCancelRegister'])
