'''
封装办件中心
:param qllx 权利类型 如（国有建设用地使用权）
:param djlx 登记类型 如（首次登记）
:param ywlx 业务类型 如 出让用地)
'''
from Common.CommonFunc import WebTools
import time


class taskCenter():
    def __init__(self,driver):
        self.driver = driver

    def common(self):
        # 办件中心
        WebTools(self.driver).mouse_click('xpath', "//div[@xid='mainMenu']/div[1]/div[1]")
        # 判断新建任务菜单是否出现
        WebTools(self.driver).check_element_is_exists('xpath', "//span[@xid='newTask']")
        # 等待办件中心办件中数据加载
        time.sleep(4)
        # 新建任务
        WebTools(self.driver).mouse_click('xpath',"//span[contains(text(),'新建任务')]")
        WebTools(self.driver).check_element_is_exists('link_text', "国有建设用地使用权")

    def chooseNode(self,qllx=None,djlx=None,ywlx=None):
        '''
        流程发起菜单，包括一级菜单、二级菜单、三级菜单
        :param qllx: 权利类型
        :param djlx: 登记类型（optional）
        :param ywlx: 业务类型
        :return:
        '''
        if qllx and ywlx:
            if qllx == '国有建设用地使用权':
                if djlx =='首次登记':
                    if ywlx == '出让用地':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167090000060]/div[1]")
                        time.sleep(2)
                elif djlx == '转移登记':
                    WebTools(self.driver).mouse_click('xpath',"//ul[@xid='subUl0']/li[2]/a")
                    time.sleep(2)
                    if ywlx == '转移登记（01201）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167090000064]/div[1]")
                        time.sleep(2)
                    elif ywlx == '分割合并转移登记（01202）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167010001541]/div[1]")
                        time.sleep(2)
                    elif ywlx == '裁定过户（01203）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167010001761]/div[1]")
                        time.sleep(2)
                elif djlx == '变更登记':
                    WebTools(self.driver).mouse_click('xpath',"//ul[@xid='subUl0']/li[3]/a")
                    if ywlx =='名称、地址、用途等变更登记（01303）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167090000067]/div[1]")
                        time.sleep(2)
                    elif ywlx =='分割合并变更（01304）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167010001542]/div[1]")
                        time.sleep(2)
                elif djlx == '注销登记':
                    WebTools(self.driver).mouse_click('xpath',"//ul[@xid='subUl0']/li[4]/a")
                    if ywlx =='注销登记（01401）':
                        WebTools(self.driver).mouse_doubleClick('xpath',"//div[@ywlxid=167090000068]/div[1]")
                        time.sleep(2)
            elif qllx == '国有建设用地使用权及房屋所有权':
                WebTools(self.driver).mouse_click('link_text',"国有建设用地使用权及房屋所有权")
                if djlx =='首次登记':
                    if ywlx == '商品房、征地拆迁安置房、经适房、房改售房（02101）' or ywlx == '历史性房屋首次登记（包括商品房、征地拆迁安置房、经适房、房改售房）（02101）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000118]/div[1]")
                        time.sleep(2)
                    elif ywlx == '自建房屋（02102）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000070]/div[1]")
                        time.sleep(2)
                    elif ywlx == '建筑物区分业主共有部分（02103）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000071]/div[1]")
                        time.sleep(2)
                    elif ywlx == '车库（位）及其他附属设施（02104）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000072]/div[1]")
                        time.sleep(2)
                    elif ywlx == '首次登记（批量）（02105）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167010000260]/div[1]")
                        time.sleep(2)
                    elif ywlx == '项目内多幢（02106）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167010001401]/div[1]")
                        time.sleep(2)
                    else:
                        print("业务类型（%s）不存在！" % self.ywlx)
                elif djlx == '转移登记':
                    WebTools(self.driver).mouse_click('xpath', "//ul[contains(@xid,'subUl1')]/li[2]/a")
                    if ywlx =='房屋首次转移登记（含商品房、经适房、安置房）（02201）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[contains(text(),'房屋首次转移登记（含商品房、经适房、安置房）（02201）')]")
                        time.sleep(2)
                    elif ywlx =='存量房买卖（含公房、解困房、安居房、经适房、安置房）（02203）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[contains(text(),'存量房买卖（含公房、解困房、安居房、经适房、安置房）（02203）')]")
                        time.sleep(2)
                    elif ywlx =='房改售房（02202）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[contains(text(),'房改售房（02202）')]")
                        time.sleep(2)
                    elif ywlx =='继承（02204）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[contains(text(),'继承（02204）')]")
                        time.sleep(2)
                    elif ywlx =='赠与，归并（02205）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[contains(text(),'赠与，归并（02205）')]")
                        time.sleep(2)
                elif djlx == '变更登记':
                    pass
                elif djlx == '注销登记':
                    pass
                else:
                    print("登记类型（%s）不存在！" % self.djlx)
            elif qllx == '抵押权':
                WebTools(self.driver).mouse_click('link_text',"抵押权")
                if djlx =='首次登记':
                    if ywlx == '土地抵押（03101）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000091]/div[1]")
                        time.sleep(2)
                    elif ywlx == '不动产抵押（03102）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000092]/div[1]")
                        time.sleep(2)
                    elif ywlx == '在建房地产（03103）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000093]/div[1]")
                        time.sleep(2)
                elif djlx == '转移登记':
                    WebTools(self.driver).mouse_click('xpath', "//ul[contains(@xid,'subUl2')]/li[2]/a")
                    if ywlx == '土地抵押转移（03201）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000094]/div[1]")
                        time.sleep(2)
                    elif ywlx == '不动产抵押转移（03202）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000095]/div[1]")
                        time.sleep(2)
                    elif ywlx == '预抵押转现（03204）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167010000303]/div[1]")
                        time.sleep(2)
            elif qllx == '查封登记':
                WebTools(self.driver).mouse_click('link_text', "查封登记")
                if ywlx == '查封登记（包括轮候查封）（05001）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000104]/div[1]")
                        time.sleep(2)
                elif ywlx == '查封登记（续查封）（05005）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167010000140]/div[1]")
                        time.sleep(2)
                elif ywlx == '解封登记（05002）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000105]/div[1]")
                        time.sleep(2)
                elif ywlx == '批量查封（05004）':
                        WebTools(self.driver).mouse_doubleClick('xpath', "//div[@ywlxid=167090000107]/div[1]")
                        time.sleep(2)
        else:
            print("权利类型(qllx)和业务类型(ywlx)参数必填。")
