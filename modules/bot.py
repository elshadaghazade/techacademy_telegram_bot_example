import requests as rq
import re
import os

class Bot:
    def __init__(self, info):
        self.__info = info
        self.__url = f"{os.environ['BOT_URL']}{os.environ['BOT_TOKEN']}"
        self.__channel_id=os.environ['CHANNEL_ID']

    def send(self):
        # sending photo
        self.sendPhoto()
        # sending message
        self.sendMessage()

    def sendPhoto(self):
        url = self.__url + "/sendPhoto"

        data = {
            "chat_id": self.__channel_id,
            "photo": self.__info['image_src'],
            "disable_notification": True
        }

        print(data)

        r = rq.post(url, data=data)
        if r.status_code != 200:
            raise Exception("Avtomobilin şəkli yüklənə bilmədi")


    def sendMessage(self):
        url = self.__url + "/sendMessage"
        text = f"""<strong>{self.__info['title']} / {self.__info['year']} / {self.__info['engine']} / {self.__info['mileage']}</strong>
<strong>Qiyməti: {self.__info['price']}</strong>
{self.__info['description']}
<a href="{self.__info['url']}">{self.__info['url']}</a>"""

        data = {
            "chat_id": self.__channel_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
            "disable_notification": True
        }

        r = rq.post(url, data=data)
        if r.status_code != 200:
            raise Exception("Avtomobil elanın mətni yüklənə bilmədi")