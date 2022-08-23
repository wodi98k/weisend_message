import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url= 'http://www.weather.com.cn/weather/101281601.shtml'
res = requests.get(url, headers=headers,timeout=20)
res.encoding = 'utf-8'
#print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
tem_list = soup.find_all('p',class_='tem')  #存温度

day = soup.find('ul',class_='t clearfix')  #存日期
day_list = day.find_all('h1')    
#print(day_list)
wealist = soup.find_all('p',class_='wea') #存天气
day_pre = {}
print(wealist)
print(tem_list)

# for i in range(7):
#     try:
#         temHigh = tem_list[i].span.string    #有时候没有最高温度，用第二天的代替
#     except AttributeError as e:
#         temHigh = tem_list[i+1].span.string
#     temLow = tem_list[i].i.string
#     wea = wealist[i].string
#     day_pre[day_list[i].string] = '最高温度：'+temHigh +' 最低温度：' + temLow + ' 天气：' + wea
# print(day_pre)
