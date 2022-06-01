import os
from lxml import html
import scrapy
import requests, re, json
from scrapy.cmdline import execute
from scrapy.http import HtmlResponse
import pandas as pd
import time
import hashlib
import general
import random

ip_addresses = ['154.28.67.106','154.28.67.111','154.28.67.116','154.28.67.117','154.28.67.125','154.28.67.131','154.28.67.133','154.28.67.142','154.28.67.156','154.28.67.163','154.28.67.173','154.28.67.18','154.28.67.182','154.28.67.184','154.28.67.20','154.28.67.200','154.28.67.210','154.28.67.218','154.28.67.222','154.28.67.223','154.28.67.231','154.28.67.240','154.28.67.243','154.28.67.253','154.28.67.39','154.28.67.4','154.28.67.49','154.28.67.5','154.28.67.61','154.28.67.80','154.28.67.81','154.28.67.87','154.28.67.88','154.28.67.96','154.28.67.99','154.7.230.100','154.7.230.101','154.7.230.103','154.7.230.107','154.7.230.109','154.7.230.130','154.7.230.132','154.7.230.14','154.7.230.140','154.7.230.147','154.7.230.151','154.7.230.156','154.7.230.163','154.7.230.170','154.7.230.18','154.7.230.183','154.7.230.188','154.7.230.189','154.7.230.19','154.7.230.190','154.7.230.198','154.7.230.204','154.7.230.209','154.7.230.235','154.7.230.238','154.7.230.246','154.7.230.29','154.7.230.41','154.7.230.42','154.7.230.51','154.7.230.55','154.7.230.60','154.7.230.61','154.7.230.74','154.7.230.82','154.7.230.89','23.131.8.112','23.131.8.115','23.131.8.117','23.131.8.12','23.131.8.121','23.131.8.124','23.131.8.150','23.131.8.161','23.131.8.166','23.131.8.171','23.131.8.173','23.131.8.176','23.131.8.177','23.131.8.181','23.131.8.19','23.131.8.192','23.131.8.194','23.131.8.199','23.131.8.202','23.131.8.203','23.131.8.204','23.131.8.207','23.131.8.209','23.131.8.213','23.131.8.216','23.131.8.225','23.131.8.228','23.131.8.231','23.131.8.238','23.131.8.254','23.131.8.36','23.131.8.5','23.131.8.76','23.131.8.93','23.131.8.95','23.131.8.99','23.131.88.105','23.131.88.12','23.131.88.137','23.131.88.139','23.131.88.140','23.131.88.145','23.131.88.150','23.131.88.151','23.131.88.153','23.131.88.154','23.131.88.156','23.131.88.165','23.131.88.18','23.131.88.191','23.131.88.192','23.131.88.194','23.131.88.198','23.131.88.202','23.131.88.206','23.131.88.220','23.131.88.223','23.131.88.228','23.131.88.233','23.131.88.24','23.131.88.242','23.131.88.244','23.131.88.47','23.131.88.63','23.131.88.67','23.131.88.73','23.131.88.80','23.131.88.81','23.131.88.82','23.131.88.88','23.131.88.97','23.170.144.149','23.170.144.209','23.170.144.212','23.170.144.242','23.170.144.83','23.170.145.117','23.170.145.167','23.170.145.182','23.170.145.19','23.170.145.203','23.226.17.101','23.226.17.109','23.226.17.112','23.226.17.113','23.226.17.115','23.226.17.123','23.226.17.129','23.226.17.143','23.226.17.148','23.226.17.165','23.226.17.186','23.226.17.199','23.226.17.201','23.226.17.207','23.226.17.210','23.226.17.219','23.226.17.220','23.226.17.222','23.226.17.229','23.226.17.250','23.226.17.254','23.226.17.26','23.226.17.33','23.226.17.4','23.226.17.49','23.226.17.5','23.226.17.55','23.226.17.66','23.226.17.7','23.226.17.72','23.226.17.78','23.226.17.8','23.226.17.86','23.226.17.90','23.226.17.93','23.230.177.105','23.230.177.110','23.230.177.113','23.230.177.121','23.230.177.130','23.230.177.14','23.230.177.143','23.230.177.15','23.230.177.150','23.230.177.154','23.230.177.165','23.230.177.173','23.230.177.191','23.230.177.196','23.230.177.203','23.230.177.206','23.230.177.208','23.230.177.217','23.230.177.220','23.230.177.221','23.230.177.224','23.230.177.228','23.230.177.231','23.230.177.235','23.230.177.237','23.230.177.241','23.230.177.27','23.230.177.38','23.230.177.52','23.230.177.61','23.230.177.67','23.230.177.72','23.230.177.80','23.230.177.88','23.230.177.94','23.230.177.99','23.230.197.103','23.230.197.106','23.230.197.109','23.230.197.11','23.230.197.12','23.230.197.122','23.230.197.124','23.230.197.146','23.230.197.155','23.230.197.156','23.230.197.174','23.230.197.179','23.230.197.181','23.230.197.196','23.230.197.2','23.230.197.201','23.230.197.207','23.230.197.208','23.230.197.225','23.230.197.227','23.230.197.233','23.230.197.236','23.230.197.239','23.230.197.240','23.230.197.244','23.230.197.251','23.230.197.50','23.230.197.52','23.230.197.54','23.230.197.60','23.230.197.71','23.230.197.80','23.230.197.81','23.230.197.84','23.230.197.97','23.230.74.102','23.230.74.110','23.230.74.116','23.230.74.125','23.230.74.133','23.230.74.135','23.230.74.14','23.230.74.141','23.230.74.149','23.230.74.15','23.230.74.157','23.230.74.16','23.230.74.170','23.230.74.172','23.230.74.174','23.230.74.183','23.230.74.187','23.230.74.19','23.230.74.198','23.230.74.208','23.230.74.212','23.230.74.215','23.230.74.23','23.230.74.230','23.230.74.231','23.230.74.252','23.230.74.30','23.230.74.41','23.230.74.57','23.230.74.58','23.230.74.59','23.230.74.6','23.230.74.75','23.230.74.81','23.230.74.88','23.230.74.91','23.27.222.108','23.27.222.109','23.27.222.134','23.27.222.138','23.27.222.159','23.27.222.161','23.27.222.164','23.27.222.166','23.27.222.178','23.27.222.19','23.27.222.195','23.27.222.201','23.27.222.202','23.27.222.203','23.27.222.208','23.27.222.21','23.27.222.211','23.27.222.218','23.27.222.223','23.27.222.228','23.27.222.234','23.27.222.236','23.27.222.242','23.27.222.251','23.27.222.253','23.27.222.34','23.27.222.61','23.27.222.62','23.27.222.69','23.27.222.70','23.27.222.72','23.27.222.73','23.27.222.74','23.27.222.81','23.27.222.93','38.131.131.110','38.131.131.114','38.131.131.123','38.131.131.125','38.131.131.137','38.131.131.142','38.131.131.145','38.131.131.147','38.131.131.15','38.131.131.154','38.131.131.16','38.131.131.17','38.131.131.173','38.131.131.18','38.131.131.193','38.131.131.204','38.131.131.207','38.131.131.227','38.131.131.229','38.131.131.233','38.131.131.238','38.131.131.246','38.131.131.248','38.131.131.250','38.131.131.31','38.131.131.36','38.131.131.50','38.131.131.58','38.131.131.64','38.131.131.70','38.131.131.71','38.131.131.74','38.131.131.83','38.131.131.94','38.131.131.99','38.75.75.104','38.75.75.111','38.75.75.112','38.75.75.119','38.75.75.120','38.75.75.123','38.75.75.127','38.75.75.139','38.75.75.14','38.75.75.143','38.75.75.155','38.75.75.156','38.75.75.158','38.75.75.170','38.75.75.179','38.75.75.188','38.75.75.2','38.75.75.201','38.75.75.231','38.75.75.232','38.75.75.241','38.75.75.246','38.75.75.251','38.75.75.26','38.75.75.29','38.75.75.4','38.75.75.44','38.75.75.49','38.75.75.56','38.75.75.58','38.75.75.62','38.75.75.72','38.75.75.76','38.75.75.79','38.75.75.88','38.96.156.108','38.96.156.112','38.96.156.128','38.96.156.131','38.96.156.14','38.96.156.142','38.96.156.143','38.96.156.149','38.96.156.16','38.96.156.163','38.96.156.165','38.96.156.169','38.96.156.186','38.96.156.188','38.96.156.190','38.96.156.192','38.96.156.194','38.96.156.199','38.96.156.218','38.96.156.236','38.96.156.240','38.96.156.252','38.96.156.28','38.96.156.32','38.96.156.35','38.96.156.56','38.96.156.57','38.96.156.6','38.96.156.67','38.96.156.77','38.96.156.80','38.96.156.83','38.96.156.84','38.96.156.89','38.96.156.92','45.238.157.100','45.238.157.104','45.238.157.106','45.238.157.110','45.238.157.116','45.238.157.118','45.238.157.119','45.238.157.12','45.238.157.123','45.238.157.132','45.238.157.14','45.238.157.149','45.238.157.15','45.238.157.183','45.238.157.186','45.238.157.189','45.238.157.2','45.238.157.212','45.238.157.214','45.238.157.217','45.238.157.22','45.238.157.228','45.238.157.23','45.238.157.247','45.238.157.43','45.238.157.48','45.238.157.51','45.238.157.52','45.238.157.53','45.238.157.56','45.238.157.61','45.238.157.65','45.238.157.72','45.238.157.79','45.238.157.8','45.238.159.103','45.238.159.107','45.238.159.110','45.238.159.114','45.238.159.116','45.238.159.123','45.238.159.126','45.238.159.144','45.238.159.148','45.238.159.15','45.238.159.156','45.238.159.165','45.238.159.167','45.238.159.183','45.238.159.20','45.238.159.208','45.238.159.217','45.238.159.220','45.238.159.23','45.238.159.230','45.238.159.235','45.238.159.237','45.238.159.238','45.238.159.24','45.238.159.249','45.238.159.251','45.238.159.32','45.238.159.34','45.238.159.51','45.238.159.6','45.238.159.66','45.238.159.77','45.238.159.79','45.238.159.82','45.238.159.91']

user_pass = "csimonra:h19VA2xZ"
port = "29842"


def join_string1(list_string):
    # Join the string based on '-' delimiter
    string = ' | '.join(list_string)
    return string

def join_string2(list_string):
    # Join the string based on '-' delimiter
    string = ': '.join(list_string)
    return string

product_details = []
# excel_data = pd.read_csv('NetShoesSKU.csv')
excel_data = pd.read_csv('input-1.csv')
p_rpc = excel_data['PDP_URL']
# p_rpc = excel_data['Input_URL']

for pp_url in p_rpc:

    headers = {
        'authority': 'www.decathlon.es',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Cookie': 'incap_ses_706_989893=bFiQYsOLVjWkeJXC4DfMCWdlPmIAAAAAeKPWXjMBwcdE3GqfKRtV1Q==; incap_ses_707_989893=7MpDM4nhI2gWWGu8YcXPCbRlPmIAAAAAzuA2NMbiFlsxfhEJ6ozIog==; visid_incap_989893=K6aROiYLShOkGSqNR07i36RkPmIAAAAAQUIPAAAAAAB3IrT+iW7Rw5TH8MpXRwoN'
    }
    sku_url = pp_url
    print(sku_url)
    #sku_url = 'https://www.decathlon.es/es/p/camiseta-fitness-adidas-mujer-rosa/_/R-p-X8661624?mc=8661624&_adin=11551547647'
    for _ in range(30):
        proxy = random.randint(0, len(ip_addresses) - 1)
        proxies = {"http": "https://" + user_pass + "@" + ip_addresses[proxy] + ":" + port,
                   "https": "http://" + user_pass + "@" + ip_addresses[proxy] + ":" + port}
        try:
            res = requests.request("GET", sku_url, headers=headers, proxies=proxies)
            if res.status_code == 200:
                print(res.status_code)
                break
        except:
            continue
    response = HtmlResponse(url=sku_url, body=res.content)
    tree = html.fromstring(res.text)
    data = ''.join(response.xpath('//*[@type="application/json"]/text()').extract()).strip()
    # data2 = json.dumps(data).replace('\\', '').strip('"').strip()
    if data == '':
        data = ''
    else:
        file_data= json.loads(data)

        try:
            page_id = rpc_code = str(file_data['_ctx']['data'][4]['input']['modelId'])
            node_server_dir = "\\\\ecxus440\\E$\\ADIDAS_SavePages\\"
            current_directory = node_server_dir

            # current_directory = os.getcwd()
            website_dir = os.path.join(current_directory, r'Decathlon_ES')
            scrape_format_dir = os.path.join(website_dir, r'PDP')
            date_wise_dir = os.path.join(scrape_format_dir, str(time.strftime("%d_%m_%Y")))
            #date_wise_dir = os.path.join(scrape_format_dir, str(time.strftime("21_04_2022")))
            if not os.path.exists(date_wise_dir):
                os.makedirs(date_wise_dir)

            cache_page_path = date_wise_dir + "\\" + page_id + "_" + time.strftime("%d_%m_%Y") + ".html"
            #cache_page_path = date_wise_dir + "\\" + page_id + "_" + time.strftime("21_04_2022") + ".html"
            with open(cache_page_path, 'wb') as f:
                f.write(response.body)
                f.close()

            # cache_page_path = cache_page_path.replace('C:\\Project\\Adidas\\',
            #                 'https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace('//', '/')

            cache_page_path = cache_page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                                      'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                             '//').replace(
                '//', '/')
            print(cache_page_path)
        except Exception as e:
            cache_page_path = ''
            print("Exception occurred : ", e)

        try:
            p_name = file_data['_ctx']['data'][4]['data']['webLabel']
        except Exception as e:
            p_name = ''
            print(e)

        try:
            brand = file_data['_ctx']['data'][4]['data']['brand']['label']
        except Exception as e:
            brand = ''
            print(e)

        try:
            category = '/'.join(response.xpath('//*[@class="breadcrumbs svelte-f8j1pd"]//li//a//text()').extract()).strip()
        except Exception as e:
            category = ''
            print(e)

       # list_price = ''
        try:
            list_price = ''.join(response.xpath('//*[@class="product-summary svelte-1ghvio2"]//div[@class="prc__cartridge  svelte-1rx7yel"]//div/div/span[@class="prc__previous svelte-1rx7yel"]/text()').extract()).strip()
        except Exception as e:
            list_price = ''
            print(e)

        if list_price == '':
            list_price = ''.join(response.xpath('//*[@class="product-summary svelte-1ghvio2"]//div[@class="prc__cartridge  svelte-1rx7yel"]//div/text()').extract()).strip()

        try:
            promo_price = ''.join(response.xpath('//*[@class="product-summary svelte-1ghvio2"]//div[@class="prc__cartridge  svelte-1rx7yel"]//div/text()').extract()).strip()
        except Exception as e:
            promo_price = ''
            print(e)
        if promo_price == '':
            promo_price = ''.join(response.xpath('//*[@class="product-summary svelte-1ghvio2"]//div[@class="prc__cartridge  svelte-1rx7yel"]//div/div/span[@class="prc__previous svelte-1rx7yel"]/text()').extract()).strip()
        else:
            promo_price = '-'

        discount_price = ''
        try:
            discount_price = ''.join(response.xpath(
                '//*[@class="product-summary svelte-1ghvio2"]//div[@class="prc__cartridge  svelte-1rx7yel"]//div/div/span[@class="prc__rate svelte-1rx7yel"]/text()').extract()).strip()
        except Exception as e:
            discount_price = ''
            print(e)

        if discount_price == '':
            discount_price = '-'
       #================================
        #discount = general.xpath(tree, '//div[@class="product-summary-price  svelte-1xqtxw5"]//span[@class="prc__rate svelte-rppk6w"]/text()')
        discount=general.xpath(tree,'//div[@class="product-summary-price  svelte-qcr7co"]//span[@class="prc__previous svelte-ay5r8q"]/text()')

        discount_price = discount
        print(discount)
        if discount !='':
            promo_price = general.xpath(tree,'//div[@class="prc__active-price svelte-ay5r8q prc__active-price--sale"]/@data-price')
            list_price = general.xpath(tree, '//span[@class="prc__previous svelte-ay5r8q"]/text()')
        else:
            promo_price = general.xpath(tree, '//div[@class="product-summary-price  svelte-qcr7co"]//div[@class="prc__active-price svelte-ay5r8q"]/@data-price')
            list_price = promo_price
        print((list_price, promo_price, discount_price))
        #====================================
        try:
            images = []
            ima = len(file_data['_ctx']['data'][4]['data']['models'][0]['images']['product'])
            for im in range(int(ima)):
                imag = file_data['_ctx']['data'][4]['data']['models'][0]['images']['product'][im]['media']['resource']
                images.append(imag)
            image = '|'.join(images)
        except Exception as e:
            image = ''
            print(e)

        try:
            color_variant = ''.join(response.xpath('//*[contains(text(),"Color:")]//following-sibling::span/text()').extract()).strip()
        except Exception as e:
            color_variant = ''
            print(e)

        if color_variant == '':
            color_variant = '-'

        try:
            group_color = '|'.join(response.xpath('//*[@role="radiogroup"]//button/@aria-label').extract())
        except Exception as e:
            group_color = ''
            print(e)
        if group_color == '':
            group_color = '-'

        try:
            product_url = ''.join(response.xpath('//*[@rel="canonical"]/@href').extract())
        except Exception as e:
            product_url = ''
            print(e)

        try:
            # p_code = file_data['sku']
            # product_code = '-'.join(p_code.split('-')[:-1])
            rpc_code = ''.join(response.xpath('//*[@class="product-summary-model-code svelte-qcr7co"]/span/text()').extract())
            if rpc_code == '':
                rpc_code = str(file_data['_ctx']['data'][4]['input']['modelId'])
        except Exception as e:
            # product_code = ''
            rpc_code = ''
            print(e)

        rating = ''
        reviews = ''
        try:
            rating = ''.join(response.xpath('//*[@class="svelte-1d39ptv"]/text()').extract())
            reviews = ''.join(response.xpath('//*[@class="count svelte-1d39ptv"]/text()').extract()).replace('Opiniones','').strip()
        except Exception as e:
            reviews = ''
            rating = ''
            print(e)

        if rating == '':
            rating = '-'
        if reviews == '':
            reviews = '-'

        try:
            stock_details = ''.join(response.xpath('//*[@id="addToBasket"]/@title').extract())
        except Exception as e:
            stock_details = ''
            print(e)

        # try:
        #     description = ''.join(response.xpath('//*[@class="product-description svelte-1ghvio2"]/text()').extract())
        # except Exception as e:
        #     description = ''
        #     print(e)
        try:
            description = general.xpath(tree, '//div[@class="product-summary-infos svelte-qcr7co"]/p', mode='set_tc', sep=' ')
        except:
            description = '-'
        print(description)

        try:
            specification = general.xpath(tree,'//p[@class="svelte-xqr10u"]/text()',mode='set_tc',sep=' ')
        except Exception as e:
            specification = ''
            print(e)
        if specification == '':
            specification = '-'
        try:
            if 'Disponible' not in response.text:
                stock_Condition = 'Out_of_Stock'
            else:
                stock_Condition = 'InStock'
        except Exception as e:
            stock_Condition = ''
            print(e)

        try:
            seller_info = ''
        except Exception as e:
            seller_info = ''
            print(e)

        if seller_info == '':
            seller_info = '-'

        try:
            vart = []
            vartid = []
            var = len(file_data['_ctx']['data'][4]['data']['models'][0]['skus'])
            for vi in range(int(var)):
                vat = file_data['_ctx']['data'][4]['data']['models'][0]['skus'][vi]['size']
                vart.append(vat)
                vatid = file_data['_ctx']['data'][4]['data']['models'][0]['skus'][vi]['skuId']
                vartid.append(vatid)
            variants = vart
            variant_id = vartid

        except Exception as e:
            variants = ''
            variant_id = ''
            print(e)

        for var, var_id in zip(variants,variant_id):

            product_data = {
                'SKU_ID': 'decathlon_es_'+rpc_code,
                'Website_Name' : 'www.decathlon.es',
                'Country' : 'ES',
                'RPC' : rpc_code,
                'MPC' : 'Not Available',
                'Product_ID': rpc_code,
                'Product_URL': product_url,
                'Product_Name': p_name,
                'Category_Path': category,
                'Specification': specification,
                'Description': description,
                'Currency': 'BRL',
                'List_Price': list_price,
                'Promo_Price': promo_price,
                'Discount': discount_price,
                'Brand': brand,
                'Rating_Count': rating,
                'Review_Count': reviews,
                'Image_URLs': image,
                'Variant': var,
                'Variant_ID': var_id,
                'Colour_of_Variant': color_variant,
                'Colour_Grouping': group_color,
                'Seller_Name': 'Not Available',
                'Stock_Count': 'Not Available',
                'Stock_Condition': stock_Condition,
                'Stock_Message': 'Not Available',
                'Sustainability_Badge': 'Not Available',
                'Reason_Code': 'Success-PF',
                'Crawling_TimeStamp': time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                'Cache_Page_Link': cache_page_path,
                'Extra1': '-',
                'Extra2': '-',
                'Extra3': '-',
                'Extra4': '-',
                'Extra5': '-'
            }
            print(product_data)
            data_dict_copy = product_data.copy()
            product_details.append(data_dict_copy)

    data_df = pd.DataFrame(product_details)
    data_df.to_csv(r"decathlon_ES-1.csv", encoding="utf-8-sig")

