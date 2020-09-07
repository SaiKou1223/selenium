from selenium import webdriver
import lxml.etree
# 谷歌静默模式
from urllib import request
driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')
input = driver.find_element_by_class_name("nav-search-keyword")
input.send_keys("刘皇叔")
button = driver.find_element_by_class_name("nav-search-btn")
button.click()
while True:
    try:
        windows = driver.window_handles
        # 是获取当前的所有窗口
        driver.switch_to.window(windows[-1])
        # 是切换到最新打开的窗口
        driver.switch_to.default_content()
        llxml = driver.page_source
        soul = lxml.etree.HTML(llxml)
        items = soul.xpath('//ul[@class="video-list clearfix"]/li')
        for item in items:
            title = item.xpath('./a/@title')[0]
            href = item.xpath('./a/@href')[0]
            link = "https:"+href
            print("title:",title,"href:",link,)
    except:
        break