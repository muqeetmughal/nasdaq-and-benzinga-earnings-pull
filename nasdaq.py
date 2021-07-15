
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

import datetime
import json
import csv

class Nasdaq:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe',options=options)
        next_date =datetime.date.today() + datetime.timedelta(days=1)
        # print(next_date)


        # next_date    = datetime.date(2021,7,25) # test purpose only

        today_day = next_date.weekday()

        if int(today_day) == 5 or int(today_day) == 6:
            print("Date is Saturday or Sunday So Skipping")
        else:
            url = f'https://api.nasdaq.com/api/calendar/earnings?date={next_date}'

            self.driver.get(url)
            content = self.driver.page_source
            soup = BeautifulSoup(content, 'html.parser')
            pre_tag = soup.select('pre')[0].text
            # print(pre_tag)

            data = json.loads(pre_tag)
            headers = data['data']['headers']
            rows = data['data']['rows']


            print(list(headers.keys()))
            

            # with open('test.json','w') as file:
            #     file.write(str(json.dumps(rows)))


            self.driver.quit()
bot = Nasdaq()