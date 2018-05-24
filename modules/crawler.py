import requests as rq
from lxml import html
import os

class Crawler:
    def __init__(self, ads_id):
        try:
            self.ads_id = int(ads_id)
        except Exception as err:
            print("Crawler error at line 9:", err)
            exit()
    
    def get_info (self):
        r = rq.get(f"{os.environ['ADS_BASE_URL']}/car/{self.ads_id}")
        
        if r.status_code != 200:
            raise Exception("Elan tapılmadı")

        dom = html.fromstring(r.content)
        
        # finding price
        price = dom.xpath('//div[@class="eln_price"]//b/text()')[0]

        # finding image url
        image_src = dom.xpath('//meta[@property="og:image"]/@content')[0]
        
        # finding ads description
        descr = "\n".join(dom.xpath('//div[@class="eln_desc"]/text()'))

        # finding title
        title = dom.xpath('//title/text()')[0].split(" - ")[0]


        # finding year
        year = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(),"Buraxılış ili")]/following-sibling::td[1]//b/text()')[0]

        # finding milage
        milage = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(), "Yürüş")]/following-sibling::td[1]//b/text()')[0]

        # finding engine
        engine = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(),"Mühərrik")]/following-sibling::td[1]//text()')[0]

        return {
            "url": r.url,
            "description": descr,
            "image_src": image_src,
            "price": price,
            "title": title,
            "year": year,
            "milage": milage,
            "engine": engine
        }