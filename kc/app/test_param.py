import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestParam():
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
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('search_name,type,expected_price',[
        ('阿里巴巴','BABA',230),
        ('小米','01810',24)
    ])
    def test_param(self,search_name,type,expected_price):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(search_name)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        price_ele=self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        res = float(price_ele.text)
        print(res)
        expected_price=expected_price
        assert_that(res,close_to(expected_price,expected_price*0.1))