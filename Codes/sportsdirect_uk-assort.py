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
#SportsDirect	UK	sportsdirect_uk_001	https://www.sportsdirect.com/adidas/view-all-adidas
#SportsDirect	UK	sportsdirect_uk_002	https://www.sportsdirect.com/reebok/all-reebok

#6166

class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        super().debug(True)
        print('Crawling started')
        self.base_url = "https://www.aboutyou.de/"
        general.create_project_dir('firstcry_screenshots_count')
        general.header_values(["Website","Country","Category ID","Page ID","Category URL","SKU_ID","PDP URL","Date_&_TimeStamp","Cache Page"])

    def initiate(self, input_row, region, proxies_from_tool, thread_name):
        try:

            Website = input_row[0]
            Country = input_row[1]
            Category_ID = input_row[2]
            Category = input_row[3]
            w_array = [Website, Country, Category_ID, Category]

            strurl =Category
            # strid = input_row[1]
            pageid = 1
            p_list=[]

            for _ in range(10):
               data, driver = general.get_url(strurl)
               if data['text']:
                   break

            source = html.fromstring(data['text'])
            totalp = '//span[@class="totalProducts"]//text()'
            #------
            datazone = datetime.datetime.now()
            f_date = datazone.strftime("%d_%m_%Y")
            strdate = datazone.day
            strm = datazone.month
            stry = datazone.year
            pageid = Category_ID + '_' + str('1')
            cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
            # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"
            # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_uk\ASS"
            ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Sportsdirect_com\\ASS"
            sos_date_wise_folder = ASS_folder + f"\\{f_date}"
            if os.path.exists(sos_date_wise_folder):
                pass
            else:
                os.mkdir(sos_date_wise_folder)
            sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
            sos_filename = sos_filename.replace("+", "_").replace("-", "_")
            page_path = sos_filename
            page_path = page_path.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\',
                                          'https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace(
                '//', '/')
            if os.path.exists(sos_filename):
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(data['text'])
            else:
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(data['text'])
            t_ele=source.xpath(totalp)
            if t_ele:
                totalp = t_ele[0]
                # totalp = totalp.replace('chevron-right','').replace(".","")

            page_count=general.xpath(source,'//a[@class="swipeNumberClick"][3]//text()')
            print(page_count)
            value = general.xpath(source,'//div[@class="s-producttext-top-wrapper"]/a/@href',mode='set')
            if value:
                # for eachval in value:
                for outer_list in value:
                        url = outer_list
                        url = 'https://www.sportsdirect.com' + url
                        print(url)
                        lastid = url.replace('.html','')
                        lastid = lastid[-13:]
                        skuid = Website + '_' + Country + '_' + lastid
                        self.push_data2("found", [[Website,Country,Category_ID,pageid,Category,skuid, url,datazone,page_path]])


            if page_count:
                category_id=general.xpath(source,'//div[@id="productlistcontainer"]/@data-category')
                split_cat_url=strurl.split("/")
                # i = 2
                #nextpage_link=general.xpath(source,'//a[@class="swipeNextClick NextLink"]/@href')
                for p in range(2,int(page_count)+1):
                    print("PAGE-----",p)
                    nextpage_url=f"https://www.sportsdirect.com/api/productlist/v1/getforcategory?categoryId={category_id}&page={p}&productsPerPage=120&sortOption=rank&selectedFilters=&isSearch=false&searchText=&columns=3&mobileColumns=2&clearFilters=false&pathName=%2F{split_cat_url[-2]}%2{split_cat_url[-1]}&searchTermCategory=&selectedCurrency=GBP&portalSiteId=12&searchCategory="

                    for _ in range(15):
                        data1, driver = general.get_url(nextpage_url)
                        if data1['status_code']==200:
                            break

                    source1 = html.fromstring(data1['text'])
                    value1 = general.xpath(source1,'//div[@class="s-producttext-top-wrapper"]/a/@href',mode='set')
                    #==================================================================
                    datazone = datetime.datetime.now()
                    f_date = datazone.strftime("%d_%m_%Y")
                    strdate = datazone.day
                    strm = datazone.month
                    stry = datazone.year
                    pageid = Category_ID + '_' + str(p)
                    cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
                    # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"
                    # ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Sportsdirect_uk\ASS"
                    ASS_folder = f"\\\\10.100.20.40\\E$\ADIDAS_SavePages\\Sportsdirect_com\\ASS"
                    sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                    if os.path.exists(sos_date_wise_folder):
                        pass
                    else:
                        os.mkdir(sos_date_wise_folder)
                    sos_filename1 = sos_date_wise_folder + "\\" + cpid + ".html"
                    sos_filename1 = sos_filename1.replace("+", "_").replace("-", "_")
                    page_path2 = sos_filename1
                    page_path2 = page_path2.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\',
                                                    'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                           '//').replace(
                        '//', '/')
                    print(page_path2)
                    if os.path.exists(sos_filename1):
                        with open(sos_filename1, 'w', encoding='utf-8') as f:
                            f.write(data['text'])
                    else:
                        with open(sos_filename1, 'w', encoding='utf-8') as f:
                            f.write(data['text'])
                    #===================================================================
                    if data1['text']:
                        load_data = json.loads(data1['text'])
                        product_list=load_data.get('products')
                        for k in product_list:
                            url = k.get('url')
                            url1 = 'https://www.sportsdirect.com' + url
                            print("----",url1)
                            lastid = url1.replace('.html', '')
                            lastid = lastid[-13:]
                            skuid = Website + '_' + Country + '_' + lastid

                            self.push_data2("found", [[Website, Country, Category_ID, pageid, Category, skuid, url1,datazone, page_path2]])


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