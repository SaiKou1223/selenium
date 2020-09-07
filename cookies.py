from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# print(driver.get_cookies())
# for cookie in driver.get_cookies():
#     print(cookie)
# 分条输出cookies信息
# print(driver.get_cookie("PSTM"))
# 获取带有关键词的cookies信息
# driver.delete_cookie("PSTM")
# 删除指定cookies信息
# driver.delete_all_cookies()
# 删除所有cookies信息
# print(driver.get_cookies())