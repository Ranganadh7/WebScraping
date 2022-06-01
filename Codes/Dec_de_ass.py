import os
import os
import os
import re
from datetime import datetime,date
import datetime
import random
from lxml import html
import general
from panacea_crawl import spider
import re
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from lxml import html
import general
from panacea_crawl import spider
from datetime import *
from datetime import datetime,date
import re
import json
import time
import time
import datetime
current_path = os.path.dirname(os.path.abspath(__file__))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        super().debug(True)
        print('Crawling started')
        self.base_url = "https://www.firstcry.ae/"
        #general.create_project_dir('firstcry_screenshots_count')
        general.header_values(["Website","Country","Category ID","Page ID","Category URL","SKU_ID","PDP URL","Date_&_TimeStamp","Cache Page"])

    def initiate(self, input_row, region, proxies_from_tool, thread_name):
        try:

            Website = input_row[0]
            Country = input_row[1]
            Category_ID = input_row[2]
            Category = input_row[3]

            strurl =Category
            # strid = input_row[1]
            pageid = 1
            

            for _ in range(20):
               data, driver = general.get_url2(strurl,cloak=True,images=True)
               # data, driver = general.get_url(strurl)
               if data['text']:
                   break
            # source = html.fromstring(data['text'])


            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            source = driver.page_source
            source = html.fromstring(source)
#--------------------------------cachpage save link-----------------------------------------------
            datazone = datetime.datetime.now()
            #f_date = datazone.strftime("%d_%m_%Y")
            f_date = datazone.strftime("14_05_2022")
            strdate = datazone.day
            strm = datazone.month
            stry = datazone.year
            pageid = Category_ID + '_' + str('1')
            #f_date = '28_02_2022'
            cpid = pageid + '14_05_2022'
            #cpid = pageid + '_' + str(f_date)
            # cpid = pageid + '_' + str(strdate)+ '_' + str(strm)+ '_' + str(stry)
            # ASS_folder = f"E:\ADIDAS_SavePages\Zalando_DE\ASS"
            ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Decathlon_de\ASS"
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
            totalp = general.xpath(source,'//nav[@class="svelte-18kvb4z"]',mode='tc')
            if totalp:
                totalp = totalp.split(' ')[-1]
                totalp = totalp.replace('chevron-right','')
            rank = 1#
            #value = general.xpath(source,'//a[@class="dpb-product-model-link svelte-d5pqmr"]//@href',mode='set')
            value = general.xpath(source, '//a[@class="dpb-product-model-link svelte-oxwwyr"]//@href', mode='set')
            print(('products count', value))
            if value:
                for eachval in value:
                    url = eachval
                    rank = rank + 1
                    if 'zalando' not in url.lower():
                        url = 'https://www.decathlon.de/' + url
                    # lastid = url.replace('.html','')
                    # lastid = lastid[-13:]
                    lastid = url.split('=')[-1]
                    skuid = Website + '_' + Country + '_' + lastid
                    time = datetime.datetime.now()
                    dt_string = time.strftime("%Y-%m-%dT%H:%M:%SZ")
                    self.push_data2("found", [[Website,Country,Category_ID,pageid,Category,skuid, url,dt_string,page_path]])
                    print("Success")

            totalp = int(totalp)
            if int(totalp) > 1:
                m = 40
                i=1
                # for p in range(totalp+1):
                for p in range(totalp + 1):
                    strurl1 = strurl + '&from=' + str(m) +'&size=40'
                    m = m + 40
                    # if i > int(totalp):
                    #     break

                    for _ in range(20):
                        data, driver = general.get_url2(strurl1, cloak=True, images=True)
                        if data['text']:
                            break
                    # source = html.fromstring(data['text'])

                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    source = driver.page_source
                    source = html.fromstring(source)
                    pageid = Category_ID + '_' + str(i)
                    i = i + 1
                    cpid = pageid + '_' + str(strdate)+ '_' + str(strm)+ '_' + str(stry)
                    #f_date = '28_02_2022'
                    cpid = pageid + '_' + str(f_date)
                    ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Decathlon_de\ASS"
                    sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                    if os.path.exists(sos_date_wise_folder):
                        pass
                    else:
                        os.mkdir(sos_date_wise_folder)
                    sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
                    sos_filename = sos_filename.replace("+", "_").replace("-", "_")
                    page_path = sos_filename
                    page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                                  'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                         '//').replace(
                        '//', '/')
                    if os.path.exists(sos_filename):
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            f.write(data['text'])
                    else:
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            f.write(data['text'])

                    #value = general.xpath(source,'//a[@class="dpb-product-model-link svelte-1qosgs4"]/@href',mode='set')
                    value=general.xpath(source,'//a[@class="dpb-product-model-link svelte-oxwwyr"]//@href',mode='set')
                    if value:
                        for eachval in value:
                            url = eachval
                            rank = rank + 1
                            if 'zalando' not in url.lower():
                                url = 'https://www.decathlon.de/' + url
                            # lastid = url.replace('.html', '')
                            # lastid = general.midtext(url,'mc=','_')
                            lastid = url.split('=')[-1]
                            skuid = Website + '_' + Country + '_' + lastid
                            time = datetime.datetime.now()
                            dt_string = time.strftime("%Y-%m-%dT%H:%M:%SZ")
                            self.push_data2("found", [[Website, Country, Category_ID, pageid, Category, skuid, url,dt_string, page_path]])

            try:
                cat_id = ''
                # cat_id = cat_id.replace(" & ", "_")
                # cat_id = cat_id.replace(" ", "_")
                # ss_name = cat_id + '_' + '_' + total_prod + '_' + time.strftime("%Y%m%d_%H%M") + '.png'
                # driver.save_screenshot('./firstcry_screenshots_count/' + ss_name)
            except Exception as e:
                self.push_data2("tag_failed", [[url, url]])


        except Exception as err:
            self.push_data2("tag_failed",[[self.url, self.url]])

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