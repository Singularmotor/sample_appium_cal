#coding=utf-8
#running in Pyhton3.6

import os
from appium import webdriver

from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Galaxy Note4'
desired_caps['appPackage'] = 'com.sec.android.app.popupcalculator'
desired_caps['appActivity'] = 'com.sec.android.app.popupcalculator.Calculator'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',desired_caps)
print("初始化完成")

try:
    driver.find_element_by_accessibility_id('1').click()
    print('1')
    driver.find_element_by_id('com.sec.android.app.popupcalculator:id/bt_add').click()
    print('2')
    driver.find_element_by_xpath('//android.widget.Button[@content-desc="5"]').click()
    print('3')
    driver.find_element('id','com.sec.android.app.popupcalculator:id/bt_equal').click()
    print('4')
    a = driver.find_elements_by_id('com.sec.android.app.popupcalculator:id/txtCalc').text
    print(a)
    if a=='1+5 =6. 正在编辑。':
        print('correct')
    else:
        print('fail1')
except:
    print('fail2')

driver.quit()




