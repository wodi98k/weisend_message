import requests
from bs4 import BeautifulSoup
import datetime
import re
def info():
    weather_list=[]
    url = "http://www.weather.com.cn/weather1d/101281601.shtml"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    } 
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    data = res.text
    soup = BeautifulSoup(data,'lxml')
    tem = soup.find_all('p',class_='tem')
    weather_list.append(tem)
    for  say in weather_list:
        say = str(say)
        htmlstr=re.sub(pattern='<(.|\n)+?>',repl='',string=say)
        tems = re.findall(pattern='\s(-?\d+\.?/?\d*%?)',string=htmlstr)
        return tems[1]+"/" +tems[0]+"°C"
def day():
    today = datetime.datetime.now().strftime('%Y-%m-%d ')
    week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    return today + week_list[datetime.datetime.today().weekday()]
