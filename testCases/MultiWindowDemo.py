#coding=utf-8

from selenium.webdriver.chrome.options import Options
from  multiprocessing import Pool
from selenium import webdriver
import  time


chromeOpt = Options()
#chromeOpt.add_argument("--headless")
#chromeOpt.add_argument("--disable-gpu")
#chromeOpt.add_argument("--window-size=1400,3600")
chrome = webdriver.Chrome(chrome_options=chromeOpt)

def openUrl(url):
    try:
        windowUrl = "window.open('{}')".format(url)
        chrome.execute_script(windowUrl)
        time.sleep(5)
        pass
    except BaseException as e:
        print(e)
    pass



if __name__ == '__main__':
    try:
        chrome.implicitly_wait(5)  # 隐式等待 5 min
        chrome.get("https://www.dytt8.net")
        chrome.find_element_by_id("cs_ap_8040").click()
        chrome.switch_to.window(chrome.window_handles[0])

        aListLength = len(chrome.find_elements_by_xpath("//div[@class='co_content2']//a"))
        # 类型必须是一致的才能使用+
        print("length=" + str(aListLength))


        urlList = []
        initI = 0
        while initI < 10:
            initI += 1  #自增
            tempXpath = "//div[@class='co_content2']//a[" + str(initI) + "]"
            href = chrome.find_element_by_xpath(tempXpath).get_attribute("href")
            print(href)
            # 判断href 是否是 None
            if not(href is None):
                urlList.append(href)
            pass
        #print(urlList)
        pool = Pool(4)
        rl  = pool.map(openUrl,urlList)
        pool.close()
        pool.join()
        pass
    except TypeError as e:
        print(e)
        pass
    except:
        print("error")
    finally:
        chrome.quit()