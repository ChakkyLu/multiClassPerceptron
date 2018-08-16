import os
import ssl
import time
import urllib
from bs4 import BeautifulSoup


district = ["足立区", "荒川区","板橋区","江戸川区","大田区","葛飾区","北区","江東区","品川区","渋谷区","新宿区","杉並区","墨田区","世田谷区","台東区","中央区","千代田区",
            "豊島区","中野区","練馬区","文京区","港区","目黒区"]
district_dict = gen_disctict(district)
house_dict = {"ワンルーム":0, "1K":1, '1DK':2, '1LDK': 3, '2K':4, '2DK':5, '2LDK':6, '3K': 7, '3DK':8, '3LDK':9, '4K':10, '4DK':11, '4LDK':12}


def gen_disctict(district):
    dict = {}
    k = 0
    for i in district:
        dict[i] = k
        k += 1
    return dict


def get_floor(floor_str):
    total_floor = ""
    this_floor = ""
    if ' / ' not in floor_str:
        return None
    else:
        floor_ = floor_str.split(' / ')
    if len(floor_)!=2:
        return None
    else:
        for s in floor_[0]:
            if s.isdigit():
                total_floor += s
        for s in floor_[1]:
            if s.isdigit():
                this_floor += s
    return total_floor, this_floor


def scrape(url, house):
    fw = open("house.csv", 'a+')
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    page_info = urllib.request.urlopen(req).read()
    html = page_info.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    for objectBox in soup.find_all('div',class_='object boxHover'):
        record = True
        desc1 = objectBox.find_all('span', class_="desc1")
        desc2 = objectBox.find_all('span', class_="desc2")
        price = desc1[1].find_all('span', class_='num')[0].string.strip(',')
        while ',' in price:
            price = price[0:price.index(',')] + price[price.index(',')+1:]

        architecture = desc1[3].string
        size = desc2[2].string.split('m')[0]
        size = str(int(float(size)))
        if architecture in house_dict:
            architecture = str(house_dict[architecture]+1)
        else:
            if int(size) < 30: record = False
            else:
                architecture = '14'
        station_ = objectBox.find_all('li', class_="object-info_txt info-time")[0].string
        if '-' not in station_: station_ = station_[:-1]
        location = desc2[0].string
        floor = desc2[1].string

        age = desc2[-1].get_text().strip()
        age = age.split(' （')
        age = age[0][0:4]
        age = str(2018 - int(age))
        # print(location+','+floor+','+size+','+price+","+architecture+','+station_+','+age+"\r\n")
        if '区' in location and record:
            location = location.split('区')[0]
            location+= '区'
            if location in district_dict and get_floor(floor)!=None:
                location = str(district_dict[location])
                total_floor, this_floor = get_floor(floor)
                if [location, total_floor, this_floor, size, architecture, price, station_, age] not in house:
                    house.append([location, total_floor, this_floor, size, architecture, price, station_, age])
                    fw.write(location+','+total_floor+','+ this_floor+','+size+','+architecture+","+price+','+station_+','+age+"\r\n")
                print(location+','+total_floor+','+ this_floor+','+size+','+architecture+","+price+','+station_+','+age+"\r\n")
        return house
    fw.close()

for i in range(1, 940):
    url = "https://www.athome.co.jp/mansion/chuko/tokyo/list/page"+str(i+1)
    h = 0
    while(h==0):
        try:
            if i==1:
                house = []
                scrape(url, house)
            else:
                scrape(url, house)
            h = 1
        except Exception:
            time.sleep(0.01)
    print(house)






