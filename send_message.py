import json
import requests
from access_token import AccessToken
import color
class SendMessage(object):
    # 消息接收者
    TOUSER = 'oa7ig6mLxTgzQxgPuHWRGRJC1TzE'
    # 消息模板id
    TEMPLATE_ID = 'eLFSiiGCHNyZiZUTRKL2SlEUqdMBolkuPm3UuiZ0J-k'
    # 点击跳转链接（可无）
    CLICK_URL = 'https://623920af.cpolar.top/bai.html'

    def __init__(self, touser=TOUSER, template_id=TEMPLATE_ID, click_url=CLICK_URL) -> None:
        """
        构造函数
        :param touser: 消息接收者
        :param template_id: 消息模板id
        :param click_url: 点击跳转链接（可无）
        """
        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id
        self.click_url = click_url

    def get_send_data(self, json_data) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": self.click_url,
            "topcolor": color.color(),
            # json数据对应模板
            "data": {
                "name": {
                    "value": json_data["name"],
                    # 字体颜色
                    "color": color.color()
                },
                "day": {
                    "value": json_data["day"],
                    "color": color.color()
                },
                "weather":{
                    "value":json_data['weather'],
                    "color":color.color()
                },
                'GPS':{
                    "value":json_data['GPS'],
                    "color":color.color()
                },
                "love":{
                    'value':json_data['love_nates'],
                    'color':color.color()

                },
                "eng":{
                    'value':json_data['aiciba'],
                    'color':color.color()
                },
                "love_days":{
                    'value':json_data['love_days'],
                    'color':color.color()
                
                }
                
            }
        }

    def send_message(self, json_data) -> None:
        """
        发送消息
        :param json_data: json数据
        :return:
        """
        # 模板消息请求地址
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()
        # 有关响应结果，我有整理成xml文档（官方全1833条），免费下载：https://download.csdn.net/download/sxdgy_/86263090
        if result["errcode"] == 0:
            print("消息发送成功")
        else:
            print(result)
