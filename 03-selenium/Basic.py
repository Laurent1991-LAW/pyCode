from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os,time

ch = webdriver.Chrome()

ch.get('https://www.examtopics.com/exams/amazon/aws-certified-sap-on-aws-specialty-pas-c01/view/')

# 获取输入框 输入 回车
button = ch.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div/a[2]/i')
print('Get search button, ready to click')
button.click()
print('Get search button, click finished, getting input')

# /html/body/div[4]/div/div/div/form/div/input

input = ch.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div/input')
print('Input get, start send keys')

time.sleep(3)
input.send_keys('sap')
input.send_keys(Keys.ENTER)

print(ch.page_source)
time.sleep(3)
ch.close()