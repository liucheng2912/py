from time import sleep

from selenium import webdriver

class BasePage:
    def __init__(self,driver:webdriver=None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            self._driver=driver

    def close(self):
        sleep(20)
        self._driver.quit()