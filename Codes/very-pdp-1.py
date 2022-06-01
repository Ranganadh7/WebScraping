import pandas as pd
import requests
from lxml import html
import re
from itertools import chain
import numpy as np
from datetime import datetime
import random
from random import choice
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', }
p1 = ['104.218.195.130', '104.218.195.205', '104.251.82.191', '104.251.82.240', '104.251.82.63',
      '104.251.84.104', '104.251.84.217', '104.251.84.232', '104.251.85.123', '104.251.85.196',
      '104.251.86.162', '104.251.86.167', '104.251.86.209', '104.251.90.200', '104.251.90.237', '104.251.90.69',
      '104.251.91.154', '104.251.91.233', '104.251.92.178', '104.251.92.234', '104.251.92.63',
      '108.177.131.182', '108.177.131.25', '146.19.55.151', '146.19.55.167', '154.13.200.241', '154.13.200.34',
      '154.13.200.48', '154.13.201.156', '154.13.201.245', '154.13.202.117', '154.13.202.128', '154.13.202.146',
      '154.13.203.144', '154.13.203.212', '154.13.204.132', '154.13.204.98', '154.13.205.173', '154.13.205.40',
      '154.13.206.167', '154.13.206.181', '154.13.207.213', '154.13.207.233', '154.13.244.123',
      '154.13.244.139', '154.13.244.234', '154.13.245.128', '154.13.245.133', '154.13.245.152',
      '154.13.246.157', '154.13.246.158', '154.13.246.159', '154.13.247.187', '154.13.247.219', '154.13.247.42',
      '154.13.248.163', '154.13.248.36', '154.13.248.95', '154.13.249.100', '154.13.249.42', '154.13.250.164',
      '154.13.250.89', '154.13.251.141', '154.13.251.52', '154.13.251.76', '154.13.252.114', '154.13.252.163',
      '154.13.252.79', '154.13.253.101', '154.13.253.185', '154.13.253.195', '154.13.254.141', '154.13.254.99',
      '154.13.255.222', '154.13.255.248', '154.17.157.182', '154.17.157.234', '154.17.157.50', '154.17.188.153',
      '154.17.188.24', '154.17.189.230', '154.17.189.30', '154.29.2.16', '154.29.2.196', '154.29.2.231',
      '154.37.72.173', '154.37.72.59', '154.37.76.117', '154.37.76.137', '154.37.76.187', '158.115.224.142',
      '158.115.224.246', '158.115.225.241', '158.115.225.253', '158.115.226.137', '158.115.226.92',
      '158.115.227.120', '158.115.227.174', '165.140.224.123', '165.140.224.184', '165.140.225.115',
      '165.140.225.230', '165.140.225.46', '165.140.226.14', '165.140.226.244', '165.140.226.46',
      '165.140.227.12', '165.140.227.245', '168.91.64.213', '168.91.64.234', '168.91.64.251', '168.91.65.46',
      '168.91.65.73', '168.91.66.106', '168.91.66.123', '168.91.67.109', '168.91.67.17', '168.91.84.133',
      '168.91.84.59', '168.91.85.212', '168.91.85.30', '168.91.86.14', '168.91.86.21', '168.91.87.79',
      '168.91.87.97', '168.91.88.214', '168.91.88.245', '168.91.90.127', '168.91.90.49', '172.255.93.114',
      '172.255.93.130', '172.255.94.155', '172.255.94.158', '173.208.27.32', '173.208.27.93', '173.208.28.162',
      '173.208.28.246', '173.234.244.244', '173.234.244.79', '173.245.75.175', '173.245.75.54',
      '173.245.85.105', '173.245.85.116', '173.245.85.45', '173.245.90.138', '173.245.90.224',
      '185.255.196.162', '185.255.196.168', '185.255.197.105', '185.255.197.110', '198.251.92.13',
      '198.251.92.237', '198.251.92.29', '198.251.93.165', '198.251.93.227', '198.251.93.237',
      '207.230.104.136', '207.230.104.195', '207.230.104.90', '207.230.105.118', '207.230.105.205',
      '207.230.105.84', '207.230.106.19', '207.230.106.198', '207.230.106.204', '207.230.107.92',
      '207.230.107.95', '213.109.148.122', '213.109.148.23', '23.105.0.165', '23.105.0.224', '23.105.0.63',
      '23.105.142.171', '23.105.142.57', '23.105.143.213', '23.105.143.73', '23.105.144.123', '23.105.144.96',
      '23.105.145.215', '23.105.145.242', '23.105.146.181', '23.105.146.245', '23.105.147.152',
      '23.105.147.192', '23.105.147.203', '23.105.150.11', '23.105.150.199', '23.105.151.138', '23.105.151.3',
      '23.105.3.42', '23.105.3.68', '23.105.4.172', '23.105.4.231', '23.106.16.106', '23.106.16.203',
      '23.106.18.234', '23.106.18.44', '23.106.20.181', '23.106.20.233', '23.106.22.125', '23.106.22.147',
      '23.106.24.173', '23.106.24.41', '23.106.26.65', '23.106.26.84', '23.106.27.13', '23.106.27.139',
      '23.106.27.144', '23.106.28.230', '23.106.28.237', '23.106.30.117', '23.106.30.126', '23.110.166.102',
      '23.110.166.26', '23.110.166.76', '23.110.169.100', '23.110.169.162', '23.110.173.171', '23.110.173.225',
      '23.129.136.120', '23.129.136.245', '23.129.40.19', '23.129.40.44', '23.129.40.76', '23.129.56.191',
      '23.129.56.237', '23.161.3.146', '23.161.3.67', '23.170.144.104', '23.170.144.108', '23.170.144.19',
      '23.170.145.103', '23.170.145.252', '23.170.145.51', '23.175.176.21', '23.175.176.24', '23.175.177.176',
      '23.175.177.183', '23.175.177.8', '23.176.49.110', '23.176.49.183', '23.177.240.144', '23.177.240.217',
      '23.177.240.90', '23.184.144.105', '23.184.144.124', '23.184.144.231', '23.185.112.167', '23.185.112.229',
      '23.185.144.110', '23.185.144.171', '23.185.144.197', '23.185.80.164', '23.185.80.4', '23.185.80.6',
      '23.186.48.210', '23.186.48.248', '23.226.16.211', '23.226.16.243', '23.226.17.178', '23.226.17.240',
      '23.226.18.106', '23.226.18.193', '23.226.19.212', '23.226.19.87', '23.226.20.187', '23.226.20.90',
      '23.226.21.13', '23.226.21.22', '23.226.22.216', '23.226.22.53', '23.226.23.178', '23.226.23.250',
      '23.226.24.190', '23.226.24.6', '23.226.24.64', '23.226.25.107', '23.226.25.68', '23.226.26.158',
      '23.226.26.202', '23.226.26.220', '23.226.27.246', '23.226.27.94', '23.226.28.159', '23.226.28.194',
      '23.226.28.231', '23.226.29.126', '23.226.29.99', '23.226.30.191', '23.226.30.235', '23.226.31.131',
      '23.226.31.169', '23.226.31.193', '23.247.172.197', '23.247.172.214', '23.247.172.51', '23.247.173.202',
      '23.247.173.6', '23.247.174.196', '23.247.174.211', '23.247.174.81', '23.247.175.156', '23.247.175.215',
      '23.247.175.218', '23.27.9.103', '23.27.9.228', '23.82.105.11', '23.82.105.194', '23.82.105.45',
      '23.82.109.165', '23.82.109.242', '23.82.184.118', '23.82.184.227', '23.82.184.80', '23.82.186.178',
      '23.82.186.223', '23.82.40.136', '23.82.40.202', '23.82.40.42', '23.82.41.119', '23.82.41.40',
      '23.82.41.6', '23.82.44.209', '23.82.44.48', '23.82.80.145', '23.82.80.68', '23.82.81.171', '23.82.81.79',
      '45.146.117.234', '45.146.117.253', '45.146.118.204', '45.146.118.228', '45.146.119.223',
      '45.146.119.244', '45.154.141.33', '45.154.141.50', '45.154.142.21', '45.154.142.231', '45.154.142.42',
      '45.224.228.187', '45.224.228.87', '45.224.228.94', '45.224.230.211', '45.224.230.228', '45.224.231.141',
      '45.224.231.68', '45.237.84.117', '45.237.84.33', '45.237.86.170', '45.237.86.178', '45.238.157.141',
      '45.238.157.198', '45.238.157.225', '45.238.159.115', '45.238.159.59', '45.238.159.8', '45.59.128.144',
      '45.59.128.198', '45.59.128.236', '45.59.129.177', '45.59.129.217', '45.59.130.16', '45.59.130.218',
      '45.59.131.107', '45.59.131.140', '45.59.131.209', '45.59.180.245', '45.59.180.58', '45.59.181.38',
      '45.59.181.71', '45.59.181.80', '45.59.182.209', '45.59.182.217', '45.59.183.171', '45.59.183.214',
      '45.59.183.67', '45.71.19.128', '45.71.19.159', '52.128.0.45', '52.128.0.98', '52.128.1.105',
      '52.128.1.124', '52.128.10.164', '52.128.10.20', '52.128.11.123', '52.128.11.71', '52.128.12.46',
      '52.128.12.70', '52.128.13.125', '52.128.13.207', '52.128.14.107', '52.128.14.115', '52.128.14.30',
      '52.128.15.114', '52.128.15.92', '52.128.196.173', '52.128.196.240', '52.128.196.70', '52.128.197.105',
      '52.128.197.17', '52.128.198.105', '52.128.198.72', '52.128.198.76', '52.128.199.206', '52.128.199.237',
      '52.128.2.17', '52.128.2.58', '52.128.200.127', '52.128.200.182', '52.128.200.79', '52.128.201.194',
      '52.128.201.3', '52.128.201.56', '52.128.202.108', '52.128.202.189', '52.128.202.242', '52.128.203.21',
      '52.128.203.230', '52.128.204.144', '52.128.204.91', '52.128.205.148', '52.128.205.204', '52.128.206.110',
      '52.128.206.219', '52.128.206.96', '52.128.207.116', '52.128.207.237', '52.128.208.176', '52.128.208.60',
      '52.128.209.109', '52.128.209.120', '52.128.210.159', '52.128.210.80', '52.128.211.121', '52.128.211.155',
      '52.128.216.224', '52.128.216.41', '52.128.217.208', '52.128.217.87', '52.128.218.165', '52.128.218.65',
      '52.128.219.165', '52.128.219.177', '52.128.219.44', '52.128.220.40', '52.128.220.48', '52.128.221.181',
      '52.128.221.230', '52.128.222.161', '52.128.222.38', '52.128.223.201', '52.128.223.219', '52.128.3.86',
      '52.128.3.90', '52.128.4.106', '52.128.4.227', '52.128.5.35', '52.128.5.52', '52.128.6.111',
      '52.128.6.149', '52.128.6.93', '52.128.7.247', '52.128.7.81', '52.128.8.195', '52.128.8.33',
      '52.128.9.12', '52.128.9.177', '62.3.61.119', '62.3.61.2', '62.3.61.40', '88.218.172.175',
      '88.218.172.203', '88.218.172.83', '88.218.173.65', '88.218.173.94', '88.218.173.98', '88.218.174.16',
      '88.218.174.44', '88.218.175.235', '88.218.175.5', '88.218.175.57', '95.164.224.233', '95.164.224.38',
      '95.164.225.124', '95.164.225.21', '95.164.226.220', '95.164.226.221', '95.164.226.7', '95.164.227.152',
      '95.164.227.199', '95.164.227.206', '95.164.236.212', '95.164.236.249', '95.164.236.58', '95.164.237.111',
      '95.164.237.251', '95.164.238.183', '95.164.238.206', '95.164.239.113', '95.164.239.253']



def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '|'.join(list_string)

    return string


def listToString1(list_string):
    # Join the string based on '-' delimiter
    string = ', '.join(list_string)

    return string


all_product_data = []

wonder = ['belfast.wonderproxy.com',
'coventry.wonderproxy.com',
'malaysia.wonderproxy.com',
'london.wonderproxy.com',
'manchester.wonderproxy.com',
'gosport.wonderproxy.com',
'maidstone.wonderproxy.com',
'manila.wonderproxy.com',
'edinburgh.wonderproxy.com',
'dagupan.wonderproxy',
'malaysia.wonderproxy.com',
'newcastle.wonderproxy.com'
]
def VERY_UK_SKU(df):
    c = 1
    for url3 in df['PDP URL']:
        #url3 = 'https://www.very.co.uk/adidas-2-in-1-shorts-blackwhite/1600561830.prd'
        for _ in range(18):
            # p_auth = str("csimonra:h19VA2xZ")
            # p_host = random.choice(p1)
            # p_port = "29842"
            # proxy = {
            #     'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
            #     'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
            # }
            # ------Wonder Proxy----
            p_auth = str("ecxpremier:eCxpremier123")
            p_host = random.choice(wonder)
            p_port = "11000"
            proxy = {
                'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
                'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
            }
            # -------------------------------------------
            try:
                response = requests.get(url=url3, headers=headers, proxies=proxy)
            except:
                continue
            saving_data = response.text
            if response.status_code == 200:
                break

        # ------------
        tree = html.fromstring(response.text)

        # brand
        Brand = tree.xpath('//h1[@class="productHeading"]/text()')
        Brand = listToString(Brand)

        Product_name = tree.xpath('//h1[@class="productHeading"]/span/text()')
        Product_name = listToString(Product_name)
        if Product_name == '':
            Product_name = tree.xpath('////h1[@class="productHeading"]/span/span/span/text()')
            Product_name = listToString(Product_name)
        Product_name = Product_name.replace('\xa0', ' ')
        Product_Name = Product_name
        Product_name = Product_name.split('- ')
        if len(Product_name) > 1:
            for i in range(len(Product_name)):
                Product_name[i] = Product_name[i].strip()
            Colour_Name = Product_name[1]
        else:
            Colour_Name = '-'

        # list price
        List_price = tree.xpath(
            '//div[@class="productPrice productPrice--desktop"]/span[@class="productPrice__amount productPrice__amount--now"]/text()')
        #                 details_dict['List_price'] = listToString(List_price)
        List_price = listToString(List_price)
        List_price = List_price.strip('£')
        if 'From' in List_price:
            List_price = List_price.split(' ')
            List_price = List_price[1]
            List_price = List_price.strip('£')
        if List_price == '':
            List_price = '-'

            # promo price
        Promo_price = tree.xpath(
            '//div[@class="productPrice productPrice--desktop"]/div[@class="productPrice__amount productPrice__amount--was"]/text()')
        Promo_price = listToString(Promo_price)
        Promo_price = Promo_price.strip('£')
        if 'From' in Promo_price:
            Promo_price = Promo_price.split(' ')
            Promo_price = Promo_price[1]
            Promo_price = Promo_price.strip('£')
        if Promo_price == '':
            Promo_price = List_price

        # Discount
        try:
            Discount = tree.xpath(
                '//div[@class="productPrice productPrice--desktop"]/span[@class="productPrice__amount productPrice__amount--saving"]/text()')
            Discount = listToString(Discount)
            Discount = Discount.split(' ')
            Discount = Discount[1]
            Discount = Discount.strip(')')
            Discount = Discount.strip('£')
        #                 details_dict['Discount'] = Discount
        except:
            Discount = '-'

        # product url
        #             details_dict['Product_url'] = Domain_name
        Product_url = response.url

        # EAN Number
        EAN_Number = tree.xpath('//span[@id="productEAN"]/text()')
        EAN_Number = listToString(EAN_Number)
        EAN_Number = EAN_Number.strip(' \n ')
        if len(EAN_Number) > 1:
            EAN_Number = "EAN: " + EAN_Number
        else:
            EAN_Number = '-'
        #             details_dict['EAN_Number'] = EAN_Number

        # Catalogue Number
        Catalogue_Number = tree.xpath('//div[@class="catalogueNumber"]/span/text()')
        #             details_dict['Catalogue_Number'] = listToString(Catalogue_Number)
        Catalogue_Number = listToString(Catalogue_Number)
        Item_number = 'Item number ' + Catalogue_Number

        if EAN_Number != '-':
            Description = EAN_Number + '|' + Item_number
        else:
            Description = Item_number

        # variant_ID
        variant_ID_list = []
        variant_ID = re.findall(r',"sku(.*?)","', response.text)
        for ID in range(len(variant_ID)):
            variant_ID_list.append('sku' + variant_ID[ID])

        # stock message
        t = re.findall(r'\[(.*?)]', response.text)
        final_stock = []
        for i in range(len(t)):
            if 'In stock' in t[i] or 'Out of stock' in t[i] or 'Low stock' in t[i] or 'Unavailable' in t[
                i] or 'Available' in t[i]:
                final_stock.append(t[i])

        for i in range(len(final_stock)):
            final_stock[i] = final_stock[i].split(',')

        stock = []
        for i in final_stock:
            for k in i:
                if "Out" in k or 'In stock' in k or 'Low' in k or 'Unavailable' in k or 'Available' in k:
                    stock.append(k)

        for j in range(len(stock)):
            a = stock[j].split('#')
            stock[j] = a[0].strip('""')

        # stock_message
        stock_message = []
        for i in range(len(stock)):
            if stock[i] == 'Out of stock':
                stock_message.append('Sorry, the option you have selected is out of stock')
            elif stock[i] == 'Low stock':
                stock_message.append('Selling fast')
            elif stock[i] == 'Unavailable':
                stock_message.append('Unavailable')
            elif stock[i] == 'Available':
                stock_message.append('Delivery within 4 working days')
            else:
                stock_message.append('In Stock')

        # sizes
        print(url3)
        sizes = tree.xpath('//ul[@class="customerSelection"]/li/label/span/text()')
        colours = tree.xpath('//ul[@class="customerSelection"]/li/label/img/@src')
        try:
            if len(colours) > 1:
                for i in range(len(colours)):
                    sizes.pop()
            else:
                sizes.pop()
        except:
            continue

        # links
        #links = tree.xpath('//li[@class="productImageItem"]/a/img/@src')
        links = tree.xpath('//img[@class="product-images__image"]/@src')
        links = join_string(links)

        # size and fit
        Size_Fit = tree.xpath('//span[@itemprop = "description"]/ul[1]/li/text()')
        for i in range(len(Size_Fit)):
            Size_Fit[i] = Size_Fit[i].replace(u'\xa0', u' ').strip(' ')
        # Size_Fit = join_string(Size_Fit)

        # Details
        Details = tree.xpath('//span[@itemprop = "description"]/ul[2]/li/text()')
        for i in range(len(Details)):
            Details[i] = Details[i].replace(u'\xa0', u' ').strip(' ')

        # Material
        Material = tree.xpath('//span[@itemprop = "description"]/ul[3]/li/text()')
        for i in range(len(Material)):
            Material[i] = Material[i].replace(u'\xa0', u' ').strip(' ')

        # ratings
        Ratings = tree.xpath('//a[@class="productRating"]/@title')
        if len(Ratings) > 0:
            Ratings = Ratings[0]
            Ratings = Ratings.split()
            Ratings = Ratings[0]
        else:
            Ratings = '-'

        # reviews
        Reviews = tree.xpath('//a[@class="productRating"]/text()')
        if len(Reviews) > 0:
            Reviews = Reviews[-1]
            Reviews = Reviews.strip()
            Reviews = Reviews.split()
            Reviews = Reviews[0]
        else:
            Reviews = '-'
        try:
            sellname = tree.xpath('//div[contains(text(),"Delivered")]/strong/text()')[0]
        except Exception as e:
            sellname = '-'

        # time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

        #             details_dict['Specifications'] = [{'Size_and_Fit': Size_Fit}, {'Details': Details}, {'Material': Material}]
        Specifications = Size_Fit + Details + Material
        Specifications = join_string(Specifications)
        if len(Specifications) == 0:
            Specifications = '-'

        a = response.text.replace('<!--', '').replace('-->', '')
        tree1 = html.fromstring(a)
        ADIDAS_CODE = tree1.xpath('//span[@id="modelNumber"]/text()')
        ADIDAS_CODE = listToString(ADIDAS_CODE)
        sku_id = "Very_uk" + "_" + Product_url.split('/')[-1].replace('.prd', '')
        # ---- Cache Page Code
        # datazone = datetime.datetime.now()
        f_date = datetime.now().strftime("%d_%m_%Y")
        #f_date = datetime.now().strftime("03_04_2022")
        # strdate = datazone.day
        # strm = datazone.month
        # stry = datazone.year
        pageid = sku_id
        cpid = pageid + '_' + f_date
        cpid = pageid + '_' + f_date
        # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"

        ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Very_UK\\PDP"
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
        # Cache_Page_Link = page_path

        if os.path.exists(sos_filename):
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(saving_data)
        else:
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(saving_data)
        # --------------------
        print((List_price, Promo_price))
        for siz in range(len(sizes)):
            data_dict = {'SKU_ID': sku_id, 'Website': 'Very', 'Country': 'UK', 'RPC': Catalogue_Number,
                         'MPC': ADIDAS_CODE, 'Product_ID': Catalogue_Number, 'Product_URL': Product_url,
                         'Product_Name': Product_Name, 'Category_Path': 'Not Available', 'Specification': Specifications,
                         'Description': Description, 'Currency': 'GBP', 'List_Price': Promo_price,
                         'Promo_Price': List_price,
                         'Discount': Discount, 'Brand': Brand, 'Rating_Count': Ratings, 'Review_Count': Reviews,
                         'Image_URLs': links, 'Variant': sizes[siz], 'Variant_ID': variant_ID_list[siz],
                         'Colour_of_Variant': Colour_Name, 'Colour_Grouping': 'Not Available',
                         'Seller_Name': sellname, 'Stock_Count': 'Not Available',
                         'Stock_Condition': stock[siz], 'Stock_Message': stock_message[siz],
                         'Sustainability_Badge': 'Not Available', 'Reason_Code': 'Success-PF',
                         'Crawling_TimeStamp': date_time,
                         'Cache_Page_Link': page_path,
                         'Extra1': '-', 'Extra2': '-', 'Extra3': '-', 'Extra4': '-', 'Extra5': '-'
                         }
            all_product_data.append(data_dict)
            print(data_dict)
        data_df = pd.DataFrame(all_product_data)
        data_df.to_csv(f'{f_date}-Very_uk1.csv', index=False, encoding="cp1252")

        c = c + 1
        print(c)


df3 = pd.read_excel('urls-1.xlsx')
print(df3)
VERY_UK_SKU(df3)
#https://www.very.co.uk/adidas-originals-retropy-e5-mauve/1600662949.prd

