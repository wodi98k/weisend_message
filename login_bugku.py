from selenium import webdriver
#  pip install webdriver_manager
import requests 
import time
import ddddocr
import sys
import os
username = sys.argv[1]
password = sys.argv[2]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
driver.maximize_window()
s = requests.session()
url = 'https://ctf.bugku.com/login'
driver.get(url=url)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
f = driver.find_element_by_id('vcode')
f.screenshot('code.png')
orc = ddddocr.DdddOcr()
with open('code.png','rb') as f:
    image_data = f.read()
    raw_data = orc.classification(image_data)
driver.find_element_by_name('vcode').send_keys(raw_data)
driver.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="checkin"]').click()
    print('签到成功')
    time.sleep(3)
except:
    pass
