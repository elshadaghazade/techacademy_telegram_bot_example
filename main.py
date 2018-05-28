import os
import re
import inquirer
from dotenv import load_dotenv
load_dotenv()

from modules.crawler import Crawler
from modules.bot import Bot

def prompt():
    
    questions = [
        inquirer.Text(name="ads_id", message="Elanın İD nömrəsini yazın", validate=lambda _, x: str(x).isnumeric())
    ]
    answers = inquirer.prompt(questions)
    
    try:
        crawler = Crawler(answers['ads_id'])
        info = crawler.get_info()
        bot = Bot(info)
        bot.send()
    except Exception as err:
        print(err)
    

if __name__ == '__main__':
    prompt()