#封装流程受理（收件单 ）
'''
:param driver  浏览器驱动
:bdcdyh 不动产单元号，区分净地和房屋

'''
import time
from Common.CommonFunc import WebTools

class sjdPage():
    def __init__(self,driver):
        self.driver = driver

    def sjdHandle(self,bdcdyh,qllx,**params):
        '''
        :param qllx:权利类型
        :param bdcdyh:不动产单元号
        :param **kwargs: dict (option) 业务小类，房屋类别,是否发证
        '''
        WebTools(self.driver).mouse_click('link_text','收件单')
        time.sleep(1)

        #房屋业务涉及业务小类或者房屋类别选择
        ywxl = params.get("ywxl",None)
        fwlb = params.get("fwlb",None)
        sffz = params.get("sffz",None)
        print("params参数：{ywxl:%s,fwlb:%s,sffz:%s}" %(ywxl,fwlb,sffz))

        if bdcdyh[19:20] == 'F':
            #房--业务小类
            if qllx =='国有建设用地使用权及房屋所有权':
                if ywxl:  #ywxl !='' and ywxl != None
                    if ywxl == '市场化商品房首次登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[2]")
                    elif ywxl == '征地拆迁安置房首次登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[3]")
                    elif ywxl == '经济适用房首次登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[4]")
                    elif ywxl == '房改售房转移登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[5]")
                    # 转移登记
                    elif ywxl == '经济适用房上市':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[2]")
                    elif ywxl == '拆迁安置房上市':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[3]")
                    elif ywxl == '存量房转移登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[5]")
                    elif ywxl == '市场化商品房转移登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[6]")
                    else:
                        pass
                else:
                    print("%s收件单业务小类必选！"%qllx)
                    return
            #房屋抵押--房屋类别
            elif qllx =='抵押权':
                if fwlb:
                    if fwlb == '商品房':
                        WebTools(self.driver).choose_droplist_value('fwlb', 'xpath', "//select[@name='fwlb']/option[2]")
                    elif fwlb == '存量房':
                        WebTools(self.driver).choose_droplist_value('fwlb', 'xpath', "//select[@name='fwlb']/option[3]")
                    else:
                        pass
                else:
                    print("%s收件单房屋类别必选！"%qllx)
                    return
            #查封登记--业务小类,房屋类别
            elif qllx == '查封登记':
                if ywxl:
                    if ywxl == '查封登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[2]")
                    elif ywxl == '轮候查封登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[3]")
                    else:
                        pass
                else:
                    print("%s收件单业务小类必选！"%qllx)
                    return
                if fwlb:
                    if fwlb == '商品房':
                        WebTools(self.driver).choose_droplist_value('fwlb', 'xpath', "//select[@name='fwlb']/option[2]")
                    elif fwlb == '存量房':
                        WebTools(self.driver).choose_droplist_value('fwlb', 'xpath', "//select[@name='fwlb']/option[3]")
                else:
                    print("%s收件单房屋类别必选！"%qllx)
                    return
        else:#净地
            if qllx == '查封登记':
                if ywxl:
                    if ywxl == '查封登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[2]")
                    elif ywxl == '轮候查封登记':
                        WebTools(self.driver).choose_droplist_value('ywxl', 'xpath', "//select[@name='ywxl']/option[3]")
                else:
                    print("%s收件单业务小类必选！"%qllx)
                    return

        # 是否发证
        if sffz:
            WebTools(self.driver).choose_droplist_value('lzdz', 'xpath', "//select[@name='lzdz']/option[2]")
            time.sleep(1)
        # #发证--领证地址
        # if qllx == '国有建设用地使用权'or qllx == '国有建设用地使用权及房屋所有权'or qllx == '抵押权' or qllx == '预告登记':
        #     WebTools(self.driver).choose_droplist_value('lzdz', 'xpath', "//select[@name='lzdz']/option[2]")
        #     time.sleep(1)
        # else:
        #     pass


