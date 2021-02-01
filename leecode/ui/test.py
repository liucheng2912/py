from selenium import webdriver

driver=webdriver.Chrome()
url=("http://secure.finedevelop.com:65081/webroot/decision")
driver.get(url)

driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/input").send_keys("1")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/input").send_keys("1")
