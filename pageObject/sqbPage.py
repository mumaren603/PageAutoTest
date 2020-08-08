#封装流程受理（申请表）
'''
:param driver  浏览器驱动
'''
import time
from Common.CommonFunc import WebTools


class sqbPage():
    def __init__(self,driver):
        self.driver = driver

    # def sqbHandle(self,qllx,*args,**kwargs):
    def sqbHandle(self, qllx, ywlx, **kwargs):
        WebTools(self.driver).mouse_click('link_text','申请表')
        time.sleep(4)

        if qllx == '国有建设用地使用权' or qllx =='国有建设用地使用权及房屋所有权':
            if ywlx == '自建房屋（02102）':
                # 业务小类
                if kwargs.get('ywxl', None) == '个人自建房':
                    WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', '//select[@name="ywxl"]/option[3]')
                elif kwargs.get('ywxl', None) == '单位自建房':
                    WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', '//select[@name="ywxl"]/option[2]')
                else:
                    print("%s业务业务小类必填！" %ywlx)

                # 领证地址
                self.driver.execute_script('document.documentElement.scrollTop=700')
                time.sleep(1)
                WebTools(self.driver).choose_droplist_value('lzdz', 'xpath', '//select[@name="lzdz"]/option[2]')

            # 独用土地面积
            # WebTools(self.driver).input_content('xpath', "//input[@xid='tdsyqdymj']",'0')
                # 获取独用土地面积，该字段为空提交会存在必填校验，需要传值
                # import execjs
                # try:
                #     js = execjs.compile('''var value1 = $("input[xid='tdsyqdymj']").val()''')
                #     tdsyqdymj = driver.execute_script(js)
                #     print("土地使用权独用面积：%s" %tdsyqdymj)
                # except Exception as e:
                #     print(e)



            # 自建房屋流程没有收件单 领证地址等信息放到申请表页面
            # if args[0] =='自建房屋（02102）':
            #     # 业务小类
            #     if kwargs.get('ywxl',None) == '个人自建房':
            #         WebTools(self.driver).choose_droplist_value('ywxl', 'name', '//select[@name="ywxl"]/option[3]')
            #     elif kwargs.get('ywxl',None) == '单位自建房':
            #         WebTools(self.driver).choose_droplist_value('ywxl', 'name', '//select[@name="ywxl"]/option[2]')
            #     else:
            #         print("%s业务业务小类必填！" %args[0])
            #     # 领证地址
            #     # 将页面滚动条拖到顶部
            #     # js= "var q = document.documentElement.scrollTop=0"
            #     self.driver.execute_script('document.documentElement.scrollTop=500')
            #     time.sleep(1)
            #     WebTools(self.driver).choose_droplist_value('lzdz','name','//select[@name="lzdz"]/option[2]')
        elif qllx =='抵押权':
            #抵押业务
            #预置数据（当前时间）
            currentDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            #预置数据（抵押结束时间）
            fetureDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400 * 365 * 10))
            #抵押方式
            WebTools(self.driver).choose_droplist_value('DYFS', 'xpath', "//select[@name='DYFS']/option[2]")
            #不动产价值
            WebTools(self.driver).input_content('xpath',"//input[@xid='dywjz']",'1000000')
            #抵押合同签订日期
            WebTools(self.driver).input_content('xpath', "//input[@xid='DYHTQDRQ']", currentDate)
            #被担保主债权数额
            WebTools(self.driver).input_content('xpath',"//input[@xid='bdbzqse']",'800000')
            #债务履行起始时间
            WebTools(self.driver).input_content('xpath', "//input[@xid='zwlxqssj']", currentDate)
            #债务履行结束时间
            WebTools(self.driver).input_content('xpath', "//input[@xid='zwlxjssj']", fetureDate)
            #最高债权确定事实和数额
            WebTools(self.driver).input_content('xpath', "//textarea[@xid='ZGZQQDSSJSE']", 500000)
        elif qllx == '查封登记':
            #预置数据（当前时间）
            currentDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            #查封机关
            WebTools(self.driver).input_content('xpath',"//input[@xid='cfjg']",'北京市中级人民法院')
            #查封文号
            WebTools(self.driver).input_content('xpath',"//input[@xid='cfwj']",args[0])
            #查封起始日期
            WebTools(self.driver).input_content('xpath',"//input[@xid='CFQSRQ']",currentDate)
            #查封期限
            WebTools(self.driver).mouse_click('xpath', "//input[@xid='btnAdd2']")
            #来文日期
            WebTools(self.driver).input_content('xpath',"//input[@xid='lwrq']",currentDate)
            #查封范围
            WebTools(self.driver).input_content('xpath',"//input[@xid='cffw']","该产权所有，包括附着物（测试）。")

