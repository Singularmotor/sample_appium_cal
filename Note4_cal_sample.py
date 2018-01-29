#coding=utf-8
#running in Pyhton3.6

#加载运行环境所需的API
import os
from appium import webdriver
from time import sleep

#设置系统查找软件包地址方式
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)
#确认设备是否正常连接到pc
def connectD():
    try:
        deInfo = os.popen('adb devices').read()
        if deInfo == '':
            return False
        else:
            return True
    except Exception as e:
        print('设备连接失败:',e)

#自动识别连接设备的信息
#识别手机名称对应参数deviceName
def auto_get_DeName():
    try:
        if connectD():
            DeName = os.popen('adb shell getprop ro.product.model').read()
            return DeName
        else:
            return '连接失败，请重新尝试'
    except Exception as e:
        print('DeName信息获取失败:',e)
    return 0

#识别手机系统版本对应参数platformVersion
def auto_get_DeVersion():
    try:
        if connectD():
            DeVersion = os.popen('adb shell getprop ro.build.version.release').read()
            return DeVersion
        else:
            return '连接失败，请重新尝试'
    except Exception as e:
        print('DeVersion信息获取失败:',e)
    return 0

#上传appium-servers初始化参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = auto_get_DeVersion() #更替为自动获取的设备信息
desired_caps['deviceName'] = auto_get_DeName() #更替为自动获取的设备信息
#desired_caps['app'] = PATH() 括号内填写软件包地址，如果安装软件包的话
desired_caps['appPackage'] = 'com.sec.android.app.popupcalculator'
desired_caps['appActivity'] = 'com.sec.android.app.popupcalculator.Calculator'

#设置appium地址，和导入参数完成初始化
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',desired_caps)
print("初始化完成")

#作容错处理运行用例
try:
    driver.find_element_by_accessibility_id('1').click()  #使用accessibility_id定位控件，完成点击事件
    print('1')
    driver.find_element_by_id('com.sec.android.app.popupcalculator:id/bt_add').click()  #使用id（resource-id）定位控件，完成点击事件
    print('2')
    driver.find_element_by_xpath('//android.widget.Button[@content-desc="5"]').click()  #使用xpath定位控件，完成点击事件
    print('3')
    driver.find_element('id','com.sec.android.app.popupcalculator:id/bt_equal').click()  #使用自定义方式定位控件，完成点击事件
    a = driver.find_element_by_id('com.sec.android.app.popupcalculator:id/txtCalc').text  #定位控件，并获取其文本内容
    print(a)
    if a == '1+5\n=6. 正在编辑。':  #使用文本对结果进行判断测试结果
        print('success')  #输出测试结果
    else:
        print('fail')  #输出测试结果
except:
    print('fail')  #输出测试结果

driver.quit()  #结束运行用例，回收资源




