import requests as rq
import re
import os

class Bot:
    def __init__(self):
        self.__token = os.environ['BOT_TOKEN']
        self.__url = os.environ['BOT_URL']
        self.__channel_id=os.environ['CHANNEL_ID']

    def send(self, info):
        
        # sending photo
        self.sendPhoto(info['image_src'])

        # sending message
        self.sendMessage(
            f"""<strong>{info['title']} / {info['year']} / {info['engine']} / {info['milage']}</strong>
<strong>Qiyməti: {info['price']}</strong>
{info['description']}
<a href="{info['url']}">{info['url']}</a>"""
        )

    def sendPhoto(self, photo):
        url = f"{self.__url}{self.__token}/sendPhoto"

        data = {
            "chat_id": self.__channel_id,
            "photo": photo
        }

        r = rq.post(url, data=data)
        if r.status_code != 200:
            raise Exception("Avtomobilin şəkli yüklənə bilmədi")


    def sendMessage(self, text, parse_mode = 'HTML'):
        url = f"{self.__url}{self.__token}/sendMessage"

        data = {
            "chat_id": self.__channel_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": True,
            "disable_notification": True
        }

        r = rq.post(url, data=data)
        if r.status_code != 200:
            raise Exception("Avtomobil elanın mətni yüklənə bilmədi")