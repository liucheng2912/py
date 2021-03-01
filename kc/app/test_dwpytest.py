import time

import hamcrest
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDw():
    def setup(self):
        desired_caps={"platformName": "android",
                      "appPackage": "com.xueqiu.android",
                      "appActivity": ".view.WelcomeActivityAlias",
                      "noReset": "true",
                      "deviceName": "127.0.0.1:7555",
                      "unicodeKeyBoard":"true",
                      "resetKeyBoard":"true"
                      }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print('搜索测试用例')
        self.driver.find_element(By.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element(By.ID,'com.xueqiu.android:id/current_price').text)
        assert price>200

    def test_search1(self):
        el1 = self.driver.find_element(By.ID,'com.xueqiu.android:id/tv_search')
        enable1 = el1.is_enabled()
        print(el1.text)
        print(el1.location)
        print(el1.size)
        if enable1==True:
            el1.click()
            self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            #res1 = self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").is_displayed()
            res2 = self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").get_attribute("displayed")
            if res2=='true':
                print('搜索成功')
    def test_action(self):
        action = TouchAction(self.driver)
        window_react = self.driver.get_window_rect()
        width = window_react['width']
        height = window_react['height']
        x1 = int(width/2)
        y_start = int(height*0.8)
        y_end = int(height*0.2)
        time.sleep(3)
        action.press(x=x1,y=y_start).wait(2000).move_to(x=x1,y=y_end).release().perform()
        time.sleep(3)

    def test_hk(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        re1 = self.driver.find_element(By.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 对应的股价价格是:{re1}")
        assert float(re1) < 200

    def test_wait(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)
        print(f"当前09988 对应的股价价格是:{ele.text}")
        assert float(ele.text) > 200

    def test_attr(self):
        ele=self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search')
        print(ele.get_attribute('text'))
        print(ele.get_attribute('displayed'))
        print(ele.get_attribute('enabled'))

if __name__ == '__main__':
    pytest.main()