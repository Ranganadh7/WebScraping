import csv
import os
import random
import time
from scrapy.http import HtmlResponse
import pandas as pd
import requests
from lxml import html
import json
import re
import pandas as pd
import numpy as np
from datetime import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
products_df = pd.DataFrame()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
def fetch_proxy():
    p1 = ['104.218.195.130','104.218.195.205','104.251.82.191','104.251.82.240','104.251.82.63','104.251.84.104','104.251.84.217','104.251.84.232','104.251.85.123','104.251.85.196','104.251.86.162','104.251.86.167','104.251.86.209','104.251.90.200','104.251.90.237','104.251.90.69','104.251.91.154','104.251.91.233','104.251.92.178','104.251.92.234','104.251.92.63','108.177.131.182','108.177.131.25','146.19.55.151','146.19.55.167','154.13.200.241','154.13.200.34','154.13.200.48','154.13.201.156','154.13.201.245','154.13.202.117','154.13.202.128','154.13.202.146','154.13.203.144','154.13.203.212','154.13.204.132','154.13.204.98','154.13.205.173','154.13.205.40','154.13.206.167','154.13.206.181','154.13.207.213','154.13.207.233','154.13.244.123','154.13.244.139','154.13.244.234','154.13.245.128','154.13.245.133','154.13.245.152','154.13.246.157','154.13.246.158','154.13.246.159','154.13.247.187','154.13.247.219','154.13.247.42','154.13.248.163','154.13.248.36','154.13.248.95','154.13.249.100','154.13.249.42','154.13.250.164','154.13.250.89','154.13.251.141','154.13.251.52','154.13.251.76','154.13.252.114','154.13.252.163','154.13.252.79','154.13.253.101','154.13.253.185','154.13.253.195','154.13.254.141','154.13.254.99','154.13.255.222','154.13.255.248','154.17.157.182','154.17.157.234','154.17.157.50','154.17.188.153','154.17.188.24','154.17.189.230','154.17.189.30','154.29.2.16','154.29.2.196','154.29.2.231','154.37.72.173','154.37.72.59','154.37.76.117','154.37.76.137','154.37.76.187','158.115.224.142','158.115.224.246','158.115.225.241','158.115.225.253','158.115.226.137','158.115.226.92','158.115.227.120','158.115.227.174','165.140.224.123','165.140.224.184','165.140.225.115','165.140.225.230','165.140.225.46','165.140.226.14','165.140.226.244','165.140.226.46','165.140.227.12','165.140.227.245','168.91.64.213','168.91.64.234','168.91.64.251','168.91.65.46','168.91.65.73','168.91.66.106','168.91.66.123','168.91.67.109','168.91.67.17','168.91.84.133','168.91.84.59','168.91.85.212','168.91.85.30','168.91.86.14','168.91.86.21','168.91.87.79','168.91.87.97','168.91.88.214','168.91.88.245','168.91.90.127','168.91.90.49','172.255.93.114','172.255.93.130','172.255.94.155','172.255.94.158','173.208.27.32','173.208.27.93','173.208.28.162','173.208.28.246','173.234.244.244','173.234.244.79','173.245.75.175','173.245.75.54','173.245.85.105','173.245.85.116','173.245.85.45','173.245.90.138','173.245.90.224','185.255.196.162','185.255.196.168','185.255.197.105','185.255.197.110','198.251.92.13','198.251.92.237','198.251.92.29','198.251.93.165','198.251.93.227','198.251.93.237','207.230.104.136','207.230.104.195','207.230.104.90','207.230.105.118','207.230.105.205','207.230.105.84','207.230.106.19','207.230.106.198','207.230.106.204','207.230.107.92','207.230.107.95','213.109.148.122','213.109.148.23','23.105.0.165','23.105.0.224','23.105.0.63','23.105.142.171','23.105.142.57','23.105.143.213','23.105.143.73','23.105.144.123','23.105.144.96','23.105.145.215','23.105.145.242','23.105.146.181','23.105.146.245','23.105.147.152','23.105.147.192','23.105.147.203','23.105.150.11','23.105.150.199','23.105.151.138','23.105.151.3','23.105.3.42','23.105.3.68','23.105.4.172','23.105.4.231','23.106.16.106','23.106.16.203','23.106.18.234','23.106.18.44','23.106.20.181','23.106.20.233','23.106.22.125','23.106.22.147','23.106.24.173','23.106.24.41','23.106.26.65','23.106.26.84','23.106.27.13','23.106.27.139','23.106.27.144','23.106.28.230','23.106.28.237','23.106.30.117','23.106.30.126','23.110.166.102','23.110.166.26','23.110.166.76','23.110.169.100','23.110.169.162','23.110.173.171','23.110.173.225','23.129.136.120','23.129.136.245','23.129.40.19','23.129.40.44','23.129.40.76','23.129.56.191','23.129.56.237','23.161.3.146','23.161.3.67','23.170.144.104','23.170.144.108','23.170.144.19','23.170.145.103','23.170.145.252','23.170.145.51','23.175.176.21','23.175.176.24','23.175.177.176','23.175.177.183','23.175.177.8','23.176.49.110','23.176.49.183','23.177.240.144','23.177.240.217','23.177.240.90','23.184.144.105','23.184.144.124','23.184.144.231','23.185.112.167','23.185.112.229','23.185.144.110','23.185.144.171','23.185.144.197','23.185.80.164','23.185.80.4','23.185.80.6','23.186.48.210','23.186.48.248','23.226.16.211','23.226.16.243','23.226.17.178','23.226.17.240','23.226.18.106','23.226.18.193','23.226.19.212','23.226.19.87','23.226.20.187','23.226.20.90','23.226.21.13','23.226.21.22','23.226.22.216','23.226.22.53','23.226.23.178','23.226.23.250','23.226.24.190','23.226.24.6','23.226.24.64','23.226.25.107','23.226.25.68','23.226.26.158','23.226.26.202','23.226.26.220','23.226.27.246','23.226.27.94','23.226.28.159','23.226.28.194','23.226.28.231','23.226.29.126','23.226.29.99','23.226.30.191','23.226.30.235','23.226.31.131','23.226.31.169','23.226.31.193','23.247.172.197','23.247.172.214','23.247.172.51','23.247.173.202','23.247.173.6','23.247.174.196','23.247.174.211','23.247.174.81','23.247.175.156','23.247.175.215','23.247.175.218','23.27.9.103','23.27.9.228','23.82.105.11','23.82.105.194','23.82.105.45','23.82.109.165','23.82.109.242','23.82.184.118','23.82.184.227','23.82.184.80','23.82.186.178','23.82.186.223','23.82.40.136','23.82.40.202','23.82.40.42','23.82.41.119','23.82.41.40','23.82.41.6','23.82.44.209','23.82.44.48','23.82.80.145','23.82.80.68','23.82.81.171','23.82.81.79','45.146.117.234','45.146.117.253','45.146.118.204','45.146.118.228','45.146.119.223','45.146.119.244','45.154.141.33','45.154.141.50','45.154.142.21','45.154.142.231','45.154.142.42','45.224.228.187','45.224.228.87','45.224.228.94','45.224.230.211','45.224.230.228','45.224.231.141','45.224.231.68','45.237.84.117','45.237.84.33','45.237.86.170','45.237.86.178','45.238.157.141','45.238.157.198','45.238.157.225','45.238.159.115','45.238.159.59','45.238.159.8','45.59.128.144','45.59.128.198','45.59.128.236','45.59.129.177','45.59.129.217','45.59.130.16','45.59.130.218','45.59.131.107','45.59.131.140','45.59.131.209','45.59.180.245','45.59.180.58','45.59.181.38','45.59.181.71','45.59.181.80','45.59.182.209','45.59.182.217','45.59.183.171','45.59.183.214','45.59.183.67','45.71.19.128','45.71.19.159','52.128.0.45','52.128.0.98','52.128.1.105','52.128.1.124','52.128.10.164','52.128.10.20','52.128.11.123','52.128.11.71','52.128.12.46','52.128.12.70','52.128.13.125','52.128.13.207','52.128.14.107','52.128.14.115','52.128.14.30','52.128.15.114','52.128.15.92','52.128.196.173','52.128.196.240','52.128.196.70','52.128.197.105','52.128.197.17','52.128.198.105','52.128.198.72','52.128.198.76','52.128.199.206','52.128.199.237','52.128.2.17','52.128.2.58','52.128.200.127','52.128.200.182','52.128.200.79','52.128.201.194','52.128.201.3','52.128.201.56','52.128.202.108','52.128.202.189','52.128.202.242','52.128.203.21','52.128.203.230','52.128.204.144','52.128.204.91','52.128.205.148','52.128.205.204','52.128.206.110','52.128.206.219','52.128.206.96','52.128.207.116','52.128.207.237','52.128.208.176','52.128.208.60','52.128.209.109','52.128.209.120','52.128.210.159','52.128.210.80','52.128.211.121','52.128.211.155','52.128.216.224','52.128.216.41','52.128.217.208','52.128.217.87','52.128.218.165','52.128.218.65','52.128.219.165','52.128.219.177','52.128.219.44','52.128.220.40','52.128.220.48','52.128.221.181','52.128.221.230','52.128.222.161','52.128.222.38','52.128.223.201','52.128.223.219','52.128.3.86','52.128.3.90','52.128.4.106','52.128.4.227','52.128.5.35','52.128.5.52','52.128.6.111','52.128.6.149','52.128.6.93','52.128.7.247','52.128.7.81','52.128.8.195','52.128.8.33','52.128.9.12','52.128.9.177','62.3.61.119','62.3.61.2','62.3.61.40','88.218.172.175','88.218.172.203','88.218.172.83','88.218.173.65','88.218.173.94','88.218.173.98','88.218.174.16','88.218.174.44','88.218.175.235','88.218.175.5','88.218.175.57','95.164.224.233','95.164.224.38','95.164.225.124','95.164.225.21','95.164.226.220','95.164.226.221','95.164.226.7','95.164.227.152','95.164.227.199','95.164.227.206','95.164.236.212','95.164.236.249','95.164.236.58','95.164.237.111','95.164.237.251','95.164.238.183','95.164.238.206','95.164.239.113','95.164.239.253']
    p_auth = str("csimonra:h19VA2xZ")
    p_host = random.choice(p1)
    p_port = "29842"
    proxy = {
        'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
        'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
    }
    return proxy

def join_string(list_string):
    # Join the string based on '-' delimiter
    string = ' > '.join(list_string)
    return string

def join_string1(list_string):
    # Join the string based on '-' delimiter
    string = ' | '.join(list_string)

    return string

def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def join_string2(list_string):
    # Join the string based on '-' delimiter
    string = ': '.join(list_string)

    return string

# def create_csv(data1):
#
#     self.products_df =products_df.append(data1)
#     products_df.to_csv('ASOS_UK_sku_data3.csv', encoding='utf-8-sig', index=False)

def ASOS_UK_SKU(df):
    counter=1
    data_list=[]
    c = 1
    products_df = pd.DataFrame()
    for sku,site,country,url in zip(df['SKU_ID'],df['Website'],df['Country'],df['PDP URL']):
        SKU_ID=sku
        Website=site
        Country=country
        Product_url=url
        headers = {
            'Cookie': 'geocountry=IN; bm_sz=6D41114D75AD06A70C10865FCE1503EA~YAAQNMYcuDTXG+Z+AQAA5eXjAA64bRGfu58OlA8NvhONrW8p8JfqX6chFhcwsg5dDoJs842Gpom50KGYs6OdoLOf0W31FldWhiIsQSI/C2PZZw8Up2v3ig3GoKWS9jFExhOuflhyA8isfsverUEyTTvg4VZk5P733oc8y0tugYLKVHInagieIW0iKitWqLcYwo6YNik5IDgYoCPQ/wY+JV9R0iF3cIoHmfp3D4Pv+NwtDP4lE1CNcJoxMJ2FY//sXtAXGcunnHsMUlWxPqLbn1B1ugOyXSjPsaFn+GAxb2Td~3163461~4339256; siteChromeVersion=au=11&com=11&de=11&dk=11&es=11&fr=11&it=11&nl=11&pl=11&roe=11&row=11&ru=11&se=11&us=11; keyStoreDataversion=hgk0y12-29; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; browseCurrency=GBP; browseSizeSchema=UK; currency=1; featuresId=cfd228aa-8a79-4434-984e-d40f4e279d47; asos-b-sdv629=hgk0y12-29; ak_bmsc=ED1CF393FD9F133D451BA8B54E47BC04~000000000000000000000000000000~YAAQNMYcuFzXG+Z+AQAAev/jAA5aJKVenMWeP2VUqk4DKp4yxnEZbEhfNFq56IR1z8Y5k5/xgdCQlNyAzSaJVDESp4Asg+WDUn+LDoO/y4ckIhDvZgwZ+LDAIapnWqxQDA+0zNHCqfrre5kvhsQMXiJ6X12hW0VWmPoAWlGlONqkwkMyDf3T4ep+jFtjh71/MuopL4gUgXOC4/f39muZ89nMwK7urCm7lkY4yWdK0nmMPAvUTvRksvnSRFbbOjoSxz6UMqgQIDTt3Vlx9El68yryOmIdv9mFTXijMMGH6oVosz6cj0EKcYu109Sct0o4eoM4NGKics/Uu2E2yjx9//K/+3JCK+P87hYJCY6lQjfHTS6bVP7DCCPscg==; optimizelyEndUserId=oeu1644987426337r0.48545337035332126; s_ecid=MCMID%7C83688196826904108272576498552548238375; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C83688196826904108272576498552548238375%7CMCAAMLH-1645592224%7C6%7CMCAAMB-1645592224%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1644994624s%7CNONE%7CvVersion%7C3.3.0%7CMCAID%7CNONE; _s_fpv=true; s_cc=true; asos-perx=7300f8adbc344732b31d0a546d186518||f14ea9b1e3c441be99747b80532e263c; bt_recUser=0; _cs_c=0; btpdb.ydg7T9K.dGZjLjc0OTQ1OTE=U0VTU0lPTg; _gid=GA1.2.220924119.1644987431; _gcl_au=1.1.329702633.1644987433; s_sq=%5B%5BB%5D%5D; browseCountry=GB; storeCode=COM; browseLanguage=en-GB; stc-welcome-message=resolvedDeliveryCountry=IN; studentModalShown=true; s_pers=%20s_vnum%3D1646073000150%2526vn%253D1%7C1646073000150%3B%20s_invisit%3Dtrue%7C1644989618392%3B%20s_nr%3D1644987818397-New%7C1676523818397%3B%20gpv_p10%3Ddesktop%2520com%257Cproduct%257Cadidas%2520Outdoor%2520Primegreen%2520puffer%2520jacket%2520with%2520hood%2520and%2520three%2520stripes%2520in%2520navy%2520%257C%2520ASOS%7C1644989618402%3B%20gpv_p6%3D%2520%7C1644989618409%3B%20gpv_e47%3Dsearch%257Cadidas%7C1644989618414%3B; floor=1001; asos=PreferredSite=&currencyid=1&currencylabel=GBP&customerguid=7300f8adbc344732b31d0a546d186518&topcatid=1001; OptanonConsent=isIABGlobal=false&datestamp=Wed+Feb+16+2022+10%3A33%3A40+GMT%2B0530+(India+Standard+Time)&version=6.25.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _abck=9C35315F3EA8943658A2F621808A4122~0~YAAQRq1NaBoAwdV+AQAAmAbqAAc6x3j+1eeVIavq8BEAcSy/NWS5CZdQgt8uqP3lFCcHcyx1S+XAwuMRox4BmfN8ahczOZEAMbPilyOZHQkl/IYIqTtpeGUjJZNoQfrNiHde/9ssG7Xk0ICsX+JIbjVRlaELJkBj8GaAfBfa8gntQxGz9l/5a6GpP6TwtV9sNk7zt0engP9vUZ6qQ2dGU84TrKA0x8yTTD5fKtX8QNqVjGcQiOsqC3gW/O74p+JrIZzwjPfwWKTs6bGghUHmpqfKbvN9uLMG43SNME9vFWULIUihWVZgvTFSjOFEYiJn0yACOHTtftc2VfnE+tOOXfyesdTFOmwX3Ip0vJLiM5vh2BWO2bDl2M6D4l9LaBRGx4DKT/adw+DZj82+yPTtbrJvafL+xw==~-1~-1~-1; _cs_id=8c1ce34c-87c0-a6e6-af40-a1d16d4b1f96.1644987429.1.1644987821.1644987429.1628755191.1679151429788; _cs_s=3.0.0.1644989621988; _ga_54TNE49WS4=GS1.1.1644987432.1.1.1644987822.60; _ga=GA1.1.1297817281.1644987431; _ga_1JR0QCFRSY=GS1.1.1644987432.1.1.1644987822.0; fita.sid.asos=o-BPx4-nu_VnltpHiTBUfsbbVUQkdG5i; RT="z=1&dm=asos.com&si=4e30b0e7-790f-428f-b2dc-8a2edc654815&ss=kzp31aqq&sl=8&tt=iwz&bcn=%2F%2F684dd330.akstat.io%2F&ul=c4vo"',
            'Referer': f'{Product_url}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        for i in range(1,15):
            proxy = fetch_proxy()
            try:
                response = requests.get(url=Product_url, headers=headers, proxies=proxy,timeout=30)
                response123 = HtmlResponse(url=Product_url, body=response.content)
                # time.sleep(2)
                if response.status_code == 200:
                    tree = html.fromstring(response.content)
                    #RPC
                    try:
                        RPC=tree.xpath('//div[@class="product-code"]/p/text()')
                        RPC=listToString(RPC)
                    except Exception as e:
                        RPC =''
                    if RPC =='':
                        RPC=Product_url.split('?clr=')[0].split('/')[-1]
                    # product_name
                    product_name = tree.xpath('//div[@id="aside-content"]/div[@class="product-hero"]/h1/text()')
                    if product_name==[]:
                        product_name=tree.xpath('//h1/text()')
                    product_name = listToString(product_name)
                    # product url
                    product_url = response.url
                    # brand
                    Brand = product_url.split('/')
                    Brand = Brand[4]
                    # product_id
                    product_id = tree.xpath('//div[@class="col"]/div[@class="product-code"]/p/text()')
                    product_id = listToString(product_id)
                    if product_id=='':
                        product_id=Product_url.split('?clr=')[0].split('/')[-1]
                    # category path
                    category_path1 = tree.xpath('//div[@id="chrome-breadcrumb"]/div/nav/ol/li/a/text()')
                    # category_path1 = category_path1[0]
                    category_path2 = 'Search results for ' + product_id
                    # category_path1.append(category_path2)
                    category_path1.append(product_name)
                    category_path = join_string(category_path1)

                    # list price, promo price, discount
                    # try:
                    stock_url = re.findall(r'window.asos.pdp.config.stockPriceApiUrl = \'(.*?)\';', response.text)
                    stock_url = stock_url[0]
                    url1 = 'https://www.asos.com' + stock_url
                    for sp in range(1,5):
                        proxy2=fetch_proxy()
                        response1 = requests.get(url = url1, headers = headers,proxies=proxy2,timeout=30)
                        if response1.status_code==200:
                            price = response1.json()
                            price = price[0]

                            discount = int(price['discountPercentage'])
                            if discount == 0:
                                promo_price = price['productPrice']['current']['value']
                                list_price = promo_price
                                discount = '-'
                            else:
                                promo_price = price['productPrice']['current']['value']
                                list_price = price['productPrice']['rrp']['value']
                                if list_price == None:
                                    list_price = price['productPrice']['previous']['value']
                            break
                        else:
                            print('trying again for stock_url.....')
                    # except Exception as e:
                    #     promo_price = '-'
                    #     list_price = '-'
                    #     discount = '-'
                    #     print(e)
                    try:
                        # variant
                        list1 = re.findall(
                            r'"variantId":(.*?),"size":"(.*?)","isInStock":(.*?),"sizeId":(.*?),"colour":"(.*?)"',
                            response.text)

                        variant_list = []
                        stock_condition = []
                        variant_id = []
                        for i in range(len(list1)):
                            variant_id.append(list1[i][0])
                            variant_list.append(list1[i][1])
                            stock_condition.append(list1[i][2])

                        stock_condition_final = []
                        for i in stock_condition:
                            if i == 'true':
                                stock_condition_final.append('In Stock')
                            else:
                                stock_condition_final.append('Out of Stock')
                        # colour
                        try:
                            colour = list1[0][4]
                        except:
                            colour = ''
                    except Exception as e:
                        variant_id=''
                        variant_list=''
                        colour=''
                        stock_condition_final=''
                        print(e)

                    # ratings and reviews
                    review_rating = re.findall(
                        r'"totalReviewCount":(.*?),"averageOverallRating":(.*?),"averageOverallStarRating":',
                        response.text)

                    if len(review_rating) == 0:
                        Reviews = '-'
                        Ratings = '-'
                    else:
                        Reviews = review_rating[0][0]
                        Ratings = review_rating[0][1]
                        if int(Reviews) < 2:
                            Reviews = '-'
                            Ratings = '-'

                    # image_urls
                    try:
                        image_urls = tree.xpath('//div[@class="gallery-aside-wrapper"]/div/ul/li/button/img/@src')
                        image_urls = join_string1(image_urls)
                    except Exception as e:
                        image_urls='-'
                        print(e,'-- image',product_url)
                    # description
                    try:
                        description = tree.xpath('//div[@class="product-description"]/ul/li/text()')
                        if len(description) == 0:
                            description = tree.xpath('//div[@class="product-description"]/ul/li/span/text()')
                        for desc in range(len(description)):
                            description[desc] = description[desc].strip(' ').strip('\xa0')
                        description = join_string1(description)
                    except Exception as e:
                        description='-'
                        print(e,'---- description',product_url)
                    if description=='':
                        description='-'
                    else:
                        description=description

                    try:
                        # specifications
                        specifications = tree.xpath('//div[@class="col"]/div[@class="about-me"]/text()')
                        xyz = listToString(specifications)
                        if ":" in xyz:
                            for abc in specifications:
                                if ':' in abc:
                                    specifications = abc.strip(' ').strip('\n').strip('.')
                        else:
                            specifications = tree.xpath('//div[@class="col"]/div[@class="about-me"]/p/text()')
                            xyz = listToString(specifications)
                            if ":" in xyz:
                                for abc in specifications:
                                    if ':' in abc:
                                        specifications = abc.strip(' ').strip('\n').strip('.')
                            else:
                                specifications = tree.xpath('//div[@class="col"]/div[@class="about-me"]/div/text()')
                                xyz = listToString(specifications)
                                if ":" in xyz:
                                    for abc in specifications:
                                        if ":" in abc:
                                            specifications = abc.strip(' ').strip('\n').strip('.')
                                else:
                                    specifications = tree.xpath('//div[@class="col"]/div[@class="about-me"]/p/span/text()')
                                    xyz = listToString(specifications)
                                    if ':' in xyz:
                                        for abc in specifications:
                                            if ":" in abc:
                                                specifications = abc.strip(' ').strip('\n').strip('.')
                                    else:
                                        specifications = tree.xpath(
                                            '//div[@class="col"]/div[@class="about-me"]/div/div/text()')
                                        xyz = listToString(specifications)
                                        if ':' in xyz:
                                            for abc in specifications:
                                                if ':' in abc:
                                                    specifications = abc.strip(' ').strip('\n').strip('.')
                                        else:
                                            specifications = tree.xpath(
                                                '//div[@class="col"]/div[@class="about-me"]/span/text()')
                                            xyz = listToString(specifications)
                                            if ':' in xyz:
                                                for abc in specifications:
                                                    if ':' in abc:
                                                        specifications = abc.strip(' ').strip('\n').strip('.')
                                            else:
                                                specifications = tree.xpath(
                                                    '//div[@class="col"]/div[@class="about-me"]/div/span/text()')
                                                xyz = listToString(specifications)
                                                if ':' in xyz:
                                                    for abc in specifications:
                                                        if ':' in abc:
                                                            specifications = abc.strip(' ').strip('\n').strip('.')
                        if len(specifications) == 0:
                            specifications = '-'

                        if specifications != '-':
                            specifications_value = specifications.split(', ')
                            specifications_bool = specifications_value[-1][0].isdigit()
                            if specifications_bool == True:
                                specifications_value[-2] = specifications_value[-2] + ", " + specifications_value[-1]
                                specifications_value.pop()
                                specifications = specifications_value
                                specifications = join_string1(specifications)
                    except Exception as e:
                        specifications='-'
                        print(e,'--- specification',product_url)

                    # pagesave
                    now = datetime.now()
                    date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
                    date_time1 = str(now.strftime("%m%d%Y"))
                    try:
                        datazone = datetime.now()
                        f_date = datazone.strftime("%d_%m_%Y")
                        # date_time1 = '17032022'
                        # f_date = '17_03_2022'
                        cpid = SKU_ID + '_' + date_time1
                        ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Asos_IT\\PDP"
                        sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                        if os.path.exists(sos_date_wise_folder):
                            pass
                        else:
                            os.mkdir(sos_date_wise_folder)
                        sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
                        sos_filename = sos_filename.replace("+", "_").replace("-", "_")
                        page_path = sos_filename
                        page_path = page_path.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\','https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace('//', '/')
                        # cptext = response.text + response1.text
                        cptext = response.text
                        if os.path.exists(sos_filename):
                            # with open(sos_filename, 'wb', encoding='utf-8') as f:
                            with open(sos_filename, 'wb') as f:
                                f.write(response123.body)
                        else:
                            with open(sos_filename, 'wb') as f:
                                # f.write(response.text)
                                f.write(response123.body)
                    except Exception as e:
                        page_location = ''
                        print(e)
                    try:
                        a = tree.xpath('//script[contains(text(),"window.asos.pdp.config.product = ")]/text()')
                        # print(type(a))
                        d = str(a)
                        # print(d)
                        data1 = d.split("window.asos.pdp.config.product =")[1].split(";")[0]
                        # print(data1)
                        data1=str(data1).replace("\\'","'")
                        j_data = json.loads(data1)
                        print(type(j_data))
                        varxy = j_data['products']
                        var = j_data['products'][0]['variants']
                        try:
                            seller_name = var[0].get('seller')
                            if not seller_name:
                                seller_name='-'
                        except Exception as e:
                            seller_name = "-"
                    except Exception as e:
                        seller_name='-'
                    for siz in range(len(variant_id)):
                        now = datetime.now()
                        date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
                        data1={'SKU_ID':SKU_ID,'Website':'Asos','Country':Country,'RPC':RPC,'MPC':'Not Available','Product_ID':RPC,
                               'Product URL':Product_url,'Product_Name':product_name,'Category Path':category_path,'Specification':specifications,
                               'Description':description,'Currency':'GBP','List_Price':list_price,'Promo_Price':promo_price,'Discount':discount,
                               'Brand':Brand,'Rating_Count':Ratings,'Review_Count':Reviews,'Image_URLs':image_urls,'Variant': variant_list[siz], 'Variant_ID': variant_id[siz],
                               'Colour_of_Variant': colour, 'Colour_Grouping': 'Not Available','Seller_Name': seller_name, 'Stock_Count': 'Not Available', 'Stock_Condition':stock_condition_final[siz],
                                                          'Stock_Message': '-', 'Sustainability_Badge': 'Not Available',
                                                          'Reason_Code': 'Success-PF', 'Crawling_TimeStamp': date_time,
                                                          'Cache_Page_Link' : page_path, 'Extra1': '-', 'Extra2': '-', 'Extra3': '-',
                                                          'Extra4': '-', 'Extra5': '-'}

                        # create_csv(data1)
                        print(data1)
                        products_df=products_df.append(data1, ignore_index=True)
                        # products_df.to_csv(f'ASOS_IT_sku_data1_{date_time1}.csv', encoding='utf-8',
                        products_df.to_csv(f'ASOS_UK_sku_data1_{date_time1}_pending1.csv', encoding='utf-8',
                                           columns=['SKU_ID', 'Website', 'Country',
                                                    'RPC', 'MPC', 'Product_ID',
                                                    'Product URL', 'Product_Name', 'Category Path', 'Specification',
                                                    'Description',
                                                    'Currency', 'List_Price', 'Promo_Price', 'Discount', 'Brand',
                                                    'Rating_Count',
                                                    'Review_Count', 'Image_URLs', 'Variant', 'Variant_ID',
                                                    'Colour_of_Variant',
                                                    'Colour_Grouping', 'Seller_Name', 'Stock_Count', 'Stock_Condition',
                                                    'Stock_Message', 'Sustainability_Badge', 'Reason_Code',
                                                    'Crawling_TimeStamp', 'Cache_Page_Link', 'Extra1', 'Extra2',
                                                    'Extra3',
                                                    'Extra4', 'Extra5'],index=False)
                    break
                else:
                    print('trying again for main url.....')
                    continue
            except Exception as e:
                print(i,'-----------------------')
                if counter >=14:
                    now = datetime.now()
                    date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
                    date_time1 = str(now.strftime("%m%d%Y"))
                    data1 = {'SKU_ID': SKU_ID, 'Website': 'Asos', 'Country': Country, 'RPC': '-', 'MPC': 'Not Available',
                             'Product_ID': '-',
                             'Product URL': Product_url, 'Product_Name': '-', 'Category Path': '-',
                             'Specification': '-',
                             'Description': '-', 'Currency': '-', 'List_Price': '-',
                             'Promo_Price': '-', 'Discount': '-',
                             'Brand': '-', 'Rating_Count': '-', 'Review_Count': '-', 'Image_URLs': '-',
                             'Variant': '-', 'Variant_ID': '-',
                             'Colour_of_Variant': '-', 'Colour_Grouping': 'Not Available', 'Seller_Name': '-',
                             'Stock_Count': 'Not Available', 'Stock_Condition': '-',
                             'Stock_Message': '-', 'Sustainability_Badge': 'Not Available',
                             'Reason_Code': 'blocked', 'Crawling_TimeStamp': date_time,
                             'Cache_Page_Link': page_path, 'Extra1': '-', 'Extra2': '-', 'Extra3': '-',
                             'Extra4': '-', 'Extra5': '-'}
                    products_df = products_df.append(data1, ignore_index=True)
                    # products_df.to_csv(f'ASOS_IT_sku_data1_{date_time1}.csv', encoding='utf-8',
                    products_df.to_csv(f'ASOS_UK_sku_data1_{date_time1}_pending1.csv', encoding='utf-8',
                                       columns=['SKU_ID', 'Website', 'Country',
                                                'RPC', 'MPC', 'Product_ID',
                                                'Product URL', 'Product_Name', 'Category Path', 'Specification',
                                                'Description',
                                                'Currency', 'List_Price', 'Promo_Price', 'Discount', 'Brand',
                                                'Rating_Count',
                                                'Review_Count', 'Image_URLs', 'Variant', 'Variant_ID', 'Colour_of_Variant',
                                                'Colour_Grouping', 'Seller_Name', 'Stock_Count', 'Stock_Condition',
                                                'Stock_Message', 'Sustainability_Badge', 'Reason_Code',
                                                'Crawling_TimeStamp', 'Cache_Page_Link', 'Extra1', 'Extra2', 'Extra3',
                                                'Extra4', 'Extra5'],index=False)
                else:
                    counter=counter+1
                    continue
                print(e)
                print('response issue here. exception part.....')
# df=pd.read_csv(r'asos_pdp_input1.csv')
df=pd.read_csv(r'asos_pdp_input1.csv')
# df=pd.read_csv(r'E:\Prarthavi\SKU script\SKU_ASOS\SKU\ASOS_pdp\asos_pdp_pending1_new.csv')
# df=pd.read_csv(r'E:\Prarthavi\SKU script\SKU_ASOS\SKU\ASOS_pdp\asos_pdp_input1_pending.csv')
ASOS_UK_SKU(df)
