from operator import ge
import requests
import json
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }
def love_notes():
    
    url = "https://api.lovelive.tools/api/SweetNothings/Serialization/Json"
    r = requests.get(url=url,headers=headers)
    data = json.loads(r.text)
    return data['returnObj'][0]
def aiciba():
    url = "http://open.iciba.com/dsapi/"
 
    r = requests.get(url,headers=headers)
    note_en = r.json()["content"]
    note_ch = r.json()["note"]
    return note_ch + note_en

