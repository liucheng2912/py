from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps={
  "platformName": "android",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": "true",
  "deviceName": "127.0.0.1:7555",
  "noResrt":True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(20)
TouchAction(driver).tap(x=125, y=147).perform()
TouchAction(driver).tap(x=44, y=152).perform()



driver.quit()