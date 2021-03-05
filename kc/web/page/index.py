from selenium.webdriver.common.by import By

from kc.web.page.base_page import BasePage
from kc.web.page.login import Login
from kc.web.page.register import Register


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/'
    #进入注册页面
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT,'立即注册').click()
        return Register(self._driver)

    #进入登录页面
    def goto_login(self):
        self._driver.find_element(By.CSS_SELECTOR,'#indexTop > div.index_top_inside > aside > a.index_top_operation_loginBtn').click
        return Login(self._driver)