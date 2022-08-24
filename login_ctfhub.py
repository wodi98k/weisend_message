import time
import ddddocr
from PIL import Image
#http请求模块
from selenium import webdriver
#  pip install webdriver_manager 
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
username = sys.argv[0]
password = sys.argv[1]
def get_captcha():
        url = "https://www.ctfhub.com/#/user/login"
        driver.get(url=url)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="formLogin"]/div[1]/div[3]/div/div[4]/div[2]/img').click()
        time.sleep(2)
        f = driver.find_element_by_class_name('getCaptcha')
        f.screenshot('code.png')
        image = Image.open('code.png')
        image =image.convert('L')
        count = 160
        table = []
        for  i in  range(256):
                if i <count:
                        table.append(1)
                else:
                        table.append(0) 
        image = image.point(table,'1')
        image.save('captcha.png')
def discern_captcha():
        ocr = ddddocr.DdddOcr()
        def get_file_read(file_name):
                with open(file_name,'rb') as f:
                        return f.read()
        image_name = get_file_read('captcha.png')
        return ocr.classification(image_name)
def login(captcha):
                driver.find_element_by_id("account").send_keys(username)
                driver.find_element_by_id('password').send_keys(password)
                driver.find_element_by_id('imgCaptcha').send_keys(captcha)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
                time.sleep(2)

def get_submit():
        try:
                driver.maximize_window()
                driver.refresh()
                time.sleep(2)
                move = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[2]/span[2]')
                ActionChains(driver).move_to_element(move).perform()#将鼠标悬停在个人名称上，唤出二级菜单
                driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[1]').click()#点击签到
                print('签到成功')
        except:
                pass        
if __name__=="__main__":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chromedriver = "/usr/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        get_captcha()
        driver.maximize_window()
        captcha = discern_captcha()
        login(captcha=captcha)
        get_submit()
