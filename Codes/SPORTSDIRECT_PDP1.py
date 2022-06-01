import os
import re
import  random
import general
import general
import requests
import json
import pandas as pd
from datetime import datetime
from scrapy.http import HtmlResponse
from lxml import  html
from bs4 import  BeautifulSoup

search_URL = "https://www.sportsdirect.com/searchresults?descriptionfilter="
# headers = {
#         'authority': 'www.sportsdirect.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
#         }
headers = {
    'authority': 'www.sportsdirect.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
}
# input_sheet = pd.read_excel(r'C:\Users\gagandeep.sharma01\Dropbox\Adidas Crawler Automation (1)\Sample Inputs\Sportsdirect.com_Scrape Input_01112022.xlsx', sheet_name='SKU', nrows=10)
# input_sheet = pd.read_excel(r'ASS-1.xlsx')#, nrows=10), sheet_name='Sheet1'
input_sheet = pd.read_excel(r'ASS-1.xlsx')#, nrows=10), sheet_name='Sheet1'
input_link = input_sheet['PDP URL']
input_links = input_link
website = input_sheet['Website']
country = input_sheet['Country']
sku_id = input_sheet['SKU_ID']

all_product_data = []
data_record = []
pos_count = 1
c = 0
for idx, link in enumerate(input_links):
        #print((website[idx], country[idx], sku_id[idx], link))
        #link = 'https://www.sportsdirect.com/reebok-op2-abu-dhabi-t-shirt-mens-621704#colcode=62170403'
        #link = 'https://www.sportsdirect.com/adidas-real-madrid-home-socks-2021-2022-373048#colcode=37304801'

        try:
                for _ in range(30):
                        p1 = ['154.28.67.106', '154.28.67.111', '154.28.67.116', '154.28.67.117', '154.28.67.125',
                          '154.28.67.131',
                          '154.28.67.133', '154.28.67.142', '154.28.67.156', '154.28.67.163', '154.28.67.173',
                          '154.28.67.18',
                          '154.28.67.182', '154.28.67.184', '154.28.67.20', '154.28.67.200', '154.28.67.210',
                          '154.28.67.218',
                          '154.28.67.222', '154.28.67.223', '154.28.67.231', '154.28.67.240', '154.28.67.243',
                          '154.28.67.253',
                          '154.28.67.39', '154.28.67.4', '154.28.67.49', '154.28.67.5', '154.28.67.61', '154.28.67.80',
                          '154.28.67.81', '154.28.67.87', '154.28.67.88', '154.28.67.96', '154.28.67.99',
                          '154.7.230.100',
                          '154.7.230.101', '154.7.230.103', '154.7.230.107', '154.7.230.109', '154.7.230.130',
                          '154.7.230.132',
                          '154.7.230.14', '154.7.230.140', '154.7.230.147', '154.7.230.151', '154.7.230.156',
                          '154.7.230.163',
                          '154.7.230.170', '154.7.230.18', '154.7.230.183', '154.7.230.188', '154.7.230.189',
                          '154.7.230.19',
                          '154.7.230.190', '154.7.230.198', '154.7.230.204', '154.7.230.209', '154.7.230.235',
                          '154.7.230.238',
                          '154.7.230.246', '154.7.230.29', '154.7.230.41', '154.7.230.42', '154.7.230.51',
                          '154.7.230.55',
                          '154.7.230.60', '154.7.230.61', '154.7.230.74', '154.7.230.82', '154.7.230.89',
                          '23.131.8.112',
                          '23.131.8.115', '23.131.8.117', '23.131.8.12', '23.131.8.121', '23.131.8.124', '23.131.8.150',
                          '23.131.8.161', '23.131.8.166', '23.131.8.171', '23.131.8.173', '23.131.8.176',
                          '23.131.8.177',
                          '23.131.8.181', '23.131.8.19', '23.131.8.192', '23.131.8.194', '23.131.8.199', '23.131.8.202',
                          '23.131.8.203', '23.131.8.204', '23.131.8.207', '23.131.8.209', '23.131.8.213',
                          '23.131.8.216',
                          '23.131.8.225', '23.131.8.228', '23.131.8.231', '23.131.8.238', '23.131.8.254', '23.131.8.36',
                          '23.131.8.5', '23.131.8.76', '23.131.8.93', '23.131.8.95', '23.131.8.99', '23.131.88.105',
                          '23.131.88.12', '23.131.88.137', '23.131.88.139', '23.131.88.140', '23.131.88.145',
                          '23.131.88.150',
                          '23.131.88.151', '23.131.88.153', '23.131.88.154', '23.131.88.156', '23.131.88.165',
                          '23.131.88.18',
                          '23.131.88.191', '23.131.88.192', '23.131.88.194', '23.131.88.198', '23.131.88.202',
                          '23.131.88.206',
                          '23.131.88.220', '23.131.88.223', '23.131.88.228', '23.131.88.233', '23.131.88.24',
                          '23.131.88.242',
                          '23.131.88.244', '23.131.88.47', '23.131.88.63', '23.131.88.67', '23.131.88.73',
                          '23.131.88.80',
                          '23.131.88.81', '23.131.88.82', '23.131.88.88', '23.131.88.97', '23.170.144.149',
                          '23.170.144.209',
                          '23.170.144.212', '23.170.144.242', '23.170.144.83', '23.170.145.117', '23.170.145.167',
                          '23.170.145.182', '23.170.145.19', '23.170.145.203', '23.226.17.101', '23.226.17.109',
                          '23.226.17.112', '23.226.17.113', '23.226.17.115', '23.226.17.123', '23.226.17.129',
                          '23.226.17.143',
                          '23.226.17.148', '23.226.17.165', '23.226.17.186', '23.226.17.199', '23.226.17.201',
                          '23.226.17.207',
                          '23.226.17.210', '23.226.17.219', '23.226.17.220', '23.226.17.222', '23.226.17.229',
                          '23.226.17.250',
                          '23.226.17.254', '23.226.17.26', '23.226.17.33', '23.226.17.4', '23.226.17.49', '23.226.17.5',
                          '23.226.17.55', '23.226.17.66', '23.226.17.7', '23.226.17.72', '23.226.17.78', '23.226.17.8',
                          '23.226.17.86', '23.226.17.90', '23.226.17.93', '23.230.177.105', '23.230.177.110',
                          '23.230.177.113',
                          '23.230.177.121', '23.230.177.130', '23.230.177.14', '23.230.177.143', '23.230.177.15',
                          '23.230.177.150', '23.230.177.154', '23.230.177.165', '23.230.177.173', '23.230.177.191',
                          '23.230.177.196', '23.230.177.203', '23.230.177.206', '23.230.177.208', '23.230.177.217',
                          '23.230.177.220', '23.230.177.221', '23.230.177.224', '23.230.177.228', '23.230.177.231',
                          '23.230.177.235', '23.230.177.237', '23.230.177.241', '23.230.177.27', '23.230.177.38',
                          '23.230.177.52', '23.230.177.61', '23.230.177.67', '23.230.177.72', '23.230.177.80',
                          '23.230.177.88',
                          '23.230.177.94', '23.230.177.99', '23.230.197.103', '23.230.197.106', '23.230.197.109',
                          '23.230.197.11', '23.230.197.12', '23.230.197.122', '23.230.197.124', '23.230.197.146',
                          '23.230.197.155', '23.230.197.156', '23.230.197.174', '23.230.197.179', '23.230.197.181',
                          '23.230.197.196', '23.230.197.2', '23.230.197.201', '23.230.197.207', '23.230.197.208',
                          '23.230.197.225', '23.230.197.227', '23.230.197.233', '23.230.197.236', '23.230.197.239',
                          '23.230.197.240', '23.230.197.244', '23.230.197.251', '23.230.197.50', '23.230.197.52',
                          '23.230.197.54', '23.230.197.60', '23.230.197.71', '23.230.197.80', '23.230.197.81',
                          '23.230.197.84',
                          '23.230.197.97', '23.230.74.102', '23.230.74.110', '23.230.74.116', '23.230.74.125',
                          '23.230.74.133',
                          '23.230.74.135', '23.230.74.14', '23.230.74.141', '23.230.74.149', '23.230.74.15',
                          '23.230.74.157',
                          '23.230.74.16', '23.230.74.170', '23.230.74.172', '23.230.74.174', '23.230.74.183',
                          '23.230.74.187',
                          '23.230.74.19', '23.230.74.198', '23.230.74.208', '23.230.74.212', '23.230.74.215',
                          '23.230.74.23',
                          '23.230.74.230', '23.230.74.231', '23.230.74.252', '23.230.74.30', '23.230.74.41',
                          '23.230.74.57',
                          '23.230.74.58', '23.230.74.59', '23.230.74.6', '23.230.74.75', '23.230.74.81', '23.230.74.88',
                          '23.230.74.91', '23.27.222.108', '23.27.222.109', '23.27.222.134', '23.27.222.138',
                          '23.27.222.159',
                          '23.27.222.161', '23.27.222.164', '23.27.222.166', '23.27.222.178', '23.27.222.19',
                          '23.27.222.195',
                          '23.27.222.201', '23.27.222.202', '23.27.222.203', '23.27.222.208', '23.27.222.21',
                          '23.27.222.211',
                          '23.27.222.218', '23.27.222.223', '23.27.222.228', '23.27.222.234', '23.27.222.236',
                          '23.27.222.242',
                          '23.27.222.251', '23.27.222.253', '23.27.222.34', '23.27.222.61', '23.27.222.62',
                          '23.27.222.69',
                          '23.27.222.70', '23.27.222.72', '23.27.222.73', '23.27.222.74', '23.27.222.81',
                          '23.27.222.93',
                          '38.131.131.110', '38.131.131.114', '38.131.131.123', '38.131.131.125', '38.131.131.137',
                          '38.131.131.142', '38.131.131.145', '38.131.131.147', '38.131.131.15', '38.131.131.154',
                          '38.131.131.16', '38.131.131.17', '38.131.131.173', '38.131.131.18', '38.131.131.193',
                          '38.131.131.204', '38.131.131.207', '38.131.131.227', '38.131.131.229', '38.131.131.233',
                          '38.131.131.238', '38.131.131.246', '38.131.131.248', '38.131.131.250', '38.131.131.31',
                          '38.131.131.36', '38.131.131.50', '38.131.131.58', '38.131.131.64', '38.131.131.70',
                          '38.131.131.71',
                          '38.131.131.74', '38.131.131.83', '38.131.131.94', '38.131.131.99', '38.75.75.104',
                          '38.75.75.111',
                          '38.75.75.112', '38.75.75.119', '38.75.75.120', '38.75.75.123', '38.75.75.127',
                          '38.75.75.139',
                          '38.75.75.14', '38.75.75.143', '38.75.75.155', '38.75.75.156', '38.75.75.158', '38.75.75.170',
                          '38.75.75.179', '38.75.75.188', '38.75.75.2', '38.75.75.201', '38.75.75.231', '38.75.75.232',
                          '38.75.75.241', '38.75.75.246', '38.75.75.251', '38.75.75.26', '38.75.75.29', '38.75.75.4',
                          '38.75.75.44', '38.75.75.49', '38.75.75.56', '38.75.75.58', '38.75.75.62', '38.75.75.72',
                          '38.75.75.76', '38.75.75.79', '38.75.75.88', '38.96.156.108', '38.96.156.112',
                          '38.96.156.128',
                          '38.96.156.131', '38.96.156.14', '38.96.156.142', '38.96.156.143', '38.96.156.149',
                          '38.96.156.16',
                          '38.96.156.163', '38.96.156.165', '38.96.156.169', '38.96.156.186', '38.96.156.188',
                          '38.96.156.190',
                          '38.96.156.192', '38.96.156.194', '38.96.156.199', '38.96.156.218', '38.96.156.236',
                          '38.96.156.240',
                          '38.96.156.252', '38.96.156.28', '38.96.156.32', '38.96.156.35', '38.96.156.56',
                          '38.96.156.57',
                          '38.96.156.6', '38.96.156.67', '38.96.156.77', '38.96.156.80', '38.96.156.83', '38.96.156.84',
                          '38.96.156.89', '38.96.156.92', '45.238.157.100', '45.238.157.104', '45.238.157.106',
                          '45.238.157.110', '45.238.157.116', '45.238.157.118', '45.238.157.119', '45.238.157.12',
                          '45.238.157.123', '45.238.157.132', '45.238.157.14', '45.238.157.149', '45.238.157.15',
                          '45.238.157.183', '45.238.157.186', '45.238.157.189', '45.238.157.2', '45.238.157.212',
                          '45.238.157.214', '45.238.157.217', '45.238.157.22', '45.238.157.228', '45.238.157.23',
                          '45.238.157.247', '45.238.157.43', '45.238.157.48', '45.238.157.51', '45.238.157.52',
                          '45.238.157.53',
                          '45.238.157.56', '45.238.157.61', '45.238.157.65', '45.238.157.72', '45.238.157.79',
                          '45.238.157.8',
                          '45.238.159.103', '45.238.159.107', '45.238.159.110', '45.238.159.114', '45.238.159.116',
                          '45.238.159.123', '45.238.159.126', '45.238.159.144', '45.238.159.148', '45.238.159.15',
                          '45.238.159.156', '45.238.159.165', '45.238.159.167', '45.238.159.183', '45.238.159.20',
                          '45.238.159.208', '45.238.159.217', '45.238.159.220', '45.238.159.23', '45.238.159.230',
                          '45.238.159.235', '45.238.159.237', '45.238.159.238', '45.238.159.24', '45.238.159.249',
                          '45.238.159.251', '45.238.159.32', '45.238.159.34', '45.238.159.51', '45.238.159.6',
                          '45.238.159.66',
                          '45.238.159.77', '45.238.159.79', '45.238.159.82', '45.238.159.91']

                        p_auth = str("csimonra:h19VA2xZ")
                        p_host = random.choice(p1)
                        p_port = "29842"
                        proxy = {
                                'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
                                'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
                        }
                        #link = 'https://www.sportsdirect.com/reebok-nano-x1-mens-training-shoes-131192#colcode=13119202'
                        res = requests.request("GET", link, headers=headers, proxies=proxy)
                        response = HtmlResponse(url=link, body=res.content)
                        if res.status_code == 200:
                                saving_data = res.text
                                tree =html.fromstring(res.content)
                                soup = BeautifulSoup(res.content, 'lxml')
                                break

                # SAVING PAGE=========================================
                url = link.split('#colcode=')
                try:
                    rpc = url[1]
                except:
                    rpc = '-'

                page_id = 'SportsDirect_UK_code=' + rpc
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
                date_time1 = str(now.strftime("%m%d%Y"))
                try:
                        datazone = datetime.now()
                        f_date = datazone.strftime("%d_%m_%Y")
                        # f_date = datazone.strftime("03_04_2022")
                        cpid = page_id + '_' + date_time1
                        # f_date = datazone.strftime("03_04_2022")
                        # cpid = page_id + '_' + f_date

                        #--
                        ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_com\PDP"
                        sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                        if os.path.exists(sos_date_wise_folder):
                                pass
                        else:
                                os.mkdir(sos_date_wise_folder)
                        sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
                        sos_filename = sos_filename.replace("+", "_").replace("-", "_")
                        page_path = sos_filename.replace('/', '')
                        print(page_path)
                        page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                                      'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                             '//').replace(
                                '//', '/')
                        print(page_path)
                        if os.path.exists(sos_filename):
                                with open(sos_filename, 'w', encoding='utf-8') as f:
                                        f.write(saving_data)
                        else:
                                with open(sos_filename, 'w', encoding='utf-8') as f:
                                        f.write(saving_data)
                except Exception as e:
                        page_location = ''
                        print(e)
                # =========================================
                if res.status_code == 200:
                        url = link.split('#colcode=')
                        try:
                                rpc = url[1]
                        except:
                                rpc = '-'
                        try:
                                product_url = ''.join(response.xpath('//link[@rel="canonical"]/@href').extract())
                        except Exception as e:
                                product_url = "Not Available"
                        try:
                            product_dataid = ''.join(
                                response.xpath("//script[text()[contains(.,'window.DY = window.DY')]]/text()").extract())
                            product_dataid = product_dataid.split('data: ["', 1)[1]
                            product_dataid = (product_dataid.split('"], lng:', 1)[0])
                            idx = product_dataid.index('-')
                            product_dataid = product_dataid[0:idx - 2] + product_dataid[idx:]
                        except:
                            product_dataid = ''

                        try:
                                product_name = ''.join(response.xpath('//span[@class = "prodTitle"]//span/text()').extract())
                                product_name = product_name.replace('+', '').replace('=', '').strip()
                        except Exception as e:
                                product_name = "Not Available"
                                print("Exception occurred : ", e)

                        try:
                                brand = (''.join(response.xpath(
                                        '//span[@class = "brandTitle"]//a/span/text()').extract())).strip()
                        except Exception as e:
                                brand = "Not Available"
                                print("Exception occurred : ", e)

                        try:
                                category_path = ' > '.join(
                                        response.xpath('//div[@class = "s-breadcrumbs-bar"]//ol/li/a/span/text()').extract())
                        except Exception as e:
                                category_path = "Not Available"
                                print("Exception occurred : ", e)

                        try:
                                promo_price = (
                                        ''.join(response.xpath('//div[@class = "pdpPrice"]/span/text()').extract())).strip()
                                promo_price = promo_price.replace('£', '')
                        except Exception as e:
                                promo_price = "-"
                                print("Exception occurred : ", e)

                        try:
                                list_price = (''.join(response.xpath(
                                        '//div[@class = "originalprice"]/span/text()').extract())).strip()
                                list_price = list_price.replace('£', '')
                        except Exception as e:
                                list_price = "-"
                                print("Exception occurred : ", e )
                        if list_price == promo_price:
                            discount = '-'
                        elif list_price == '0.00':
                            list_price=promo_price
                            discount='-'
                        else:
                            discount = ((float(list_price)-float(promo_price))/float(list_price))*100
                            discount = format(discount,'.2f')
                            # print(discount)


                        try:
                                image_urls = ' | '.join(response.xpath('//ul[@id = "piThumbList"]//li/a/@href').extract())
                        except Exception as e:
                                image_urls = "Not Available"
                                print("Exception occurred : ", e)
                        variant_id = "Not Available"

                        #try:
                        #       variant_id = re.findall('products/(.*?)_l', image_urls)[0]
                        #except Exception as e:
                        #     variant_id = "Not Available"
                        #       print("Exception occurred : ", e)

                        try:
                                color_of_variant = (
                                        ''.join(response.xpath('//span[@id = "colourName"]/text()').extract())).strip()
                                if color_of_variant == '':
                                    color_of_variant = '-'
                        except Exception as e:
                                color_of_variant = "Not Available"
                                print("Exception occurred : ", e)


                        color_grouping = (response.xpath('//ul[@id = "ulColourImages"]//li/a/img/@alt').extract())
                        if len(color_grouping) > 0:
                            color_grouping = "|".join(color_grouping)
                        else:
                            color_grouping = '-'


                        try: #t- //div[@class = "infoTabPage"]//span/text()
                                description = (''.join(response.xpath('//div[@class = "infoTabPage"]//span[@itemprop="description"]/text()').extract())).strip()
                                description = description.replace('>', '')
                                if description == '':
                                    description = '-'
                        except Exception as e:
                                description = "-"
                                print("Exception occurred : ", e)

                        try:
                                specification_table = response.xpath('//dl[@id="DisplayAttributes"]//text()').extract()[1::2]
                                specification = {key: value for key, value in
                                                 zip(specification_table[::2], specification_table[1::2])}
                                specification = " | ".join("{} : {}".format(*i) for i in specification.items())
                                if specification == '':
                                    specification = '-'

                        except Exception as e:
                                specification = "Not Available"
                                print("Exception occurred : ", e)

                        try:
                                prod_id = ((''.join(response.xpath('//p[@class = "productCode"]/text()').extract())).replace(
                                        "Product code:", "")).strip()
                        except Exception as e:
                                prod_id = "Not Available"
                                print("Exception occurred : ", e)
                        specification = general.clean(specification)
                        description = general.clean(description)

                        status_code = res.status_code
                        if status_code == 200:
                            reason_code = 'Success-PF'

                        #general.write_file('sp.html', res.text, 'a', encoding='utf-8')
                        s = general.xpath(tree, '//span[@class="ProductDetailsVariants hidden"]/@data-variants')

                        if len(s) > 1:
                            try:
                                s_data = json.loads(s)
                                print(type(s_data[len(s_data)-1]))
                                print(s_data[len(s_data)-1])
                                get_data = s_data[len(s_data)-1]
                                seller = get_data['SizeVariants'][0]['SuppliedByName']
                                if seller is None:
                                    seller = 'None'

                            except:
                                seller = ''

                        else:
                            seller = ''

                        print(('seller = ', seller))
                        data = ''.join(response.xpath('//*[@id="structuredDataLdJson"]//text()').extract())
                        data = general.clean(data)
                        # file_data = json.loads(data)


                        try:
                                inStock = response.xpath(
                                        '//ul[@id = "ulSizes"]//li[@class = "tooltip sizeButtonli "]/@data-text').extract()
                                outofStock = response.xpath(
                                        '//ul[@id = "ulSizes"]//li[@class = "tooltip sizeButtonli greyOut"]/@data-text').extract()
                        except Exception as e:
                                pass


                        # Requesting to another URL to get the ratings & reviews contents of the product
                        ratings_api = "https://api.bazaarvoice.com/data/display/0.2alpha/product/summary?PassKey=caiGlgNZJbkmq4vv9Aasd5JdLBg2YKJzgwEEhL0sLkQUw&productid={p_id}&contentType=reviews,questions&reviewDistribution=primaryRating,recommended&rev=0&contentlocale=en*,en_GB".format(
                                p_id=product_dataid)
                        res = requests.request("GET", ratings_api, proxies=proxy)   # , headers=headers)
                        json_data = json.loads(res.text)

                        try:
                                ratings = str(json_data['reviewSummary']['primaryRating']['average'])[0:3]
                        except Exception as e:
                                ratings = "Not Available"
                                print("Exception occurred : ", e)
                        if ratings== 'Non':
                                ratings = '-'
                        print(json_data)
                        try:
                                reviews = json_data['reviewSummary']['numReviews']
                        except Exception as e:
                                reviews = "Not Available"
                                print("Exception occurred : ", e)
                        if reviews == 0 :
                            reviews = '-'

                        try:
                                variants = response.xpath('//ul[@id = "ulSizes"]//li/@data-text').extract()
                        except Exception as e:
                                variants = "Not Available"
                                print("Exception occurred : ", e)

                        for variant in variants:
                                print(variant)
                                if variant in inStock:
                                        stock_condition = "In Stock"
                                elif variant in outofStock:
                                        stock_condition = "Out of Stock"
                                data_dict = {
                                        'SKU_ID': 'sportsdirect_UK_code=' + rpc,
                                        'Website': 'SportsDirect',
                                        'Country': 'UK',
                                        'RPC': rpc,
                                        'MPC': 'Not Available',
                                        'Product_ID': prod_id,
                                        'Product_URL': link,
                                        'Product_Name': product_name,
                                        'Category_Path': category_path,
                                        'Specification': specification,
                                        'Description': description,
                                        'Currency': 'GBP',
                                        'List_Price': list_price,
                                        'Promo_Price': promo_price,
                                        'Discount': discount,
                                        'Brand': brand,
                                        'Rating_Count':ratings,
                                        'Review_Count': reviews,
                                        'Image_URLs': image_urls,
                                        'Variant': variant,
                                        'Variant_ID': variant_id,
                                        'Colour_of_Variant': color_of_variant,
                                        'Colour_Grouping': color_grouping,
                                        'Seller_Name': seller,
                                        'Stock_Count': 'Not Available',
                                        'Stock_Condition': stock_condition,
                                        'Stock_Message': 'Not Available',
                                        'Sustainability_Badge': 'Not Available',
                                        'Reason_Code': reason_code,
                                        'Crawling_TimeStamp':datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                        'Cache_Page_Link': page_path,
                                        'Extra1': '-',
                                        'Extra2': '-',
                                        'Extra3': '-',
                                        'Extra4': '-',
                                        'Extra5': '-'
                                }
                                all_product_data.append(data_dict)
                                print(data_dict)
                        f_s_d = datetime.now().strftime("%d-%m-")
                        data_df = pd.DataFrame(all_product_data)
                        data_csv = data_df.to_csv(fr"{f_s_d}SPORTSDIRECT-PDP1.csv",
                                                  encoding="utf-8", index=False)
                        print("\nData saved successfully!\n")


        except Exception as e:
            #general.write_file(r'E:\Nilesh\Adidas\Sportsdirect\PDP\input_failed.txt', link, 'a', encoding=None)
            print("working")
            data_dict = {
                'SKU_ID': '-',
                'Website': 'SportsDirect',
                'Country': 'UK',
                'RPC': '-',
                'MPC': '-',
                'Product_ID': '-',
                'Product_URL': link,
                'Product_Name': '-',
                'Category_Path': '-',
                'Specification': '-',
                'Description': '-',
                'Currency': '-',
                'List_Price': '-',
                'Promo_Price': '-',
                'Discount': '-',
                'Brand': '-',
                'Rating_Count': '-',
                'Review_Count': '-',
                'Image_URLs': '-',
                'Variant': '-',
                'Variant_ID': '-',
                'Colour_of_Variant': '-',
                'Colour_Grouping': '-',
                'Seller_Name': '-',
                'Stock_Count': '-',
                'Stock_Condition': '-',
                'Stock_Message': '-',
                'Sustainability_Badge': '-',
                'Reason_Code': "Success-PNF",
                'Crawling_TimeStamp': datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                'Cache_Page_Link': '-',
                'Extra1': '-',
                'Extra2': '-',
                'Extra3': '-',
                'Extra4': '-',
                'Extra5': '-'
            }
            all_product_data.append(data_dict)
            # data_df = pd.DataFrame(all_product_data)
            # data_csv = data_df.to_csv(r"28-SPORTSDIRECT-PDP1.csv",
            #                           encoding="utf-8", index=False)
            # print("\n NOT Data saved successfully!\n")
        pos_count = pos_count + 1


        c += 1
print("\nData saved successfully!\n")