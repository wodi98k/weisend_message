import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import os
import sys
username = sys.argv[1]
password = sys.argv[2]
url = "https://www.ctfer.vip/user/login?redirect=/index"
def login():
    wait = ui.WebDriverWait(driver,15)
    driver.get(url=url)
    time.sleep(3)
    #wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div[2]/form/div[1]/div/div/div/input"))
    driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(username)
    driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div[2]/form/div[2]/div/div/div/input').send_keys(password)
def get_track(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+(1/2)at²
    ③v²-v0²=2as
    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    '''
    # 初速度
    v=0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t=0.1
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks=[]
    # 当前的位移
    current=0
    # 到达mid值开始减速
    mid=distance * 4/5

    distance += 10  # 先滑过一点，最后再反着滑动回来

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = 2  # 加速运动
        else:
            a = -3 # 减速运动

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0*t+0.5*a*(t**2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))
        # 速度已经达到v,该速度作为下次的初速度
        v= v0+a*t
    # 反着滑动到大概准确位置
    for i in range(3):
       tracks.append(-2)
    for i in range(4):
       tracks.append(-1)
    return tracks

def move_to_gap(tracks):
    need_move_span = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div[2]/form/div[3]/div/div/div/div[3]')
    ActionChains(driver).click_and_hold(need_move_span).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
    time.sleep(1)
    ActionChains(driver).release().perform()
    get_register()
def get_register():
    driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div[2]/form/div[4]/div/div/div[2]/button").click()
    time.sleep(5)
    driver.find_element_by_css_selector('#app > section > header > ul > li.el-menu-item-group > ul > div:nth-child(5)').click()
    print("NSSCTF签到成功")
if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
    login()
    move_to_gap(get_track(300))





