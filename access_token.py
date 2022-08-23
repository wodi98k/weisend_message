import requests


class AccessToken(object):
    # 微信公众测试号账号（填写自己的）
    APPID = "wx9ebe9148696d5d1a"
    # 微信公众测试号密钥（填写自己的）
    APPSECRET = "dbe430006b73506470c8b49e9347826f"

    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:
        """
        获取access_token凭证
        :return: access_token
        """
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
            
        else:
            print(result)