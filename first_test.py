# coding:utf-8
import time
from appium import webdriver

from appium.webdriver.common.mobileby import AppiumBy

"""
配置平台信息：
"platformName": 平台的名字
"platformVersion": 平台的版本
"deviceName": 设备名称
"appPackage": 应用的包名
"appActivity": 入口页面名
"noReset": 不需要重置
"""
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "cc",
    "appPackage": "com.sdw.mingjiaonline_patient",
    "appActivity": "com.sdw.mingjiaonline_patient.ui.activity.SplashActivity",
    "noReset": True
}

# 启动工作：与 appium server 之间建立连接，然后发送我的会话初始数据
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)



# 等待，1.强制等待，2.隐式等待，3.显式等待
driver.implicitly_wait(30)

# 元素定位方法： 通过resourceid属性定位  通过ID定位
ele_Mydor = driver.find_element("id", "com.sdw.mingjiaonline_patient:id/home_tools_tv")
ele_Mydor.click()

# find_element_by_android_uiautomator
driver.find_element('-android uiautomator', 'new UiSelector().text("下一步")').click()
# driver.find_element("id","com.sdw.mingjiaonline_patient:id/tv_password_login").click()    #点击延迟

# 点击坐标driver.tap([坐标]，时间)
driver.tap([(209, 1273), (209, 1273)], 100)

ele_passwd = driver.find_element("id", "com.sdw.mingjiaonline_patient:id/et_phone_number")
# ele_passwd = driver.find_element('-android uiautomator','new UiSelector().text("请输入密码")')
# com.sdw.mingjiaonline_patient:id/et_phone_number

ele_passwd.send_keys("bl123456")

driver.find_element('-android uiautomator', 'new UiSelector().text("登录")').click()

from appium.webdriver.common.mobileby import AppiumBy
