import os
import yaml

#只针对测试环境和开发环境,对应目录config
def collect_static_data(param):
    print("配置文件:",param)
    rootdir = os.path.dirname(os.path.dirname(__file__))
    confFilePath = os.path.join(rootdir,'config',param,'conf.yml').replace('\\','/')
    print("配置文件路径是：%s" % confFilePath)

    #打开文件,通过pyyaml读取内容
    with open(confFilePath,mode='r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data


#针对多个测试环境和开发环境,对应目录conf
def collect_static_data2(param):
    print("配置文件:",param)
    rootdir = os.path.dirname(os.path.dirname(__file__))
    configFile = param+'.yml'
    confFilePath = os.path.join(rootdir,'conf',configFile).replace('\\','/')
    print("配置文件路径是：%s" % confFilePath)

    #打开文件,通过pyyaml读取内容
    with open(confFilePath,mode='r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        print(data)
    return data

if __name__ == '__main__':
    collect_static_data2('tztest')




