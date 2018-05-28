import requests as rq
from lxml import html
import os

class Crawler:
    def __init__(self, ads_id):
        try:
            self.ads_id = int(ads_id)
        except Exception as err:
            raise("Elanin ID nomresi sehvdir")
    
    def get_info (self):
        r = rq.get(f"{os.environ['ADS_BASE_URL']}/car/{self.ads_id}")
        
        if r.status_code != 200:
            r.raise_for_status()

        dom = html.fromstring(r.content)
        
        # finding price
        price = dom.xpath('//div[@class="eln_price"]//b/text()')
        price = price[0] if price else None

        # finding image url
        image_src = dom.xpath('//meta[@property="og:image"]/@content')
        image_src = image_src[0] if image_src else None
        
        # finding ads description
        descr = dom.xpath('//div[@class="eln_desc"]/text()')
        descr = "\n".join(descr) if descr else None

        # finding title
        title = dom.xpath('//title/text()')
        title = title[0].split(" - ")[0] if title else None


        # finding year
        year = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(),"Buraxılış ili")]/following-sibling::td[1]//b/text()')
        year = year[0] if year else None

        # finding milage
        mileage = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(), "Yürüş")]/following-sibling::td[1]//b/text()')
        mileage = mileage[0] if mileage else None

        # finding engine
        engine = dom.xpath('//div[@class="eln_right"]//table//td[contains(text(),"Mühərrik")]/following-sibling::td[1]//text()')
        engine = engine[0] if engine else None

        return {
            "url": r.url,
            "description": descr,
            "image_src": image_src,
            "price": price,
            "title": title,
            "year": year,
            "mileage": mileage,
            "engine": engine
        }