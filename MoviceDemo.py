from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chromeOpt = Options()
chromeOpt.add_argument("--headless")
chromeOpt.add_argument("--disable-gpu")
chromeOpt.add_argument("--window-size=1400,3600")
chrome = webdriver.Chrome(chrome_options=chromeOpt)
try:
    chrome.implicitly_wait(5)  # 隐式等待 5 min
    chrome.get("https://www.dytt8.net")
    chrome.find_element_by_id("cs_ap_8040").click()
    chrome.switch_to.window(chrome.window_handles[0])

    aListLength = len(chrome.find_elements_by_xpath("//div[@class='co_content2']//a"))
    # 类型必须是一致的才能使用+
    print("length="+str(aListLength))
    initI = 1
    while initI < aListLength:
        initI =initI +1
        chrome.switch_to.window(chrome.window_handles[0])
        tempXpath = "//div[@class='co_content2']//a["+str(initI)+"]"
        print(tempXpath)
        chrome.find_element_by_xpath(tempXpath).click()
        chrome.switch_to.window(chrome.window_handles[len(chrome.window_handles)-1])
        chrome.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(15)
        contentList = chrome.find_elements_by_xpath("//table")
        for t in contentList:
            try:
                aObj = t.find_element_by_tag_name("a")
                print(aObj.text)
            except AttributeError as e:
                pass
            except NoSuchElementException as b:
                pass
            finally:
                ActionChains(chrome).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
                #chrome.close() #该方法只会关闭第一个页面
                pass


    # chrome.find_element_by_xpath("//div[@class='co_content2']//a[3]").click()
    # chrome.switch_to.window(chrome.window_handles[2])
    # chrome.execute_script("document.documentElement.scrollTop=1000")
    # time.sleep(10)
    # contentList = chrome.find_elements_by_xpath("//table")
    # for t in contentList:
    #     try:
    #         aObj = t.find_element_by_tag_name("a")
    #         print(aObj.text)
    #     except AttributeError as e:
    #         pass
    #     except NoSuchElementException as b:
    #         pass
except TypeError as e:
    print(e)
finally:
    chrome.quit()

