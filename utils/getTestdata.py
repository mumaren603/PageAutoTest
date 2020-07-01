import os
import yaml

def getTestdataPath(testcase_path):
    '''
    根据 测试用例路径 匹配到 对应测试数据路径
    :param testcase_path:  测试用例绝对路径，由对应测试用例里传过来
    :return:
    '''
    temp_path  = testcase_path.split('Testcase/')
    print(temp_path)
    testdata_path = os.path.join(temp_path[0],'Testdata',temp_path[1]).replace('\\','/').replace('.py','.yml')
    print("测试数据路径是%s" % testdata_path)
    return testdata_path


# def getTestcaseData(testdata_path,cmdopt):
#     '''
#     :param testdata_path: 测试用例对应测试数据文件路径 由getTestdataPath()返回
#     :return:
#     '''
#     with open(testdata_path,mode='r',encoding='utf-8') as f:
#         data = yaml.load(f,Loader=yaml.FullLoader)
#         print("=====data值为=====",data)
#         splc_value = data.get('splc')
#         if cmdopt in splc_value:
#             for k,v in splc_value.items():
#                 if cmdopt == k:
#                     print("ok",k)
#                     data['splc']={cmdopt,k}
#                     print("更新后data为：",data)
#                     return data
#         else:
#            return None

def getTestcaseData(testdata_path):
    '''
    :param testdata_path: 测试用例对应测试数据文件路径 由getTestdataPath()返回
    :return:
    '''
    with open(testdata_path,mode='r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data

if __name__ == '__main__':
    pass
