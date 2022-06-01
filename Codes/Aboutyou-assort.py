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

        general.header_values(["Website","Country","Category ID","Page ID","Category URL","SKU_ID","PDP URL","Date_&_TimeStamp","Cache Page"])

    def initiate(self, input_row, region, proxies_from_tool, thread_name):
        try:

            Website = input_row[0]
            Country = input_row[1]
            Category_ID = input_row[2]
            Category = input_row[3]
            Category1 = input_row[4]

            strurl =Category
            # strid = input_row[1]
            pageid = 1
            page = 0
            bid = general.midtext(Category1,'category]=','&')
            cid = general.midtext(Category1,'brand]=','&')

            for p in range(500):
                page = page + 1
                strurl = 'https://api-cloud.aboutyou.de/v1/products?with=attributes:key(brand|brandLogo|brandAlignment|name|quantityPerPack|plusSize|colorDetail|sponsorBadge|sponsoredType|maternityNursing|exclusive|genderage|specialSizesProduct|materialStyle|sustainabilityIcons|assortmentType|dROPS|brandCooperationBadge|secondHandType),advancedAttributes:key(materialCompositionTextile|siblings),variants,variants.attributes:key(shopSize|categoryShopFilterSizes|cup|cupsize|vendorSize|length|dimension3|sizeType|sort),images.attributes:legacy(false):key(imageNextDetailLevel|imageBackground|imageFocus|imageGender|imageType|imageView),priceRange&filters[category]='+ str(bid) +'&filters[brand]=' + str(cid) +'&filters[excludedFromBrandPage]=false&sortDir=desc&sortScore=brand_scores&sortChannel=web_default&page=' + str(page) + '&perPage=100&campaignKey=00&forceNonLegacySuffix=true&shopId=139'


                for _ in range(20):
                   # data, driver = general.get_url2(strurl,cloak=True,images=True)
                   data, driver = general.get_url(strurl)
                   if data['text']:
                       break
                source = html.fromstring(data['text'])
                time.sleep(2)

                jdata = json.loads(data['text'])
                pjdata = jdata.get('pagination')
                totl = pjdata.get('total')
                lastpage = pjdata.get('last')

                if p > lastpage:
                    break

#--------------------------------cachpage save link-----------------------------------------------
                datazone = datetime.datetime.now()
                f_date = datazone.strftime("%d_%m_%Y")
                strdate = datazone.day
                strm = datazone.month
                stry = datazone.year
                pageid = Category_ID + '_' + str(page)
                cpid = pageid + '_' + str(strdate)+ '_' + str(strm)+ '_' + str(stry)
                ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Aboutyou_de\\ASS"
                sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                if os.path.exists(sos_date_wise_folder):
                    pass
                else:
                    os.mkdir(sos_date_wise_folder)
                sos_filename = sos_date_wise_folder +"\\" + cpid + ".html"
                sos_filename = sos_filename.replace("+", "_").replace("-", "_")
                page_path = sos_filename
                page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\','https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace('//', '/')
                if os.path.exists(sos_filename):
                    with open(sos_filename, 'w', encoding='utf-8') as f:
                        f.write(data['text'])
                else:
                    with open(sos_filename, 'w', encoding='utf-8') as f:
                        f.write(data['text'])

                # pjdata = jdata.get('pagination')
                value = jdata.get('entities')
                if value:
                    for eachval in value:
                        urlid = eachval.get('id')
                        urlname = eachval.get('attributes').get('name').get('values').get('label')
                        catname  = Category.split('/')[-1]
                        skuid = Website + '_' + Country + '_' + str(urlid)
                        url = 'https://www.aboutyou.de/p/' + catname + '/' + str(urlid)
                        crawltime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                        self.push_data2("found", [
                            [Website, Country, Category_ID, pageid, Category, skuid, url, crawltime, page_path, totl]])


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