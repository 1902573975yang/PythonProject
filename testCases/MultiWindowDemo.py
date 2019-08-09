#coding=utf-8

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from  multiprocessing import Pool
from selenium import webdriver
import  time



def openUrl(url):
    chromeOptNew = Options()
    chromeOptNew.add_argument("--headless")
    chromeOptNew.add_argument("--disable-gpu")
    chromeOptNew.add_argument("--window-size=1400,3600")
    chromeDriverNew = webdriver.Chrome(chrome_options=chromeOptNew)
    try:
        #打开新标签推荐使用这种方式
        # windowUrl = "window.open('{}')".format(url)
        # chrome.execute_script(windowUrl)
        # current_page_handle = chrome.window_handles[-1]

        # 缺换handle
        # print(current_page_handle)
        # chrome.switch_to.window(current_page_handle)

        chromeDriverNew.get(url)
        time.sleep(15)
        content_list = chromeDriverNew.find_elements_by_xpath("//table")
        for t in content_list:
            try:
                aObj = t.find_element_by_tag_name("a")
                print(aObj.text)
            except AttributeError as attr:
                print(attr)
                pass
            except NoSuchElementException as nse:
                print(nse)
                pass
            finally:
                pass
        pass
    except BaseException as e:
        print(e)
        pass
    finally:
        chromeDriverNew.quit()
    pass



if __name__ == '__main__':
    chromeOpt = Options()
    chromeOpt.add_argument("--headless")
    chromeOpt.add_argument("--disable-gpu")
    chromeOpt.add_argument("--window-size=1400,3600")
    chromeDriver = webdriver.Chrome(chrome_options=chromeOpt)
    try:
        chromeDriver.implicitly_wait(5)  # 隐式等待 5 min
        chromeDriver.get("https://www.dytt8.net")
        chromeDriver.find_element_by_id("cs_ap_8040").click()
        chromeDriver.switch_to.window(chromeDriver.window_handles[0])

        aListLength = len(chromeDriver.find_elements_by_xpath("//div[@class='co_content2']//a"))
        # 类型必须是一致的才能使用+
        print("length=" + str(aListLength))


        urlList = []
        initI = 0
        while initI < 10:
            initI += 1  #自增
            tempXpath = "//div[@class='co_content2']//a[" + str(initI) + "]"
            href = chromeDriver.find_element_by_xpath(tempXpath).get_attribute("href")
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
        print("join")
        pass
    except TypeError as e:
        print(e)
        pass
    except:
        print("error")
    finally:
        chromeDriver.quit()