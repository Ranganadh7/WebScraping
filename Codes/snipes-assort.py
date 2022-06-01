import os
from lxml import html
import general
from panacea_crawl import spider
from datetime import *
import re
import json
import time
import datetime
current_path = os.path.dirname(os.path.abspath(__file__))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Snipes	DE	snipes_de_001	https://www.snipes.com/search?q=adidas&lang=de_DE
#Snipes	DE	snipes_de_002	https://www.snipes.com/search?q=reebok&lang=de_DE



class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        super().debug(True)
        print('Crawling started')
        self.base_url = "https://www.aboutyou.de/"
        general.header_values(["Website","Country","Category ID","Page ID","Category URL","SKU_ID","PDP URL","Date_&_TimeStamp","Cache Page"])

    def initiate(self, input_row, region, proxies_from_tool, thread_name):
        Website = input_row[0].upper()
        Country = input_row[1]
        Category_ID = input_row[2]
        Category_url = input_row[3]
        w_array = [Website, Country, Category_ID, Category_url]

        for _ in range(25):
           data, driver = general.get_url(Category_url)
           if data['text']:
               #general.write_file('snipes.html', data['text'], 'a', encoding='UTF-8')
               break

        # ------------------------------------SAVE PAGE
        # ------
        datazone = datetime.datetime.now()
        f_date = datazone.strftime("%d_%m_%Y")
        strdate = datazone.day
        strm = datazone.month
        stry = datazone.year
        pageid = Category_ID + '_' + str(1)
        cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
        # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_uk\ASS"
        ASS_folder = f"\\\\ecxus440\\E$\ADIDAS_SavePages\\Snipes_DE\\ASS"
        sos_date_wise_folder = ASS_folder + f"\\{f_date}"
        if os.path.exists(sos_date_wise_folder):
            pass
        else:
            os.mkdir(sos_date_wise_folder)
        sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
        sos_filename = sos_filename.replace("+", "_").replace("-", "_")
        page_path = sos_filename
        page_path2 = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                      'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                             '//').replace(
           '//', '/')
        print(page_path2)
        if os.path.exists(sos_filename):
           with open(sos_filename, 'w', encoding='utf-8') as f:
               f.write(data['text'])
        else:
           with open(sos_filename, 'w', encoding='utf-8') as f:
               f.write(data['text'])
    # ----------------------------------------------
        source = html.fromstring(data['text'])
        #------------------FIRST PAGE PRODUCTS
        p_count = general.xpath(source, '//div[@data-cmp="gridQuantity"]//span/text()')
        print(p_count)
        p_count = p_count.replace('Ergebnisse', '').strip()
        products_count = int(p_count)
        num_of_pages = (products_count // 48) + 2
        print((products_count, num_of_pages))
        #https://www.snipes.com/search?q=adidas&lang=de_DE&sz=96
        products_urls_list = general.xpath(source, '//a[@class="b-product-tile-body-link"]', mode='set')
        print(len(products_urls_list))
        for pro in products_urls_list:
            product_url = 'https://www.snipes.com' + general.xpath(pro, './@href')
            try:
                rpc = product_url.split('-')[-1]
                rpc = rpc.replace('.html', '')
            except:
                rpc = '-'
            sku_id = 'snipes.de=' + rpc
            print((rpc, product_url))

            self.push_data2('found', [[Website, Country, Category_ID, Category_ID+"_"+str(1),
                                       Category_url, sku_id, product_url, time.strftime("%Y-%m-%dT%H:%M:%SZ"), page_path2]])

        #-------------------------------------

        #======================NEXT PAGE SCRIPT


    def xpath_check(self, source, xpath, loc=0, mode='t'):
        text = ''
        try:
            element = source.xpath(xpath)
            if len(element):
                if mode == 'tc':
                    text = re.sub('\s+', ' ', element[loc].text_content().strip())
                    text = re.sub('\\n|\\r', '', element[loc].text_content().strip())
                elif mode == 'set':
                    text = element
                else:
                    text = re.sub('\s+', ' ', element[loc]).strip()
                    text = re.sub('\\n|\\r', '', element[loc]).strip()
        except Exception as e:
            print(e, xpath)
        return text

    def clean(self, text):
        text = re.sub('\s+', ' ', text.strip())
        text = re.sub('\\n|\\r', '', text.strip())
        return text


crawl = Crawler(current_path)
crawl.start(crawl.initiate)