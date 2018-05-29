# -*- coding: utf-8 -*-

from urllib.parse import urljoin
import requests
import csv
import time
from bs4 import BeautifulSoup
# http://sh.58.com/zhangjiang/zufang/?PGTID=0d3090a7-0184-fa2e-0dec-edb12d812c1e&ClickID=2
url = "http://sh.58.com/zhangjiang/zufang/pn{page}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"}
page = 1
csv_file = open("house3.csv","a+")
csv_writer = csv.writer(csv_file, delimiter=',')
print("page 1")
print(page)
while True:
    html = requests.get(url.format(page=page), headers = headers)
    soup = BeautifulSoup(html.text, 'lxml')
    nextpage = soup.select('#bottom_ad_li > div.pager > a.next')
    if not nextpage:
        break
    house_list = soup.select("body > div.mainbox > div.main > div.content > div.listBox > ul > li")
    for house in house_list:
        try:
            if house.select("div.des > h2 > a") and house.select("div.listliright > div.money > b") and house.select("div.des > p.add > a") :
                house_title = house.select("div.des > h2 > a")[0].get_text().strip()
                house_url = house.select("div.des > h2 > a")[0].get('href')
                house_price = house.select("div.listliright > div.money > b")[0].get_text().strip()
                house_location = house.select("div.des > p.add > a")[0].get_text().strip()
                print(house_title)
                print(house_url)
                print(house_price)
                print(house_location)
                csv_writer.writerow([house_title, house_url, house_price, house_location])
        except Exception as e:
            csv_file.close()
            print(e)
    # time.sleep(5)
    page += 1
    print("page 2")
    print(page)

csv_file.close()
