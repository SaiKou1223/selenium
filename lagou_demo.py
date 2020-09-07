from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import lxml.etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
driver = webdriver.Chrome()
url = 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E7%88%AC%E8%99%AB'
driver.get(url)
source = driver.page_source
soul = lxml.etree.HTML(source)
items = soul.xpath('//a[@class="position_link"]/@href')
for item in items:
    print(item)
# 获取详情页url后 重复操作获取详细信息