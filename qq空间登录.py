from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://qzone.qq.com/")
time.sleep(5)
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame"))
ele = driver.find_element_by_xpath('//a[@id="switcher_plogin"]')
ele.click()
ele = driver.find_element_by_id("u")
ele.send_keys("425709654")
ele = driver.find_element_by_id("p")
ele.send_keys("WoAiNi@123")
ele = driver.find_element_by_id("login_button")
ele.click()

# 2602905498
# Wo123456