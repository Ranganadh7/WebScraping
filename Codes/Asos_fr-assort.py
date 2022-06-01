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
# www.asos.com/fr/	FR	asos_fr_002	https://www.asos.com/fr/femme/a-to-z-of-brands/adidas/cat/?cid=5906
# www.asos.com/fr/	FR	asos_fr_003	https://www.asos.com/fr/homme/a-to-z-of-brands/adidas/cat/?cid=7113


class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        super().debug(True)
        print('Crawling started')
        self.base_url = "https://www.aboutyou.de/"
        general.header_values(["Website","Country","Category ID","Page ID","Category URL","SKU_ID","PDP URL","Date_&_TimeStamp","Cache Page"])

    def initiate(self, input_row, region, proxies_from_tool, thread_name):
        Website = input_row[0]
        Country = input_row[1]
        Category_ID = input_row[2]
        Category_url = input_row[3]
        w_array = [Website, Country, Category_ID, Category_url]
        print(w_array)

        for _ in range(25):
           data, driver = general.get_url(Category_url)
           if data['text']:
               print("yes")
               break

        source = html.fromstring(data['text'])
        #------------------------------------SAVE PAGE
        # ------
        datazone = datetime.datetime.now()
        f_date = datazone.strftime("%d_%m_%Y")
        strdate = datazone.day
        strm = datazone.month
        stry = datazone.year
        pageid = Category_ID + '_' + str('1')
        cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
        # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_uk\ASS"
        ASS_folder = f"\\\\ecxus440\\E$\ADIDAS_SavePages\\Asos_FR\\ASS"
        sos_date_wise_folder = ASS_folder + f"\\{f_date}"
        if os.path.exists(sos_date_wise_folder):
            pass
        else:
            os.mkdir(sos_date_wise_folder)
        sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
        sos_filename = sos_filename.replace("+", "_").replace("-", "_")
        page_path = sos_filename
        page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                      'https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace(
            '//', '/')
        if os.path.exists(sos_filename):
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(data['text'])
        else:
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(data['text'])
        #----------------------------------------------
        #------------------FIRST PAGE PRODUCTS
        total_count = general.xpath(source, '//p[@data-auto-id="styleCount"]/text()')
        total_count = total_count.replace('styles trouvés', '').replace(' ', '').strip()

        print(total_count)
        products_urls_list = general.xpath(source, '//div[@data-auto-id="productList"]//a[@class="_3TqU78D"]//@href', mode='set')
        print(('urls', len(products_urls_list)))
        for pro in products_urls_list:
            product_url =  pro
            try:
                rpc = product_url.split('?')[0].split('/')[-1]
            except:
                rpc = '-'
            sku_id = 'Asos_FR_' + rpc
            print((rpc, product_url))

            self.push_data2('found', [[Website, Country, Category_ID, Category_ID+"_"+str(1),
                                       Category_url, sku_id, product_url, time.strftime("%Y-%m-%dT%H:%M:%SZ"), page_path]])

        #-------------------------------------
        num_of_pages = (int(total_count) // 72) + 2
        print(('num of pages', num_of_pages))
        #======================NEXT PAGE SCRIPT
        # i = 2
        for num in range(2, num_of_pages):
            if Category_ID == 'asos_fr_001':
                next_page_url = 'https://www.asos.com/fr/search/?page=' + str(num) + '&q=reebok'
            elif Category_ID == 'asos_fr_002':
                next_page_url = 'https://www.asos.com/fr/femme/a-to-z-of-brands/adidas/cat/?cid=5906&page=' + str(num)
            else:
                next_page_url = 'https://www.asos.com/fr/homme/a-to-z-of-brands/adidas/cat/?cid=7113&page=' + str(num)
            for _ in range (23):
                data1, driver = general.get_url(next_page_url)
                if data1['text']:
                    #general.write_file('foot1.html', data['text'], 'a', encoding='UTF-8')
                    break

            if data1['text']:
                source1 = html.fromstring(data1['text'])
                products_urls_list_1 = general.xpath(source1, '//div[@data-auto-id="productList"]//a[@class="_3TqU78D"]//@href', mode='set')
                for pro_1 in products_urls_list_1:
                    product_url_1 = pro_1
                    try:
                        rpc_1 = product_url.split('?')[0].split('/')[-1]
                    except:
                        rpc_1 = '-'
                    sku_id_1 = 'Asos_FR_' + rpc_1
                    print(('PAGE_NUM==', num, rpc_1, product_url_1))

                    time_2 = time.strftime("%Y-%m-%dT%H:%M:%SZ")
                    # ------------------------------------SAVE PAGE
                    # ------
                    datazone = datetime.datetime.now()
                    f_date = datazone.strftime("%d_%m_%Y")
                    strdate = datazone.day
                    strm = datazone.month
                    stry = datazone.year
                    pageid = Category_ID + '_' + str(num)
                    cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
                    # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_uk\ASS"
                    ASS_folder = f"\\\\ecxus440\\E$\ADIDAS_SavePages\\Asos_FR\\ASS"
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
                    if os.path.exists(sos_filename):
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            f.write(data1['text'])
                    else:
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            f.write(data1['text'])
                    # ----------------------------------------------

                    self.push_data2('found', [
                        [Website, Country, Category_ID, Category_ID + "_" + str(num), next_page_url, sku_id_1, product_url_1,
                         time_2, page_path2]])

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