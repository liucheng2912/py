from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWx:
    def setup(self):
        desired_caps = {"platformName": "android",
                        "appPackage": "com.tencent.wework",
                        "appActivity": ".launch.LaunchSplashActivity",
                        "noReset": "true",
                        "deviceName": "127.0.0.1:7555",
                        "unicodeKeyBoard": "true",
                        "resetKeyBoard": "true",
                        "settings[waitForIdleTimeout]":0
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wx(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0))')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        #self.driver.update_settings({'waitForIdleTimeout':0})
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        #sleep(2)
        #assert '外出打卡成功' in self.driver.page_source
        WebDriverWait(self.driver,10).until(lambda x:'外出打卡成功' in x.page_source)

















