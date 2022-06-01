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


class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        super().debug(True)
        print('Crawling started')
        self.base_url = "https://www.firstcry.ae/"
        general.create_project_dir('firstcry_screenshots_count')
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
               # data, driver = general.get_url2(strurl,cloak=True,images=True)
               data, driver = general.get_url(strurl)
               if data['text']:
                   break
            source = html.fromstring(data['text'])
            time.sleep(3)
            # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            # source = driver.page_source
            # source = html.fromstring(source)
#--------------------------------cachpage save link-----------------------------------------------
            datazone = datetime.datetime.now()
            f_date = datazone.strftime("%d_%m_%Y")
            strdate = datazone.day
            strm = datazone.month
            stry = datazone.year
            pageid = Category_ID + '_' + str('1')
            cpid = pageid + '_' + str(strdate)+ '_' + str(strm)+ '_' + str(stry)
            # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"
            # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Jdsports_uk\ASS"
            ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Jdsports_uk\ASS"
            sos_date_wise_folder = ASS_folder + f"\\{f_date}"
            if os.path.exists(sos_date_wise_folder):
                pass
            else:
                os.mkdir(sos_date_wise_folder)
            sos_filename = sos_date_wise_folder +"\\" + cpid + ".html"
            sos_filename = sos_filename.replace("+", "_").replace("-", "_")
            page_path = sos_filename
            page_path = page_path.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\','https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace('//', '/')
            if os.path.exists(sos_filename):
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(data['text'])
            else:
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(data['text'])


            totalp = general.xpath(source,'//div[@class="pageCount"]',mode='tc')
            if totalp:
                totalp = totalp.split(' ')[0]
                totalp = totalp.replace('Products:','').strip()

            value = general.xpath(source,'//span[@class="itemContainer"]/a/@href',mode='set')
            if value:
                for eachval in value:
                    url = eachval
                    if 'zalando' not in url.lower():
                        url = 'https://www.jdsports.co.uk' + url
                    lastid = url.replace('.html','')
                    lastid = lastid.split('/')[-2]
                    skuid = Website + '_' + Country + '_' + lastid
                    crawltime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                    self.push_data2("found", [[Website,Country,Category_ID,pageid,Category,skuid, url,crawltime,page_path]])


            if int(totalp) > 1:
                i = 2
                l = 72
                # for p in range(totalp+1):
                for p in range(500):
                    strurl1 = strurl + '?from=' + str(l)
                    if l > int(totalp):
                        break
                    for _ in range(20):
                        # data, driver = general.get_url2(strurl1, cloak=True, images=True)
                        data, driver = general.get_url(strurl1)
                        if data['text']:
                            break
                    source = html.fromstring(data['text'])
                    time.sleep(3)
                    # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    # source = driver.page_source
                    # source = html.fromstring(source)
                    pageid = Category_ID + '_' + str(i)
                    i = i + 1
                    l = l + 72
                    cpid = pageid + '_' + str(strdate)+ '_' + str(strm)+ '_' + str(stry)
                    # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Jdsports_uk\ASS"
                    ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Jdsports_uk\ASS"
                    sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                    if os.path.exists(sos_date_wise_folder):
                        pass
                    else:
                        os.mkdir(sos_date_wise_folder)
                    sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
                    sos_filename = sos_filename.replace("+", "_").replace("-", "_")
                    page_path = sos_filename
                    page_path = page_path.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\',
                                                  'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                         '//').replace(
                        '//', '/')
                    if os.path.exists(sos_filename):
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            # f.write(str(source))
                            f.write(data['text'])
                    else:
                        with open(sos_filename, 'w', encoding='utf-8') as f:
                            # f.write(str(source))
                            f.write(data['text'])

                    value = general.xpath(source,'//span[@class="itemContainer"]/a/@href',mode='set')
                    if value:
                        for eachval in value:
                            url = eachval
                            if 'zalando' not in url.lower():
                                url = 'https://www.jdsports.co.uk' + url
                            lastid = url.replace('.html', '')
                            lastid = lastid.split('/')[-2]
                            skuid = Website + '_' + Country + '_' + lastid
                            crawltime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                            self.push_data2("found", [[Website, Country, Category_ID, pageid, Category, skuid, url,crawltime, page_path]])

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