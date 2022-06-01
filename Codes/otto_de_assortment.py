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
            Category_URL = input_row[3]

            strurl =Category_URL
            for _ in range(20):
               # data, driver = general.get_url2(strurl,cloak=True,images=True)
               data, driver = general.get_url(strurl)
               if data['text']:
                   break
            source = html.fromstring(data['text'])
            # time.sleep(3)
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
            ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Otto_DE\ASS"
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
            #general.xpath(source,'//div[@class="pageCount"]',mode='tc')
            prod = general.xpath(source,'//strong[@class="nav_grimm-breadcrumb-headline__count"]',mode='tc')
            prod_count = re.findall(r'(\d+)',str(prod))[0]
            article = general.xpath(source,'//*[@id="san_resultSection"]//article/@data-variation-id',mode='set')
            article_tag = general.xpath(source,'//*[@id="san_resultSection"]//article/@class',mode='set')
            # for xy in range(1,5):
            for vid, ar in zip(article, article_tag):
                print(vid)
                print(ar)
                v_url = f'https://www.otto.de/cricket/tile/{str(vid)}'
                try:
                    for _ in range(20):
                        # data, driver = general.get_url2(strurl,cloak=True,images=True)
                        data1, driver1 = general.get_url(v_url)
                        if data1['text']:
                            break
                        else:
                            continue
                    source1 = html.fromstring(data1['text'])
                    d1 = str(data1['text']).split('<script type="application/ld+json">')[-1].split('</script>')[0]
                    jd1 = json.loads(d1)
                    try:
                        product_url = 'https://www.otto.de' + str(jd1['url'])
                    except:
                        product_url = '-'
                    if product_url!='-':
                        pageid = Category_ID+'_1'
                        sku=str(product_url).split('/')[-2].split('-')[-1]
                        skuid = Website + '_' + Country + '_' + sku
                        crawltime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                        data12 = {'Website': Website, 'Country': Country,
                                 'Category ID': Category_ID, 'Page ID': pageid,
                                 'Category URL': Category_URL, 'SKU_ID': skuid,
                                 'Product_url': product_url,
                                 'Date_&_TimeStamp': crawltime, 'Cache Page': page_path,
                                 'Extra1': prod_count, 'Extra2': '-', 'Extra3': '-', 'Extra4': '-', 'Extra5': '-'
                                 }
                        self.push_data2("found", [[Website, Country, Category_ID, pageid, Category_URL, skuid, product_url,crawltime, page_path,prod_count]])
                        print(data12)

                        # else:
                        #     print('issue in product url............')
                except Exception as e:
                    print(e)
                    continue

            tot_pg = general.xpath(source,'//span[@class="san_paging__btn"]',mode='tc')
            pg = str(tot_pg).strip().split(' ')[-1]
            if int(pg) > 1:
                for i in range(1, int(pg)):
                    num1 = 72 * i
                    p1 = i + 1
                    pg_url = f'{Category_URL}&l=gq&o={str(num1)}'
                    for _ in range(20):
                        # data, driver = general.get_url2(strurl,cloak=True,images=True)
                        data2, driver2 = general.get_url(pg_url)
                        if data2['text']:
                            break
                    source2 = html.fromstring(data2['text'])
                    article2 = general.xpath(source2, '//*[@id="san_resultSection"]//article/@data-variation-id',mode='set')
                    article_tag2 = general.xpath(source2, '//*[@id="san_resultSection"]//article/@class', mode='set')
                    for vid1, ar1 in zip(article2, article_tag2):
                        print(vid1)
                        print(ar1)
                        v_url1 = f'https://www.otto.de/cricket/tile/{str(vid1)}'
                        try:
                            for _ in range(20):
                                # data, driver = general.get_url2(strurl,cloak=True,images=True)
                                data3, driver3 = general.get_url(v_url1)
                                if data3['text']:
                                    break
                            source3 = html.fromstring(data3['text'])
                            d3 = str(data3['text']).split('<script type="application/ld+json">')[-1].split('</script>')[0]
                            jd2 = json.loads(d3)
                            try:
                                product_url2 = 'https://www.otto.de' + str(jd2['url'])
                            except:
                                product_url2 = '-'
                            if product_url2 != '-':
                                pageid2 = Category_ID + f'_{p1}'
                                datazone = datetime.datetime.now()
                                f_date = datazone.strftime("%d_%m_%Y")
                                strdate = datazone.day
                                strm = datazone.month
                                stry = datazone.year
                                # pageid = Category_ID + '_' + str('1')
                                cpid = pageid2 + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
                                # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"
                                ASS_folder = f"\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\Otto_DE\ASS"
                                sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                                if os.path.exists(sos_date_wise_folder):
                                    pass
                                else:
                                    os.mkdir(sos_date_wise_folder)
                                sos_filename2 = sos_date_wise_folder + "\\" + cpid + ".html"
                                sos_filename2 = sos_filename2.replace("+", "_").replace("-", "_")
                                page_path2 = sos_filename2
                                page_path2 = page_path2.replace('\\\\10.100.20.40\\E$\\ADIDAS_SavePages\\','https:////ecxus440.eclerx.com//cachepages//').replace('\\', '//').replace('//', '/')
                                if os.path.exists(sos_filename2):
                                    with open(sos_filename2, 'w', encoding='utf-8') as f:
                                        f.write(data2['text'])
                                else:
                                    with open(sos_filename2, 'w', encoding='utf-8') as f:
                                        f.write(data2['text'])
                                sku2 = str(product_url2).split('/')[-2].split('-')[-1]
                                skuid2 = Website + '_' + Country + '_' + sku2
                                crawltime2 = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                                data22 = {'Website': Website, 'Country': Country,
                                         'Category ID': Category_ID, 'Page ID': pageid2,
                                         'Category URL': Category_URL, 'SKU_ID': skuid2,
                                         'Product_url': product_url2,
                                         'Date_&_TimeStamp': crawltime2, 'Cache Page': page_path,
                                         'Extra1': prod_count, 'Extra2': '-', 'Extra3': '-', 'Extra4': '-', 'Extra5': '-'
                                         }
                                self.push_data2("found", [
                                    [Website, Country, Category_ID, pageid2, Category_URL, skuid2, product_url2,
                                     crawltime2, page_path2,prod_count]])
                                print(data22)

                                # else:
                                #     print('issue in product url............')
                        except Exception as e:
                            print(e)
                            continue

            else:
                print('no next page...')
        except Exception as e:
            print(e)

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