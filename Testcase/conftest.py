import pytest
from selenium import webdriver
from Common.CommonFunc import WebTools
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def login(request,getConfValue):

    print("yaml中读取配置内容：",getConfValue)
    driver_path = getConfValue.get('envinfo').get('browserDriver', None)
    print("浏览器驱动路径：%s" %driver_path)
    login_url = getConfValue.get('envinfo').get('url', None)
    print("url路径：%s" % login_url)
    login_user = getConfValue.get('envinfo').get('loginUser', None)
    print("登录用户信息：%s" % login_user)
    db_info = getConfValue.get('envinfo').get('db',None)

    if driver_path and login_url and login_user:
        driver = webdriver.Chrome(executable_path=driver_path)
        WebTools(driver).set_browser(login_url)
        #登录
        WebTools(driver).input_clear('xpath', "//input[contains(@id,'_name')]")
        WebTools(driver).input_clear('xpath', "//input[contains(@id,'_password')]")
        WebTools(driver).input_content('xpath', "//input[contains(@id,'_name')]", login_user.get('user'))
        WebTools(driver).input_content('xpath', "//input[contains(@id,'_password')]", login_user.get('passwd'))
        WebTools(driver).mouse_click('xpath', "//div[contains(@id,'_btnlogin')]")
        # 进入首页判断菜单是否出现
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'办件中心')]")))
            yield driver ,db_info
        except NoSuchElementException:
            print("NoSuchElementException")
            raise
    else:
        print("yaml中必须参数值缺失")

