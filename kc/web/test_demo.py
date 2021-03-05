from selenium import webdriver

class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def test_search(self):
        #创建一个chromedriver的实例
        search = self.driver.find_element_by_id('su')
        assert  search=="百度"

    def test_input(self):
        self.driver.find_element_by_name('wd').send_keys('霍格沃茨测试学院')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_name('wd').clear()

    def test_attribute(self):
        search=self.driver.find_element_by_id('su')
        print(search.get_attribute('value'))
        print(search.location)
        print(search.size)

    def test_refresh(self):
        self.driver.refresh()
        print(self.driver.page_source)

    def test_window(self):
        self.driver.minimize_window()
        self.driver.maximize_window()
        self.driver.set_window_rect(1000,1000)
        
    def teardown(self):
        #self.driver.quit()
        self.driver.close()