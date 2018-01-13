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

#上传appium-servers初始化参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Galaxy Note4'
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




