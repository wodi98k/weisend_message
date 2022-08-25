import requests
import json
import random
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }
def love_notes():
    notes = [
        "大猪起床啦","天天当懒狗,程序都比你积极啦",
        '起床！起床！起床',
        '爱你爱你,希望今天不会吵架',
        '地球爆炸啦,快跑啦',
        '今天不努力,明天变垃圾',
        '我在深圳很想你',
        '晚起毁上午，早起傻一天，所以还是不起为妙。',
        '不起床的猪'
    ]
    return random.choice(notes)
def aiciba():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url,headers=headers)
    note_en = r.json()["content"]
    note_ch = r.json()["note"]
    return note_ch + note_en
