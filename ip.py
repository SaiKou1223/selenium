from selenium import webdriver
options = webdriver.ChromeOptions()
# ip = 192.168.1.111
# port = 2525
options.add_argument("--proxy-server-http://192.168.1.111:1111")
driver = webdriver.Chrome(chrome_options=options)
url = 'httpbin.org/ip'
driver.get(url)