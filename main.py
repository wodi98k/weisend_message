from send_message import SendMessage
import weather
import love_notes
import brithday
import Birthday
class Main(object):
    def __init__(self) -> None:
        """
        构造函数
        """
        pass

    def main(self) -> None:
        # 实例SendMessage
        sm = SendMessage()
        # 获取接口返回数据
        json_data = {"name": "老婆", 
        "day": weather.day(),
        "weather":weather.info(),
        "GPS":"东莞",
        'love_nates':love_notes.love_notes(),
        'aiciba':love_notes.aiciba(),
        'love_days':Birthday.love_day(),
        'briaty_day':Birthday.birthday(),
        'face_day':Birthday.face_day(),
        }
        # 发送消息
        sm.send_message(json_data=json_data)


if __name__ == '__main__':
    main = Main()
    main.main()
