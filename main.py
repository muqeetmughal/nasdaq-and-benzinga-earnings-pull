
from requests.api import head
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep, time
import os
import csv
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

class Benzinga:
    def __init__(self):
        
        # next_date =datetime.date.today() + datetime.timedelta(days=1)
        next_date    = datetime.date(2021,7,20) # test purpose only
        print(next_date)
        today_day = next_date.weekday()
        # print(today_day)
        # condition = False
        # if condition:
        if int(today_day) == 5 or int(today_day) == 6:
            print("---------Tommorow is Saturday or Sunday---------\n---------So Skipping---------\n:)")
            pass
        else:
            # try:
                import requests
                response = requests.get(f'https://api.benzinga.com/api/v2.1/calendar/earnings?token=1c2735820e984715bc4081264135cb90&parameters[date_from]={next_date}&parameters[date_to]={next_date}&parameters[tickers]=&pagesize=1000')
                # print(response.text)
                soup = BeautifulSoup(response.text, 'lxml')
                # print(soup.select('item'))
                headers = ['currency', 'date', 'date_confirmed', 'eps', 'eps_est', 'eps_prior', 'eps_surprise', 'eps_surprise_percent', 'eps_type', 'exchange', 'id', 'importance', 'name', 'notes', 'period', 'period_year', 'revenue', 'revenue_est', 'revenue_prior', 'revenue_surprise', 'revenue_surprise_percent', 'revenue_type', 'ticker', 'time', 'updated']
                # with open('complete.txt','a') as file:
                #     file.write(str(soup.select('item')))

                # with open('steps.txt','a') as file:
                # print(len(soup.select('item')[1:2]))
                all_items = soup.select('item')

                for item in all_items:
                    



                # print(headers)

                rows = []
                data_dit = {}

                for item in all_items:

                    for key in headers:

                        data_dit[key] = item.select_one(key).text
                        
                        print(data_dit,'\n')
                        # import time
                        # time.sleep(0.01)
                        print(key,item.select_one(key).text)
                    rows.append(data_dit)

                print(headers)




                # print(rows)

                output = json.dumps(rows)
                with open('complete.json','w') as file:
                    file.write(str(output))

                # csv_columns = headers

                # csv_file = f"data/Benzinga_Earnings_{next_date}.csv"
                # try:
                #     os.mkdir("data")
                # except FileExistsError:
                #     pass
                # try:
                #     with open(csv_file, 'w', newline='') as csvfile:
                #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                #         writer.writeheader()
                #         # print(dict_data)
                #         for data in rows:
                #             writer.writerow(data)
                # except IOError:
                #     print("I/O error")
            # except:
            #     print("An Error Occured")
            #     pass
            
bot = Benzinga()