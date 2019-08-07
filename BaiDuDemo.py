
from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get("http://www.baidu.com")

    browser.implicitly_wait(20)

    browser.find_element_by_id("kw").send_keys("selenium")

    time.sleep(2)

    browser.find_element_by_id("su").click()

    time.sleep(3)
    #如下只返回一个元素 ，要注意是否有s
    #browser.find_element_by_xpath("//div[@tpl='se_com_default']//a").click()
    #返回一个列表 ，所以使用下标,如下都可以
    #browser.find_elements_by_xpath("//div[@tpl='se_com_default']//a")[4].click()
    #browser.find_element_by_xpath("//div[@tpl='se_com_default']//a[1]").click()
    #browser.find_element_by_xpath("//div[@tpl='se_com_default']//em[text()='Selenium']").click()


    time.sleep(5)
except TypeError as e:
    print(e)
finally:
    browser.quit()