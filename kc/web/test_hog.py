import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHog:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(3)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_hog(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('霍格沃茨测试学院')
        self.driver.find_element_by_css_selector('.s_btn').click()
        self.driver.find_element_by_partial_link_text('腾讯课堂官网').click()
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to_window(handles[-1])
        self.driver.find_element_by_partial_link_text('名企定向培养').click()


