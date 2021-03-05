from time import sleep

from appium import webdriver

class TestBrowser():
    def setup(self):
        desired_caps={"platformName": "android",
                      "browserName":"Browser",
                      "noReset": "true",
                      "deviceName": "127.0.0.1:7555",
                      "chromedriverExecutable":'E:\tool\mumu'
                      }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        sleep(5)