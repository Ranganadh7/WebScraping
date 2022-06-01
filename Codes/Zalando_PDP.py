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


current_path = os.path.dirname(os.path.abspath(__file__))
home_url = "https://www.jarir.com/sa-en/"

class Crawler(spider):

    def __init__(self, current_path):
        super().__init__(current_path)
        if r'panacea\team_data' in current_path.lower():
            super().debug(True)
        else:
            print('Debug: True')
            super().debug(True)
        print('Crawling started')
        # general.create_project_dir('awok_sa_cat_list_screenshots')
        # general.header_values(["category_url", "product_url", "page", "rank", "total"])
        general.header_values(
            ['SKU_ID','Website','Country','RPC','MPC','Product_ID','Product URL','Product_Name','Category Path','Specification','Description','Currency','List_Price','Promo_Price','Discount','Brand','Rating_Count','Review_Count','Image_URLs','Variant','Variant_ID','Colour_of_Variant','Colour_Grouping','Seller_Name','Stock_Count','Stock_Condition','Stock_Message','Sustainability_Badge','Reason_Code','Crawling_TimeStamp','Cache_Page_Link','Extra1','Extra2','Extra3','Extra4','Extra5'])

    def initiate(self, input_row, region, proxies_from_tool, thread_name, childcategory=None):
        # ---------Wonder Proxy---
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
        mpp_proxy = ['154.28.67.106', '154.28.67.111', '154.28.67.116', '154.28.67.117', '154.28.67.125',
                     '154.28.67.131', '154.28.67.133', '154.28.67.142', '154.28.67.156', '154.28.67.163',
                     '154.28.67.173', '154.28.67.18', '154.28.67.182', '154.28.67.184', '154.28.67.20', '154.28.67.200',
                     '154.28.67.210', '154.28.67.218', '154.28.67.222', '154.28.67.223', '154.28.67.231',
                     '154.28.67.240', '154.28.67.243', '154.28.67.253', '154.28.67.39', '154.28.67.4', '154.28.67.49',
                     '154.28.67.5', '154.28.67.61', '154.28.67.80', '154.28.67.81', '154.28.67.87', '154.28.67.88',
                     '154.28.67.96', '154.28.67.99', '154.7.230.100', '154.7.230.101', '154.7.230.103', '154.7.230.107',
                     '154.7.230.109', '154.7.230.130', '154.7.230.132', '154.7.230.14', '154.7.230.140',
                     '154.7.230.147', '154.7.230.151', '154.7.230.156', '154.7.230.163', '154.7.230.170',
                     '154.7.230.18', '154.7.230.183', '154.7.230.188', '154.7.230.189', '154.7.230.19', '154.7.230.190',
                     '154.7.230.198', '154.7.230.204', '154.7.230.209', '154.7.230.235', '154.7.230.238',
                     '154.7.230.246', '154.7.230.29', '154.7.230.41', '154.7.230.42', '154.7.230.51', '154.7.230.55',
                     '154.7.230.60', '154.7.230.61', '154.7.230.74', '154.7.230.82', '154.7.230.89', '23.131.8.112',
                     '23.131.8.115', '23.131.8.117', '23.131.8.12', '23.131.8.121', '23.131.8.124', '23.131.8.150',
                     '23.131.8.161', '23.131.8.166', '23.131.8.171', '23.131.8.173', '23.131.8.176', '23.131.8.177',
                     '23.131.8.181', '23.131.8.19', '23.131.8.192', '23.131.8.194', '23.131.8.199', '23.131.8.202',
                     '23.131.8.203', '23.131.8.204', '23.131.8.207', '23.131.8.209', '23.131.8.213', '23.131.8.216',
                     '23.131.8.225', '23.131.8.228', '23.131.8.231', '23.131.8.238', '23.131.8.254', '23.131.8.36',
                     '23.131.8.5', '23.131.8.76', '23.131.8.93', '23.131.8.95', '23.131.8.99', '23.131.88.105',
                     '23.131.88.12', '23.131.88.137', '23.131.88.139', '23.131.88.140', '23.131.88.145',
                     '23.131.88.150', '23.131.88.151', '23.131.88.153', '23.131.88.154', '23.131.88.156',
                     '23.131.88.165', '23.131.88.18', '23.131.88.191', '23.131.88.192', '23.131.88.194',
                     '23.131.88.198', '23.131.88.202', '23.131.88.206', '23.131.88.220', '23.131.88.223',
                     '23.131.88.228', '23.131.88.233', '23.131.88.24', '23.131.88.242', '23.131.88.244', '23.131.88.47',
                     '23.131.88.63', '23.131.88.67', '23.131.88.73', '23.131.88.80', '23.131.88.81', '23.131.88.82',
                     '23.131.88.88', '23.131.88.97', '23.170.144.149', '23.170.144.209', '23.170.144.212',
                     '23.170.144.242', '23.170.144.83', '23.170.145.117', '23.170.145.167', '23.170.145.182',
                     '23.170.145.19', '23.170.145.203', '23.226.17.101', '23.226.17.109', '23.226.17.112',
                     '23.226.17.113', '23.226.17.115', '23.226.17.123', '23.226.17.129', '23.226.17.143',
                     '23.226.17.148', '23.226.17.165', '23.226.17.186', '23.226.17.199', '23.226.17.201',
                     '23.226.17.207', '23.226.17.210', '23.226.17.219', '23.226.17.220', '23.226.17.222',
                     '23.226.17.229', '23.226.17.250', '23.226.17.254', '23.226.17.26', '23.226.17.33', '23.226.17.4',
                     '23.226.17.49', '23.226.17.5', '23.226.17.55', '23.226.17.66', '23.226.17.7', '23.226.17.72',
                     '23.226.17.78', '23.226.17.8', '23.226.17.86', '23.226.17.90', '23.226.17.93', '23.230.177.105',
                     '23.230.177.110', '23.230.177.113', '23.230.177.121', '23.230.177.130', '23.230.177.14',
                     '23.230.177.143', '23.230.177.15', '23.230.177.150', '23.230.177.154', '23.230.177.165',
                     '23.230.177.173', '23.230.177.191', '23.230.177.196', '23.230.177.203', '23.230.177.206',
                     '23.230.177.208', '23.230.177.217', '23.230.177.220', '23.230.177.221', '23.230.177.224',
                     '23.230.177.228', '23.230.177.231', '23.230.177.235', '23.230.177.237', '23.230.177.241',
                     '23.230.177.27', '23.230.177.38', '23.230.177.52', '23.230.177.61', '23.230.177.67',
                     '23.230.177.72', '23.230.177.80', '23.230.177.88', '23.230.177.94', '23.230.177.99',
                     '23.230.197.103', '23.230.197.106', '23.230.197.109', '23.230.197.11', '23.230.197.12',
                     '23.230.197.122', '23.230.197.124', '23.230.197.146', '23.230.197.155', '23.230.197.156',
                     '23.230.197.174', '23.230.197.179', '23.230.197.181', '23.230.197.196', '23.230.197.2',
                     '23.230.197.201', '23.230.197.207', '23.230.197.208', '23.230.197.225', '23.230.197.227',
                     '23.230.197.233', '23.230.197.236', '23.230.197.239', '23.230.197.240', '23.230.197.244',
                     '23.230.197.251', '23.230.197.50', '23.230.197.52', '23.230.197.54', '23.230.197.60',
                     '23.230.197.71', '23.230.197.80', '23.230.197.81', '23.230.197.84', '23.230.197.97',
                     '23.230.74.102', '23.230.74.110', '23.230.74.116', '23.230.74.125', '23.230.74.133',
                     '23.230.74.135', '23.230.74.14', '23.230.74.141', '23.230.74.149', '23.230.74.15', '23.230.74.157',
                     '23.230.74.16', '23.230.74.170', '23.230.74.172', '23.230.74.174', '23.230.74.183',
                     '23.230.74.187', '23.230.74.19', '23.230.74.198', '23.230.74.208', '23.230.74.212',
                     '23.230.74.215', '23.230.74.23', '23.230.74.230', '23.230.74.231', '23.230.74.252', '23.230.74.30',
                     '23.230.74.41', '23.230.74.57', '23.230.74.58', '23.230.74.59', '23.230.74.6', '23.230.74.75',
                     '23.230.74.81', '23.230.74.88', '23.230.74.91', '23.27.222.108', '23.27.222.109', '23.27.222.134',
                     '23.27.222.138', '23.27.222.159', '23.27.222.161', '23.27.222.164', '23.27.222.166',
                     '23.27.222.178', '23.27.222.19', '23.27.222.195', '23.27.222.201', '23.27.222.202',
                     '23.27.222.203', '23.27.222.208', '23.27.222.21', '23.27.222.211', '23.27.222.218',
                     '23.27.222.223', '23.27.222.228', '23.27.222.234', '23.27.222.236', '23.27.222.242',
                     '23.27.222.251', '23.27.222.253', '23.27.222.34', '23.27.222.61', '23.27.222.62', '23.27.222.69',
                     '23.27.222.70', '23.27.222.72', '23.27.222.73', '23.27.222.74', '23.27.222.81', '23.27.222.93',
                     '38.131.131.110', '38.131.131.114', '38.131.131.123', '38.131.131.125', '38.131.131.137',
                     '38.131.131.142', '38.131.131.145', '38.131.131.147', '38.131.131.15', '38.131.131.154',
                     '38.131.131.16', '38.131.131.17', '38.131.131.173', '38.131.131.18', '38.131.131.193',
                     '38.131.131.204', '38.131.131.207', '38.131.131.227', '38.131.131.229', '38.131.131.233',
                     '38.131.131.238', '38.131.131.246', '38.131.131.248', '38.131.131.250', '38.131.131.31',
                     '38.131.131.36', '38.131.131.50', '38.131.131.58', '38.131.131.64', '38.131.131.70',
                     '38.131.131.71', '38.131.131.74', '38.131.131.83', '38.131.131.94', '38.131.131.99',
                     '38.75.75.104', '38.75.75.111', '38.75.75.112', '38.75.75.119', '38.75.75.120', '38.75.75.123',
                     '38.75.75.127', '38.75.75.139', '38.75.75.14', '38.75.75.143', '38.75.75.155', '38.75.75.156',
                     '38.75.75.158', '38.75.75.170', '38.75.75.179', '38.75.75.188', '38.75.75.2', '38.75.75.201',
                     '38.75.75.231', '38.75.75.232', '38.75.75.241', '38.75.75.246', '38.75.75.251', '38.75.75.26',
                     '38.75.75.29', '38.75.75.4', '38.75.75.44', '38.75.75.49', '38.75.75.56', '38.75.75.58',
                     '38.75.75.62', '38.75.75.72', '38.75.75.76', '38.75.75.79', '38.75.75.88', '38.96.156.108',
                     '38.96.156.112', '38.96.156.128', '38.96.156.131', '38.96.156.14', '38.96.156.142',
                     '38.96.156.143', '38.96.156.149', '38.96.156.16', '38.96.156.163', '38.96.156.165',
                     '38.96.156.169', '38.96.156.186', '38.96.156.188', '38.96.156.190', '38.96.156.192',
                     '38.96.156.194', '38.96.156.199', '38.96.156.218', '38.96.156.236', '38.96.156.240',
                     '38.96.156.252', '38.96.156.28', '38.96.156.32', '38.96.156.35', '38.96.156.56', '38.96.156.57',
                     '38.96.156.6', '38.96.156.67', '38.96.156.77', '38.96.156.80', '38.96.156.83', '38.96.156.84',
                     '38.96.156.89', '38.96.156.92', '45.238.157.100', '45.238.157.104', '45.238.157.106',
                     '45.238.157.110', '45.238.157.116', '45.238.157.118', '45.238.157.119', '45.238.157.12',
                     '45.238.157.123', '45.238.157.132', '45.238.157.14', '45.238.157.149', '45.238.157.15',
                     '45.238.157.183', '45.238.157.186', '45.238.157.189', '45.238.157.2', '45.238.157.212',
                     '45.238.157.214', '45.238.157.217', '45.238.157.22', '45.238.157.228', '45.238.157.23',
                     '45.238.157.247', '45.238.157.43', '45.238.157.48', '45.238.157.51', '45.238.157.52',
                     '45.238.157.53', '45.238.157.56', '45.238.157.61', '45.238.157.65', '45.238.157.72',
                     '45.238.157.79', '45.238.157.8', '45.238.159.103', '45.238.159.107', '45.238.159.110',
                     '45.238.159.114', '45.238.159.116', '45.238.159.123', '45.238.159.126', '45.238.159.144',
                     '45.238.159.148', '45.238.159.15', '45.238.159.156', '45.238.159.165', '45.238.159.167',
                     '45.238.159.183', '45.238.159.20', '45.238.159.208', '45.238.159.217', '45.238.159.220',
                     '45.238.159.23', '45.238.159.230', '45.238.159.235', '45.238.159.237', '45.238.159.238',
                     '45.238.159.24', '45.238.159.249', '45.238.159.251', '45.238.159.32', '45.238.159.34',
                     '45.238.159.51', '45.238.159.6', '45.238.159.66', '45.238.159.77', '45.238.159.79',
                     '45.238.159.82', '45.238.159.91']

        try:
            rank = 0
            cat_url = tpurl = input_row[0]
            catpath = input_row[1]

            header = {
                'authority': 'www.zalando.de',
                'method': 'GET',
                'accept-language': 'de-GB,en;q=0.9',
                'cookie': 'fvgs_ml=mosaic; frsx=AAAAAEgKgW4L25cabJRv5AlpYzDNYQzDL52meyszrVMTI4BZJl74_R7MXgIIo9HYOq_Y4GiUZKgrXd03VA2PmymWmRCs53ygYl_SEWUhIwFEf9D8qPWMclgyFkRn4KmDTscfgWRWqC3uBB6fLqft_HY=; Zalando-Client-Id=3c2ca8c0-5642-402d-a4a8-507dd417d07e; mpulseinject=false; bm_sz=CCE6BEF3AE39DACC635E070261EA754E~YAAQxjArFw0Iegh/AQAAWmS6DA5EpJaVwGXHgUAQTSK/T0REgRviDz03Yk8TuOIgbA2lLnN670mGjBza9KZRk+BDxRuh4kz5rZfhvN2LC5gmFD+1AluldRjlb5uCW/hARJcG5qepAjRZnIY0IPIqMZnbpnDuFDdTWLMo9T8kkLS1rVLyPTYSb0ORvhNXgpD+GhcdxBE4FPIri6CBUK4zWvyU7SVSQZsxiVshuwWnmSvuF+RKDXTJ8Fqjv2UuWeXUubVpTSiZwicpaoBEQJyPRob320bJUWi89PUwaAReNrOEVPuTarS8LeHhE3UPyF2+klZXYq823DoJOfW77iLzlyhl7a1aX/IoPzWgWrvkETk25GCqIijbkSD6xGouboBu4yBDLiMTn6l11byPPd2I~3355954~3422516; language-preference=de; ak_bmsc=51F386DA636FCE57419ABBAD40563838~000000000000000000000000000000~YAAQxjArFyUIegh/AQAARnu6DA5v9BcsO7NNRjamMaUTthlEDpZE1fTWrKa+qIRmGXsVZNLt9bO1r7ppy+NcgsKZs8sisCVlE1roV/57U6SjfPVQNscXXBkj6+ekVCpfb0mLPxK5mGhMWK0v+c/sv6Umo6LmI0GYhdfq2ezxF8bWWID7yOuB9UPe1cHFmaTK6lPSG4c63EcEiWZucxlUzFTvkDSJ4REpQYKnAIuMf3T6C+4woH6bB95jQyfbF8aygmutcPd723OuTaCd9qPzXn4200mPK3IMnpyw/3qnDpwUwETmQ5lJlbIVXOFpVX/qddgSSFg+TQnzrPA6CXipOxakim3Imh33njPdspdD8C7pKFpIck5YTTBENbBhOpgFKMboobrB4MxtFRSOSh2wbbwR+tGbQ1CwTMziMcQ0bBC+kaOVyuClkbjOqbCoygTVpGJyhO5oGN1amkrNqsfoaxB74rRVQrGwtES67EBvb58fg5W0op5+kaHJLw==; _gcl_au=1.1.670818143.1645186041; sqt_cap=1645186016565; _ga=GA1.2.158260230.1645186041; _gid=GA1.2.2078429912.1645186041; ncx=f; _abck=C28748718822C7CBE75F3BA43A652BED~-1~YAAQxjArFyEJegh/AQAAvny7DAd60d6PqxhWE2ZEf6+f4YzITRzIqF39Y7/Fza4QTTxnbXfKwkeCxo1XRV6/GRkXK7/l+abBvySYTEcrEbFAqq+O/BeYdQUStV6suPd0XaUbZ7NKQ16MfHAK/pEBIuHQL/IDRt2ywKUxqNMkHry3CbzLMe9tY4kDcGSMYtANsDjjpSSSimx32dEcdX750Ly7UvTAg+m8kwOctCvSWNj/cnLwYgKdXGzljAW5VU6APrCsxp4JmXU1spMpMmf7TJmGjygZlwIDT9S+QSMGIYasgFX9O1TNn/mwiNvbcPgMU61c3+GNq5GBOGLLTN6AhJo0nFYIgavcYSsTcSxSr+XVOZ2Hl7n5t59PvsTwrh7y+WL3KSSfGwr15A/owwYOgDSzEH6PxtxHR9xp/T8QVlk95D/bmntYzkDl7jnIAPTtaTvogLzj5dVtVm43Rj/e0EWVmt0tpAicelaVZjAC1/rfX5Yo9Z+6ahioTkTKdw==~-1~-1~1645189604; _gat_zalga=1; bm_sv=B28F2F14E3B75AC16E64B0F67A64B1BE~9ofEE5hZWYaSkEszxhghXC3cW1NwF/YT5eUA9MF7wkQ5gAPGeJFyoUsDKqsxOxtE3irchH+5ewLisV4e5qBLPtShWFSTIbTsyYndDV5IIEjV0nQ5ZPpfUQQwj+vU68AHjKbX/FH/iV1KxWl9PlGTgaXDtTDsMU0im0OgMiNuBC8=',
                'referer': 'https://zalando.de/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            }

            for _ in range(30):

                p1 = ['104.218.195.130','104.218.195.205','104.251.82.191','104.251.82.240','104.251.82.63','104.251.84.104','104.251.84.217','104.251.84.232','104.251.85.123','104.251.85.196','104.251.86.162','104.251.86.167','104.251.86.209','104.251.90.200','104.251.90.237','104.251.90.69','104.251.91.154','104.251.91.233','104.251.92.178','104.251.92.234','104.251.92.63','108.177.131.182','108.177.131.25','146.19.55.151','146.19.55.167','154.13.200.241','154.13.200.34','154.13.200.48','154.13.201.156','154.13.201.245','154.13.202.117','154.13.202.128','154.13.202.146','154.13.203.144','154.13.203.212','154.13.204.132','154.13.204.98','154.13.205.173','154.13.205.40','154.13.206.167','154.13.206.181','154.13.207.213','154.13.207.233','154.13.244.123','154.13.244.139','154.13.244.234','154.13.245.128','154.13.245.133','154.13.245.152','154.13.246.157','154.13.246.158','154.13.246.159','154.13.247.187','154.13.247.219','154.13.247.42','154.13.248.163','154.13.248.36','154.13.248.95','154.13.249.100','154.13.249.42','154.13.250.164','154.13.250.89','154.13.251.141','154.13.251.52','154.13.251.76','154.13.252.114','154.13.252.163','154.13.252.79','154.13.253.101','154.13.253.185','154.13.253.195','154.13.254.141','154.13.254.99','154.13.255.222','154.13.255.248','154.17.157.182','154.17.157.234','154.17.157.50','154.17.188.153','154.17.188.24','154.17.189.230','154.17.189.30','154.29.2.16','154.29.2.196','154.29.2.231','154.37.72.173','154.37.72.59','154.37.76.117','154.37.76.137','154.37.76.187','158.115.224.142','158.115.224.246','158.115.225.241','158.115.225.253','158.115.226.137','158.115.226.92','158.115.227.120','158.115.227.174','165.140.224.123','165.140.224.184','165.140.225.115','165.140.225.230','165.140.225.46','165.140.226.14','165.140.226.244','165.140.226.46','165.140.227.12','165.140.227.245','168.91.64.213','168.91.64.234','168.91.64.251','168.91.65.46','168.91.65.73','168.91.66.106','168.91.66.123','168.91.67.109','168.91.67.17','168.91.84.133','168.91.84.59','168.91.85.212','168.91.85.30','168.91.86.14','168.91.86.21','168.91.87.79','168.91.87.97','168.91.88.214','168.91.88.245','168.91.90.127','168.91.90.49','172.255.93.114','172.255.93.130','172.255.94.155','172.255.94.158','173.208.27.32','173.208.27.93','173.208.28.162','173.208.28.246','173.234.244.244','173.234.244.79','173.245.75.175','173.245.75.54','173.245.85.105','173.245.85.116','173.245.85.45','173.245.90.138','173.245.90.224','185.255.196.162','185.255.196.168','185.255.197.105','185.255.197.110','198.251.92.13','198.251.92.237','198.251.92.29','198.251.93.165','198.251.93.227','198.251.93.237','207.230.104.136','207.230.104.195','207.230.104.90','207.230.105.118','207.230.105.205','207.230.105.84','207.230.106.19','207.230.106.198','207.230.106.204','207.230.107.92','207.230.107.95','213.109.148.122','213.109.148.23','23.105.0.165','23.105.0.224','23.105.0.63','23.105.142.171','23.105.142.57','23.105.143.213','23.105.143.73','23.105.144.123','23.105.144.96','23.105.145.215','23.105.145.242','23.105.146.181','23.105.146.245','23.105.147.152','23.105.147.192','23.105.147.203','23.105.150.11','23.105.150.199','23.105.151.138','23.105.151.3','23.105.3.42','23.105.3.68','23.105.4.172','23.105.4.231','23.106.16.106','23.106.16.203','23.106.18.234','23.106.18.44','23.106.20.181','23.106.20.233','23.106.22.125','23.106.22.147','23.106.24.173','23.106.24.41','23.106.26.65','23.106.26.84','23.106.27.13','23.106.27.139','23.106.27.144','23.106.28.230','23.106.28.237','23.106.30.117','23.106.30.126','23.110.166.102','23.110.166.26','23.110.166.76','23.110.169.100','23.110.169.162','23.110.173.171','23.110.173.225','23.129.136.120','23.129.136.245','23.129.40.19','23.129.40.44','23.129.40.76','23.129.56.191','23.129.56.237','23.161.3.146','23.161.3.67','23.170.144.104','23.170.144.108','23.170.144.19','23.170.145.103','23.170.145.252','23.170.145.51','23.175.176.21','23.175.176.24','23.175.177.176','23.175.177.183','23.175.177.8','23.176.49.110','23.176.49.183','23.177.240.144','23.177.240.217','23.177.240.90','23.184.144.105','23.184.144.124','23.184.144.231','23.185.112.167','23.185.112.229','23.185.144.110','23.185.144.171','23.185.144.197','23.185.80.164','23.185.80.4','23.185.80.6','23.186.48.210','23.186.48.248','23.226.16.211','23.226.16.243','23.226.17.178','23.226.17.240','23.226.18.106','23.226.18.193','23.226.19.212','23.226.19.87','23.226.20.187','23.226.20.90','23.226.21.13','23.226.21.22','23.226.22.216','23.226.22.53','23.226.23.178','23.226.23.250','23.226.24.190','23.226.24.6','23.226.24.64','23.226.25.107','23.226.25.68','23.226.26.158','23.226.26.202','23.226.26.220','23.226.27.246','23.226.27.94','23.226.28.159','23.226.28.194','23.226.28.231','23.226.29.126','23.226.29.99','23.226.30.191','23.226.30.235','23.226.31.131','23.226.31.169','23.226.31.193','23.247.172.197','23.247.172.214','23.247.172.51','23.247.173.202','23.247.173.6','23.247.174.196','23.247.174.211','23.247.174.81','23.247.175.156','23.247.175.215','23.247.175.218','23.27.9.103','23.27.9.228','23.82.105.11','23.82.105.194','23.82.105.45','23.82.109.165','23.82.109.242','23.82.184.118','23.82.184.227','23.82.184.80','23.82.186.178','23.82.186.223','23.82.40.136','23.82.40.202','23.82.40.42','23.82.41.119','23.82.41.40','23.82.41.6','23.82.44.209','23.82.44.48','23.82.80.145','23.82.80.68','23.82.81.171','23.82.81.79','45.146.117.234','45.146.117.253','45.146.118.204','45.146.118.228','45.146.119.223','45.146.119.244','45.154.141.33','45.154.141.50','45.154.142.21','45.154.142.231','45.154.142.42','45.224.228.187','45.224.228.87','45.224.228.94','45.224.230.211','45.224.230.228','45.224.231.141','45.224.231.68','45.237.84.117','45.237.84.33','45.237.86.170','45.237.86.178','45.238.157.141','45.238.157.198','45.238.157.225','45.238.159.115','45.238.159.59','45.238.159.8','45.59.128.144','45.59.128.198','45.59.128.236','45.59.129.177','45.59.129.217','45.59.130.16','45.59.130.218','45.59.131.107','45.59.131.140','45.59.131.209','45.59.180.245','45.59.180.58','45.59.181.38','45.59.181.71','45.59.181.80','45.59.182.209','45.59.182.217','45.59.183.171','45.59.183.214','45.59.183.67','45.71.19.128','45.71.19.159','52.128.0.45','52.128.0.98','52.128.1.105','52.128.1.124','52.128.10.164','52.128.10.20','52.128.11.123','52.128.11.71','52.128.12.46','52.128.12.70','52.128.13.125','52.128.13.207','52.128.14.107','52.128.14.115','52.128.14.30','52.128.15.114','52.128.15.92','52.128.196.173','52.128.196.240','52.128.196.70','52.128.197.105','52.128.197.17','52.128.198.105','52.128.198.72','52.128.198.76','52.128.199.206','52.128.199.237','52.128.2.17','52.128.2.58','52.128.200.127','52.128.200.182','52.128.200.79','52.128.201.194','52.128.201.3','52.128.201.56','52.128.202.108','52.128.202.189','52.128.202.242','52.128.203.21','52.128.203.230','52.128.204.144','52.128.204.91','52.128.205.148','52.128.205.204','52.128.206.110','52.128.206.219','52.128.206.96','52.128.207.116','52.128.207.237','52.128.208.176','52.128.208.60','52.128.209.109','52.128.209.120','52.128.210.159','52.128.210.80','52.128.211.121','52.128.211.155','52.128.216.224','52.128.216.41','52.128.217.208','52.128.217.87','52.128.218.165','52.128.218.65','52.128.219.165','52.128.219.177','52.128.219.44','52.128.220.40','52.128.220.48','52.128.221.181','52.128.221.230','52.128.222.161','52.128.222.38','52.128.223.201','52.128.223.219','52.128.3.86','52.128.3.90','52.128.4.106','52.128.4.227','52.128.5.35','52.128.5.52','52.128.6.111','52.128.6.149','52.128.6.93','52.128.7.247','52.128.7.81','52.128.8.195','52.128.8.33','52.128.9.12','52.128.9.177','62.3.61.119','62.3.61.2','62.3.61.40','88.218.172.175','88.218.172.203','88.218.172.83','88.218.173.65','88.218.173.94','88.218.173.98','88.218.174.16','88.218.174.44','88.218.175.235','88.218.175.5','88.218.175.57','95.164.224.233','95.164.224.38','95.164.225.124','95.164.225.21','95.164.226.220','95.164.226.221','95.164.226.7','95.164.227.152','95.164.227.199','95.164.227.206','95.164.236.212','95.164.236.249','95.164.236.58','95.164.237.111','95.164.237.251','95.164.238.183','95.164.238.206','95.164.239.113','95.164.239.253']
                p_auth = str("csimonra:h19VA2xZ")
                p_host = random.choice(mpp_proxy)
                p_port = "29842"
                proxy = {
                    'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
                    'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
                }
                # ------Wonder Proxy----
                # p_auth = str("ecxpremier:eCxpremier123")
                # p_host = random.choice(wonder)
                # p_port = "11000"
                # proxy = {
                #     'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
                #     'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
                # }
                # -------------------------------------------
                header = {
                    'authority': 'www.zalando.de',
                    'method': 'GET',
                    'accept-language': 'de-US,en;q=0.9',
                    'cookie': 'bm_sz=069A88C760C08379B172D2DBCDEBD42B~YAAQVYpRaKQopgR9AQAAvQpECQ03kVHgTXiCd1GbcrCjcxBlNHPXVX282CkSqkAH//H+cs51HE6w7uYSYAHRJ6wmuTCtQPpIzURHd7qoQJgSOyO2Dhw9mOSBLYqatbOQzWHpsQk1EeOBCTFLEyZ3RgNyb78dhH7CArjNuWC1Je+c8MqofhH2DApJK4y5VuGuoAFW4lqRBOuOCn2LqgYE4uKimrEPQL16spOf26MFeVP67junsaaP9xcklQTh7Nc85eiSHaTwllWBnMcTDQmvenp9+Fm9XaI0RRjGHTcPvQtfp/Dbi9m8Jn8WGtiCfbsWKSfyXuempeqsrtsJJWzkkMp3KrPNWyYNV/dnjwuinvx8QA0pokBt9Z8ih3/f510IY14Ibw/Ise0CupxNqapb~4274485~3753014; frsx=AAAAAOLx0CRkDYZWFa1ckXV0kpQU5BSA4wz2nUql40qRjMoj5UoHE7fQ4DMzBTasAPxf6Nvy5guPrJa8Fq0nTcTtUpz7mWWh40z-inM_pXODdyHFseZ88cPh-7BD9ttGRCTgD4FyR8nl_WvX3FrEoeE=; Zalando-Client-Id=36582f25-e91a-4d88-ab49-46566cef2192; ncx=f; ak_bmsc=FC3464107F8B6F47B865B5E3178594A1~000000000000000000000000000000~YAAQHopRaEHi6Ah9AQAA9xhECQ3YM3UsO/ilGETvpoGVURTUVMFezuyLuNsyPIeKh50n6G7dByCWT0j4/+hnscRWObt+E3cVOsuMpibnzoEuLDGZnBCzmEcmROUSBpWvFOI45KLLcz/OxXEJEpK68fp9pr0B339KMFurCHsqN8JNLyBhe2s1qhCQHhPJ/XmrojyIPbMYTYjMo/LhHnMSD2ltPlBOBxOC1leIRziqwcSD4lJ98qjphY9Z/YLGZqn9dYn+w76JklHyFBVCOOAkMvhaKosi8bC//JnrfpJviQFgDUobJyux0fItfUCxfCcCKDby8K9c/Hzd4FxzSwJPXnqDJJoSGJNRCMdJoBL9YE1CFFKyXMzdiVWKcEsdpOcTD5dQalAEGrQteJ1Q3RV9V+Iq/bmGxoS5UwDvnfqa2Ldl4DMua6Jk/xxuMqnCCtl6iTJDmyHGCzNjyD0XeDTA5MtI0g8jg9CJ64PgmGmsLqyBInfzgCGnWDlF; _gcl_au=1.1.1341373456.1636538052; _ga=GA1.2.380652769.1636538053; _gid=GA1.2.1007503823.1636538053; _gat_zalga=1; bm_sv=0D04788DC6CB39B5D18D9F039783D418~KxLmMXYkJMJEFsadY5E5tWQxEFCov92v8oT33wJK9ghOj+ZxtemU+5soAP8tRdV22HWAL81btxwGtKKrLKxMgFDH4r0Pu1+3dWr5M3hGn/sQSHYPiXXumZxA8ZR6pnBW3BLje2dUK9Sf2U9YLvn3RwGhUdl+i2eIVTDJHKN53ss=; language-preference=de; _abck=802962DA192798FEE29D6176A9193159~-1~YAAQXMYcuEXiE/98AQAAl2RGCQbMs8vomqDAzPEXShw6pYC8MeIUgJ/YTOml5IznyPFyuEaW1ZYFpjPDa0M/6Vuz9xKwmtDiQ0ku+UmqSiC07R5Shd6sMFFGfz2P3bQCl7XDJcM5+GlgMQL924nm7517pzA1eSzeBBFbUwYK2r7OreZj1Ph3iPBrgoB/jn2mOeOzB2RSemE1Gdqgyic5Iprt0sx1XsynIgiIUS6fQj3Cf/HTf1bJ6T0QmA+mGCJcgBeinMJQQ6ZZnKISziHLgyQ4ii380xtNd0H7G6r616n6x/v+7PY16Jvuq29Ile1+ftAe7VbHH+XxF3u0BLdSdm3DEUOT4eh8n3fDPp4YmcsQECh/9yW5v0VNk1UJP1zC1lovZN5GUaI8ZAZ1FR+htgv8Xb9zVnk33FoCun3gSPvVpGjAKJVwU0nwpjlarADprniC8ivMOCXrSh90dpHyAySjFnC6WvR9q6U7Jk92vP+hcMyW/wcpAK+V8ZAtcw==~-1~-1~-1',
                    'referer': 'https://www.zalando.de/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
                }
                data1 = requests.get(cat_url, proxies=proxy, headers=header)
                if data1.text:
                    savedata = data1.text
                    variantraw = general.midtext(savedata, ':{"data":{"context":{"entity_id":"ern:product::',
                                                 ']}}},')
                    if variantraw or variantraw=='':
                        break

            variantraw=""

            source = html.fromstring(data1.text)
            # print(data1['text'])


            #-----------------------PAGE SAVE CODE BY RAKESH--------------------------
            L1 = datetime.datetime.now()
            f_date = L1.strftime("%d_%m_%Y")
            HTML = f"E:\\ADIDAS_SAVEPages"
            store_folder = HTML + f"\\Product"
            date_wise_folder = store_folder + f"\\{f_date}"
            # product_Folder=date_wise_folder+f"\\Product"
            day = L1.day
            month = L1.month
            year = L1.year
            timezonehr = L1.strftime("%H")
            timezonemn = L1.strftime("%M")
            timezonesc = L1.strftime("%S")

            adidasid = 1
            # filename = date_wise_folder + f"\\{day}{month}{year}_{timezonesc}_{catpath}_{adidasid}.html"
            # filename = date_wise_folder + f"\\{year}{timezonehr}{day}{timezonesc}{month}{timezonemn}_{adidasid}_{catpath}.html"
            # filename = filename.replace('+','_').replace('-','_')
            # # print(f_date)
            # if os.path.exists(HTML):
            #     pass
            # else:
            #     os.mkdir(HTML)
            # if os.path.exists(store_folder):
            #     pass
            # else:
            #     os.mkdir(store_folder)
            # if os.path.exists(date_wise_folder):
            #     pass
            # else:
            #     os.mkdir(date_wise_folder)
            # # if os.path.exists(product_Folder):
            # #     pass
            # # else:
            # #     os.mkdir(product_Folder)
            # if os.path.exists(filename):
            #     with open(filename, 'w', encoding='utf-8') as f:
            #         f.write(savedata)
            # else:
            #     pass
            #     with open(filename,'w',encoding='utf-8') as f:
            #         f.write(savedata)
            # # cache_page=f"\\{day}{month}{year}_{timezone}_{catpath}_{adidasid}.html"
            # cache_page = f"\\{year}{timezonehr}{day}{timezonesc}{month}{timezonemn}_{adidasid}_{catpath}.html"
            # cache_page = cache_page.replace('+', '_').replace('-', '_')

            datazone = datetime.datetime.now()
            #f_date = datazone.strftime("%d_%m_%Y")
            f_date = '12_05_2022'
            strdate = datazone.day
            strm = datazone.month
            stry = datazone.year
            strcp = cat_url.replace('.html', '').replace('?_rfl=en', '')
            strcp = strcp[-13:]
            pageid = 'ZALANDO_DE_' + str(strcp)
            #cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
            cpid = pageid + '12_05_2022'
            # ASS_folder = f"E:\ADIDAS_SavePages\Jdsports_uk\ASS"

            ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Zalando_DE\\PDP"
            sos_date_wise_folder = ASS_folder + f"\\{f_date}"
            if os.path.exists(sos_date_wise_folder):
                pass
            else:
                os.mkdir(sos_date_wise_folder)
            sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
            sos_filename = sos_filename.replace("+", "_").replace("-", "_")
            page_path = sos_filename.replace('/', '')
            print(page_path)
            cache_page = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                          'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                 '//').replace(
                '//', '/')
            if os.path.exists(sos_filename):
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(savedata)
            else:
                with open(sos_filename, 'w', encoding='utf-8') as f:
                    f.write(savedata)

            # data1['text'] = savedata


            sschecktest = general.xpath(source,'//div[@class="JT3_zV z-pdp__escape-grid"]/div/div/div/div/span',mode='tc')
            if 'Nachhaltigkeit' in sschecktest:
                sastaniblity = 'Yes'
            else:
                sastaniblity = 'No'

            varg1 = general.xpath(source,'//div[@class="JT3_zV mo6ZnF"]/div/div/img/@alt')

            vargropu = ''
            groupingvar = general.xpath(source,'//div[@class="pl0w2g kpgVnb JUrPjL"]/div/a/div/div/img/@alt',mode='set')
            if not groupingvar:
                groupingvar = general.xpath(source,'//div[@class="pl0w2g DT5BTM JUrPjL"]/div[@class="JT3_zV mo6ZnF"]/a/div/div/img',mode='set')
            if groupingvar:
                for eachgp in groupingvar:
                    val = general.xpath(eachgp,'.//@alt')
                    if vargropu == '':
                        vargropu = val
                    else:
                        vargropu =vargropu + '|' + val

            if varg1:
                vargropu = varg1 + '|' + vargropu


            vargropu = general.clean(vargropu)


            if 'id="collection_view_catalog-filters"' in savedata or 'Leider konnten wir die Seite nicht finden' in savedata or 'data-test-id="category-tree"' in savedata:
            # if variantraw=='':
                competitor_id=''
                product_name=''
                category_path='Delist'
                specification=''
                description=''
                currency=''
                list_price=''
                promo_price=''
                discount=''
                tax_info=''
                brand=''
                rating=''
                review=''
                image_url=''
                variant=''
                seller_name= ''
                seller_code=''
                seller_details=''
                seller_rating=''
                seller_ranking=''
                stock_count=''
                stock_condition=''
                warranty=''
                product_condition=''
                shipping_price=''
                shipping_location=''
                shipping_details=''
                minimum_shipping_day=''
                maximum_shipping_day=''
                shipping_days_text=''
                shipping_type=''
                input_to_connector= cat_url + '^' + catpath
                website_name=''
                now=''
                country=''
                catalog_sku_id=''
                catalog_code=''
                catalog_offer_code=''
                number_of_offers=''
                extra1=''
                extra2=''
                extra3=''
                catpath = cache_page
                # print(competitor_id)
                product_url = cat_url
                self.push_data2('found',
                                [[competitor_id, product_url, product_name, category_path,
                                  specification, description,
                                  currency, list_price, promo_price, discount, tax_info, brand,
                                  rating, review,
                                  image_url, variant, seller_name, seller_code, seller_details,
                                  seller_rating,
                                  seller_ranking,
                                  stock_count, stock_condition, warranty, product_condition,
                                  shipping_price,
                                  shipping_location,
                                  shipping_details, minimum_shipping_day, maximum_shipping_day,
                                  shipping_days_text,
                                  shipping_type, cache_page, input_to_connector, website_name, now,
                                  country,
                                  catalog_sku_id,
                                  catalog_code, catalog_offer_code, number_of_offers, extra1,
                                  extra2, extra3,
                                  catpath]])
            else:
                multivarraw = general.midtext(savedata, ',"family":{"product', ']}}},')
                if multivarraw:

                    multivarraw  = '{"family":{"product' + multivarraw + ']}'
                    multijson = json.loads(multivarraw)
                    if multijson:
                       family = multijson.get("family").get("products")
                       if family:
                            edge = family.get("edges")
                            if edge:
                                i = 0
                                for eachedge in edge:
                                    i = i +1
                                    if i > 1:
                                        break
                                    vardata = eachedge.get ("node")
                                    varurl = vardata.get("uri")
                                    variantvar = vardata.get("color").get("name")
                                    varid = vardata.get("sku")
                                    # print(varurl)

                                    if i ==1:

                                        cat_url = tpurl

                                    # variantraw = general.midtext(data1['text'], ':{"data":{"context":{"entity_id":"ern:product::', ']}}},')
                                        variantraw = general.midtext(savedata,
                                                                     ':{"data":{"context":{"entity_id":"ern:product::', ']},"')
                                        a = general.midtext(savedata,':{"data":{"context":{"entity_id":"ern:product',']}}}')

                                        variantraw = '{"data":{"context":{"entity_id":"ern:product::' + variantraw + ']}'

                                        varjson = json.loads(variantraw)
                                        data = varjson.get("data")
                                        if data:
                                            context = data.get("context")
                                            if context:
                                                name = context.get("name")
                                                id = context.get("entity_id")
                                                brand= ''
                                                brandvalue = context.get("brand")
                                                if brandvalue:
                                                    brand = brandvalue.get("name")
                                                promoprice = listprice = discount =''
                                                pricedata = context.get("display_price")
                                                varcolor = context.get("color").get("name")
                                                discount = general.xpath(source,'//div[@class="Bqz_1C"]/span',mode='tc')
                                                discount = discount.replace('off','').replace('sparen','').replace('bis zu','').strip()
                                                discount1 = discount
                                                if pricedata:
                                                    promoval = pricedata.get("current")
                                                    if promoval:
                                                        promoprice = promoval.get("amount")
                                                    listval = pricedata.get("original")
                                                    if listval:
                                                        listprice = listval.get("amount")
                                                listprice = general.xpath(source,'//div[@class="_0xLoFW vSgP6A"]/span',mode='tc')
                                                promoprice = general.xpath(source,'//div[@class="_0xLoFW vSgP6A _7ckuOK"]/span',mode='tc')
                                                promoprice = promoprice.replace('From','').replace('€','').strip()
                                                listprice = listprice.replace('€','').strip()
                                                promo_pricetemp = promoprice
                                                rating = review = ''
                                                familyval = context.get("family")
                                                if familyval:
                                                    try:
                                                        rating = familyval.get("rating").get("average")
                                                    except:
                                                        rating = ''
                                                    try:
                                                        review = familyval.get("reviews").get("totalCount")
                                                    except:
                                                        review =''
                                        tax_info = general.midtext(savedata,'"wishlist.incTax":"','"')
                                        category_path = ''
                                        category_path = general.xpath(source,
                                                                      '//ul[@class="z-navicat-header_genderList"]/li/a/span',
                                                                      mode='set_tc', sep='>')
                                        shipptext = ''
                                        shipptext = general.xpath(source,'//div[@class="PBR5VH _0xLoFW EJ4MLB"]/span[contains(@class, "u-6V88 ka2E9k uMhVZi")]',mode='set_tc',sep='|')
                                        shipping_details = shipping_days_text = shipptext

                                        image_url = ''
                                        image_url = "|".join(general.xpath(source,
                                                                           '//div[@class="JT3_zV mo6ZnF hPWzFB"]//div[@class="JT3_zV ZkIJC- _9QaS6n pckW89 csmaMi"]/div[@class="KVKCn3 u-C3dd jDGwVr mo6ZnF KLaowZ"]/img/@src',
                                                                           mode='set'))
                                        if not image_url:
                                            image_url = "|".join(
                                                general.xpath(source, '//div[@id="product-image"]//a/img/@src', mode='set'))

                                        img_new = general.xpath(source,"//script[contains(text(),'galleryMediaZoom')]//text()")
                                        data = img_new.split('"galleryMediaZoom":')[-1].split("],")[0] + "]"
                                        try:
                                            load_data = json.loads(data)
                                            img_list = []
                                            for i in load_data:
                                                img_url = i.get('uri')
                                                img_list.append(img_url)
                                            image_new = " | ".join(img_list)
                                        except:
                                            image_new = ''
                                            data = img_new.split('"galleryMediaZoom":')[1].split("],")[0] + "]"
                                            try:
                                                load_data = json.loads(data)
                                                img_list = []
                                                for i in load_data:
                                                    img_url = i.get('uri')
                                                    img_list.append(img_url)
                                                image_new = " | ".join(img_list)
                                            except:
                                                image_new=''


                                        try:
                                            spec=''
                                            spectxt = ''
                                            specraw = general.midtext(savedata,'"attributes":[{"',']},')

                                            if specraw:
                                                specraw1 = '"attributes":[{"' + specraw
                                                savedata = savedata.replace(specraw1,'')
                                                specraw = '{"attributes":[{"' + specraw
                                                if '"__' in specraw:
                                                    pass
                                                else:
                                                    specraw = specraw.replace('{__', '"{__')

                                                specjson = json.loads(specraw)
                                                attribut = specjson.get("attributes")
                                                if attribut:
                                                    for echatt in attribut:
                                                        spechead = echatt.get("key")
                                                        specvalue = echatt.get("value")
                                                        if spechead:
                                                            spec = spechead + ":" + specvalue
                                                            if spectxt == '':
                                                                spectxt = spec
                                                            else:
                                                                spectxt = spectxt + "|" + spec
                                                    specification = spectxt
                                                    specification = '^Material & care^' + specification
                                            else:
                                                specification = ''
                                        except:
                                            specification = ''
                                        try:
                                            spec = ''
                                            spectxt = ''
                                            specraw = general.midtext(savedata, '"attributes":[{"', ']},')

                                            if specraw:
                                                specraw1 = '"attributes":[{"' + specraw
                                                savedata = savedata.replace(specraw1, '')
                                                specraw = '{"attributes":[{"' + specraw
                                                if '"__' in specraw:
                                                    pass
                                                else:
                                                    specraw = specraw.replace('{__', '"{__')

                                                specjson = json.loads(specraw)
                                                attribut = specjson.get("attributes")
                                                if attribut:
                                                    for echatt in attribut:
                                                        spechead = echatt.get("key")
                                                        specvalue = echatt.get("value")
                                                        if spechead:
                                                            spec = spechead + ":" + specvalue
                                                            if spectxt == '':
                                                                spectxt = spec
                                                            else:
                                                                spectxt = spectxt + "|" + spec
                                                    specification1 = spectxt
                                                    specification1 = '^Details^' + specification1

                                            else:
                                                specification1 = ''
                                        except:
                                            specification1 = ''
                                            try:
                                                spec = ''
                                                spectxt = ''
                                                specraw2value = general.midtext(savedata, ':"details","label":"Mehr zu diesem Produkt', '}]},') + '}]},'
                                                specraw = general.midtext(specraw2value, '"attributes":[{"', ']},')

                                                if specraw:
                                                    specraw1 = '"attributes":[{"' + specraw
                                                    savedata = savedata.replace(specraw1, '')
                                                    specraw = '{"attributes":[{"' + specraw
                                                    if '"__' in specraw:
                                                        pass
                                                    else:
                                                        specraw = specraw.replace('{__', '"{__')

                                                    specjson = json.loads(specraw)
                                                    attribut = specjson.get("attributes")
                                                    Desc = attribut[0].get('description')
                                                    if attribut:
                                                        for echatt in attribut:
                                                            spechead = echatt.get("key")
                                                            specvalue = echatt.get("value")
                                                            if spechead:
                                                                spec = spechead + ":" + specvalue
                                                                if spectxt == '':
                                                                    spectxt = spec
                                                                else:
                                                                    spectxt = spectxt + "|" + spec
                                                        specification1 = spectxt
                                                        specification1 = '^Details^' + specification1

                                                else:
                                                    specification1 = ''
                                            except:
                                                specification1 = ''
                                            #:"details","label":"Mehr zu diesem Produkt


                                        # if specification and specification1:
                                        specification = specification + '|' + specification1
                                        specification = '#' + specification + '#'
                                        specification = specification.replace('#|','').replace('|#','').replace('#','').replace('\n','').replace('\t','')
                                        specification = general.clean(specification)

                                        product_url = cat_url
                                        competitor_id = id.replace('ern:product::','').strip()
                                        product_name = name
                                        product_name = source.xpath('//span[@class="EKabf7 R_QwOV"]/text()')
                                        if product_name:
                                            product_name = general.clean(product_name[0])
                                            print("--------",product_name)

                                        brand = brand
                                        sellername = ''
                                        list_price = listprice
                                        promo_price = promoprice
                                        tax_info = tax_info
                                        rating = rating
                                        review = review

                                        # ratingraw = general.midtext(data1['text'],'ting":{"distribution":{"r',',"brand')
                                        # rating = general.midtext(ratingraw, 'average":', ',')
                                        rating5 = general.xpath(source,'//span[@class="AKpsL5 ka2E9k uMhVZi Kq1JPK pVrzNP"]',mode='tc')
                                        # review = general.midtext(ratingraw, '"reviews":', '}')


                                        currency = "EURO"
                                        specification = specification
                                        description0 = general.xpath(source,'//span[@data-testid="certificate__description"]',mode='tc')
                                        description0 = general.clean(description0).replace('\n','').replace('\t','')

                                        product_condition = general.xpath(source,'//div[@data-testid="product-flag-NEW"]/span',mode='tc')

                                        # detailsdesc = general.xpath(source,'//div[@data-testid="pdp-accordion-details"]/div[@class="ZkIJC- i8_8W0"]/div/div/div',mode='set_tc',sep='|')
                                        detailsdesc = general.xpath(source, '//div[@class="b3yJDY"]', mode='set_tc',sep='|')
                                        aadata = savedata
                                        description = general.midtext(savedata,'ProductAttributeDescriptive","description":"','","')
                                        if not description:
                                            description = general.xpath(source,'//div[@class="JUrPjL"]/span',mode='tc')
                                            if not description:
                                                description = general.midtext(specraw,'"ProductAttributeDescriptive","description":"','",')
                                        description = general.clean(description).replace('\n','').replace('\t','')

                                        varcolor = context.get("color").get("name")
                                        stock_condition = ''
                                        minimum_shipping_day = maximum_shipping_day = seller_details = seller_rating  = warranty = stock_count = shipping_location = shipping_type = shipping_price = ''

                                        input_to_connector = input_row[0] + '^' + input_row[1]
                                        # now = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                                        now=L1.strftime("%Y-%m-%dT%H:%M:%SZ")
                                        extra1 = image_new
                                        extra2 = ''
                                        if ',"description":null' in savedata:
                                            extra3 = 'Description not available'
                                        else:
                                            extra3 = 'Description check'
                                        catalog_sku_id = competitor_id
                                        seller_ranking = 1
                                        country = 'DE'
                                        website_name = 'Zalando_De'
                                        catalog_code = 'Zalando_De'
                                        seller_name = general.xpath(source,'//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span[2]',mode='set_tc',sep=' : ')

                                        seller_name = general.clean(seller_name).replace('#','')
                                        if not seller_name:
                                            seller_name = general.xpath(source,'//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span',mode='set_tc').replace('Verkauft und versandt durch einen','')
                                        sellerextr2 = seller_name

                                        seller_code = ''
                                        catalog_offer_code = ''
                                        product_condition = general.xpath(source,'//div[@data-testid="product-flag-NEW"]/span',mode='tc')

                                        variantraw = context.get("simples")
                                        # vardataraw = general.midtext(data1['text'], '"simplesWithStock":[{"measures"',
                                        #                              ',"family":')
                                        #
                                        # vardataraw = '{"simplesWithStock":[{"measures"' + vardataraw + '}'
                                        vardataraw = general.midtext(savedata, '"simples":[{"size":','],"')
                                        vardataraw = '"simples":[{"size":' + vardataraw
                                        vardataraw0 = vardataraw
                                        result  = savedata
                                        result1 = result.replace(vardataraw,'')
                                        vardataraw = general.midtext(result1, '"simples":[{"size":', '],"')
                                        if vardataraw:
                                            vardataraw = '{"simples":[{"size":' + vardataraw + ']}'
                                        else:
                                            vardataraw = '{' + vardataraw0 + ']}'


                                        vardataraw1 = general.midtext(savedata, '"simplesWithStock":[{"offer"','],"')
                                        vardataraw1 = '{"simplesWithStock":[{"offer"' + vardataraw1 + ']}'

                                        try:
                                            if vardataraw:
                                                pass
                                                var2jon = json.loads(vardataraw)
                                                varvalue = var2jon.get("simples")
                                                for each2var in varvalue:
                                                    size1 = each2var.get("size")
                                                    varsku = each2var.get("sku")
                                                    size = each2var.get("supplierSize")
                                                    if size == '':
                                                        size = size1
                                                    else:
                                                        size = size1
                                                    variant = 'Size: ' +  size

                                                    stock = each2var.get("offer").get("stock").get("quantity")
                                                    if 'OUT_OF_STOCK' in stock:
                                                        stock_condition = 'Out Of stock'
                                                        list_price = ''
                                                        discount  = ''
                                                    else:
                                                        stock_condition = 'InStock'
                                                        list_price = listprice
                                                        discount = discount1

                                                    if stock_condition == 'InStock':
                                                        varlp = ''
                                                        try:
                                                            pass
                                                            varlp = each2var.get("offer").get("price").get("original").get("formatted")
                                                            if varlp =='' or varlp == None :
                                                                varlp = each2var.get("offer").get("price").get(
                                                                    "original").get("amount")
                                                        except:
                                                            varlp = listprice
                                                        try:
                                                            varpp = each2var.get("offer").get("price").get("promotional").get("formatted")
                                                        except:
                                                            varpp = each2var.get("offer").get("price").get("promotional")
                                                        if varpp == '' or varpp == 'null' or varpp == 'None' or varpp == None:
                                                            varpp = each2var.get("offer").get("price").get("original").get(
                                                                "formatted")
                                                        # else:
                                                        #     varpp = promo_pricetemp
                                                        if varpp == '' or varpp == 'null' or varpp == 'None' or varpp == None:
                                                            varpp = promo_pricetemp
                                                    else:
                                                        varpp = ''
                                                        varlp = ''

                                                    promo_price = varpp
                                                    list_price = varlp
                                                    if not promo_price:
                                                        promo_price = list_price

                                                    # list_price = list_price.replace(',','.').replace('€','')
                                                    # promo_price = promo_price.replace(',', '.').replace('€','')

                                                    number_of_offers = 1
                                                    category_path = ''
                                                    seller_name = general.xpath(source,
                                                                                '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span[2]',
                                                                                mode='set_tc', sep=' : ')

                                                    seller_name = general.clean(seller_name).replace('#', '')
                                                    if not seller_name:
                                                        seller_name = general.xpath(source,
                                                                                    '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span',
                                                                                    mode='set_tc').replace(
                                                            'Verkauft und versandt durch einen', '')

                                                    sarchtext = '","size":"' + str(size) + '","deliveryOptions":[{"'
                                                    # sarchtext = '{"sku":"' + varsku +'","size":"' +str(size) +'","isSubscribable":'
                                                    sarchtext = '{"sku":"' + varsku + '","size":"' +str(size) +'","isSubscribable":false,"offer":{"stock":{"quantity":"' + stock+'"}},"deliveryOptions"'

                                                    if sarchtext in savedata:
                                                        pass
                                                    else:
                                                        sarchtext1 = '","size":"' + str(size1) + '","deliveryOptions":[{"'
                                                        sarchtext = sarchtext1


                                                    selleraw = general.midtext(savedata,sarchtext,'"merchant"') + '"merchant"'
                                                    if stock_condition == 'Out Of stock':
                                                        seller_name = '-'
                                                    elif selleraw:
                                                        try:
                                                            # json0 = general.midtext(selleraw,sarchtext,'"merchant"')
                                                            jsonrawtxt = general.midtext(selleraw,'"fulfillmentLabel"',']')
                                                            jsonrawtxt = '{"fulfillmentLabel"' + jsonrawtxt + ']}}'
                                                            jsonseller  = json.loads(jsonrawtxt)
                                                            sellerstep1 = jsonseller.get("fulfillmentLabel")
                                                            seller2 = sellerstep1.get("label")
                                                            if seller2:
                                                                seller_name = ''
                                                                for label1 in seller2:
                                                                    selvalue = label1.get("text")
                                                                    selavailable = label1.get("isHighlighted")
                                                                    if selavailable == True:
                                                                        seller_name = selvalue
                                                                        break
                                                        except:
                                                            seller_name = '-'
                                                    else:
                                                        seller_name = '-'

                                                    seller_name = seller_name.strip()

                                                    if rating and rating != '-':
                                                        rating  = round(rating,1)
                                                    else:
                                                        rating = '-'

                                                    if review:
                                                        pass
                                                    else:
                                                        review = '-'

                                                    if promo_price:
                                                        pass
                                                    else:
                                                        promo_price = '-'

                                                    if discount:
                                                        pass
                                                    else:
                                                        discount = '-'

                                                    if stock_condition == 'InStock':
                                                        stock_condition = 'In Stock'
                                                    if stock_condition == 'Out Of stock':
                                                        stock_condition = 'Out of Stock'
                                                    catalog_offer_code = rating5
                                                    extra2 = sellerextr2
                                                    if 'ab' in str(promo_price):
                                                        promo_price = str(promo_price).replace('ab','').strip()
                                                    if 'ab' in str(list_price):
                                                        list_price = str(list_price).replace('ab','').strip()

                                                    # if ',' in str(promo_price):
                                                    #     promoextra = promo_price.replace(',','.').strip()
                                                    # elif '-' in str(promo_price):
                                                    #     promoextra = '-'
                                                    # else:
                                                    #     promoextra = float(promo_price)/100

                                                    # if ',' in str(list_price):
                                                    #     listextra = list_price.replace(',','.').strip()
                                                    # elif '-' in str(list_price):
                                                    #     listextra = '-'
                                                    # else:
                                                    #     listextra = float(list_price) / 100

                                                    # self.push_data2('found',[[competitor_id, product_url, product_name, category_path,specification, description,currency, list_price, promo_price, discount, tax_info,brand,rating, review,image_url, variant, seller_name, seller_code,seller_details,seller_rating, seller_ranking,stock_count, stock_condition, warranty,product_condition,shipping_price,shipping_location,shipping_details, minimum_shipping_day,maximum_shipping_day,shipping_days_text,shipping_type, cache_page, input_to_connector,website_name, now,country, catalog_sku_id,catalog_code, catalog_offer_code, number_of_offers,extra1,extra2, varcolor, catpath,varsku,stock,sastaniblity,vargropu]])
                                                    self.push_data2('found', [[catpath, 'ZALANDO', 'DE', competitor_id, '-', competitor_id,product_url, product_name, '-', specification, description,currency, list_price, promo_price, discount, brand, rating,review, extra1, variant, varsku, varcolor, vargropu,seller_name, stock, stock_condition, '-', sastaniblity,'Success_PF', now, cache_page,'-','-','-','-','-']])
                                                    print("Data Saved")
                                            elif vardataraw:
                                                var2jon = json.loads(vardataraw)
                                                varvalue = var2jon.get("simplesWithStock")
                                                for each2var in varvalue:
                                                    size = each2var.get("size")
                                                    # listsize.append(size)
                                                    stock = each2var.get("offer").get("stock").get("quantity")
                                                    if 'OUT_OF_STOCK' in stock:
                                                        stock_condition = 'Out Of stock'
                                                    else:
                                                        stock_condition = 'InStock'
                                                    # liststock.append(stock_condition)
                                                    varpp = each2var.get("offer").get("price").get("promotional")
                                                    if varpp == '' or varpp == 'null' or varpp == 'None' or varpp == None:
                                                        varpp = each2var.get("offer").get("price").get("original").get("formatted")
                                                    else:
                                                        varpp = promo_pricetemp
                                                    promo_price = varpp
                                                    list_price = ''
                                                    number_of_offers = 1
                                                    category_path = ''
                                                    list_price = list_price.replace(',', '.')
                                                    promo_price = promo_price.replace(',', '.')

                                                    # variant = finaljson
                                                    # self.push_data2('found',
                                                    #                 [[competitor_id, product_url, product_name, description0,
                                                    #                   specification, description,
                                                    #                   currency, list_price, promo_price, discount, tax_info, brand,
                                                    #                   rating, review,
                                                    #                   image_url, variant, seller_name, seller_code, seller_details,
                                                    #                   seller_rating,seller_ranking,
                                                    #                   stock_count, stock_condition, warranty, product_condition,
                                                    #                   shipping_price,
                                                    #                   shipping_location,
                                                    #                   shipping_details, minimum_shipping_day, maximum_shipping_day,
                                                    #                   shipping_days_text,
                                                    #                   shipping_type, cache_page, input_to_connector, website_name, now,
                                                    #                   country,catalog_sku_id,
                                                    #                   catalog_code, catalog_offer_code, number_of_offers, varcolor,
                                                    #                   extra2, extra3,catpath]])
                                                    self.push_data2('found', [[catpath, 'ZALANDO', 'DE', competitor_id, '-', competitor_id,product_url, product_name, '-', specification, description,currency, list_price, promo_price, discount, brand, rating,review, extra1, variant, varsku, varcolor, vargropu,seller_name, stock, stock_condition, '-', sastaniblity,'Succecc_PF', now, cache_page,'-','-','-','-','-']])
                                                    print("Data Saved")
                                        except:
                                            number_of_offers = ''


                                            rs = 1
                                            variant = "No Variant Found"
                                            category_path = ''
                                            list_price = list_price.replace(',', '.')
                                            promo_price = promo_price.replace(',', '.')
                                            # self.push_data2('found',
                                            #                 [[competitor_id, product_url, product_name, category_path,
                                            #                   specification, description,
                                            #                   currency, list_price, promo_price, discount, tax_info, brand,
                                            #                   rating, review,
                                            #                   image_url, variant, seller_name, seller_code, seller_details,
                                            #                   seller_rating,
                                            #                   seller_ranking,
                                            #                   stock_count, stock_condition, warranty, product_condition,
                                            #                   shipping_price,
                                            #                   shipping_location,
                                            #                   shipping_details, minimum_shipping_day, maximum_shipping_day,
                                            #                   shipping_days_text,
                                            #                   shipping_type, cache_page, input_to_connector, website_name, now,
                                            #                   country,
                                            #                   catalog_sku_id,
                                            #                   catalog_code, catalog_offer_code, number_of_offers, varcolor,
                                            #                   extra2, extra3,
                                            #                   catpath,stock]])
                                            self.push_data2('found', [
                                                [catpath, 'ZALANDO', 'DE', competitor_id, '-', competitor_id,
                                                 product_url, product_name, '-', specification, description, currency,
                                                 list_price, promo_price, discount, brand, rating, review, extra1,
                                                 variant, varsku, varcolor, vargropu, seller_name, stock,
                                                 stock_condition, '-', sastaniblity, 'Success_PF', now, cache_page, '-',
                                                 '-', '-', '-', '-']])
                                            print("Data Saved")

                                    # variantraw  = context.get("simples")
                                    # if variantraw:
                                    #     for eachvar in variantraw:
                                    #         size = eachvar.get("size")
                                    #         stock = eachvar.get("offer").get("stock").get("quantity")
                                    #         if 'OUT_OF_STOCK' in stock:
                                    #             stock_condition ='Out Of stock'
                                    #         else:
                                    #             stock_condition = 'Instock'
                                    #
                                    #         varsize = size
                                    #
                                    #         variant = varcolor + '|' + varsize
                                    #         if 'Out Of Stock' in stock_condition:
                                    #             number_of_offers = '0'
                                    #         else:
                                    #             number_of_offers = '1'
                                    #
                                    #         self.push_data2('found',
                                    #                         [[competitor_id, product_url, product_name, category_path,
                                    #                           specification, description,
                                    #                           currency, list_price, promo_price, discount, tax_info, brand,
                                    #                           rating, review,
                                    #                           image_url, variant, seller_name, seller_code, seller_details,
                                    #                           seller_rating,
                                    #                           seller_ranking,
                                    #                           stock_count, stock_condition, warranty, product_condition,
                                    #                           shipping_price,
                                    #                           shipping_location,
                                    #                           shipping_details, minimum_shipping_day, maximum_shipping_day,
                                    #                           shipping_days_text,
                                    #                           shipping_type, cache_page, input_to_connector, website_name, now,
                                    #                           country,
                                    #                           catalog_sku_id,
                                    #                           catalog_code, catalog_offer_code, number_of_offers, extra1,
                                    #                           extra2, extra3,
                                    #                           catpath]])

                else:
                    variantraw = general.midtext(savedata, ':{"data":{"context":{"entity_id":"ern:product::', ']}}},')
                    a = general.midtext(savedata, ':{"data":{"context":{"entity_id":"ern:product', ']}}}')
                    variantraw = '{"data":{"context":{"entity_id":"ern:product::' + variantraw + ']}}}'
                    try:
                        varjson = json.loads(variantraw)
                        data = varjson.get("data")
                        if data:
                            context = data.get("context")
                            if context:
                                name = context.get("name")
                                id = context.get("entity_id")
                                brand = ''
                                brandvalue = context.get("brand")
                                if brandvalue:
                                    brand = brandvalue.get("name")
                                promoprice = listprice = discount = ''
                                pricedata = context.get("display_price")
                                varcolor = context.get("color").get("name")
                                discount = general.midtext(savedata, 'u-6V88 ka2E9k uMhVZi FxZV-M z-oVg8 _88STHx">', '<').replace('sparen','').replace('bis zu','')
                                if pricedata:
                                    promoval = pricedata.get("current")
                                    if promoval:
                                        promoprice = promoval.get("amount")
                                    listval = pricedata.get("original")
                                    if listval:
                                        listprice = listval.get("amount")
                                rating = review = ''
                                familyval = context.get("family")
                                if familyval:
                                    try:
                                        rating = familyval.get("rating").get("average")
                                    except:
                                        rating = ''
                                    try:
                                        review = familyval.get("reviews").get("totalCount")
                                    except:
                                        review = ''
                        tax_info = general.midtext(savedata, '"wishlist.incTax":"', '"')
                        category_path = ''
                        category_path = general.xpath(source,
                                                      '//ul[@class="z-navicat-header_genderList"]/li/a/span',
                                                      mode='set_tc', sep='>')
                        shipptext = ''
                        shipptext = general.xpath(source,
                                                  '//div[@class="PBR5VH _0xLoFW EJ4MLB"]/span[contains(@class, "u-6V88 ka2E9k uMhVZi")]',
                                                  mode='set_tc', sep='|')
                        shipping_details = shipping_days_text = shipptext

                        image_url = ''
                        image_url = "|".join(general.xpath(source,
                                                           '//div[@class="JT3_zV mo6ZnF hPWzFB"]//div[@class="JT3_zV ZkIJC- _9QaS6n pckW89 csmaMi"]/div[@class="KVKCn3 u-C3dd jDGwVr mo6ZnF KLaowZ"]/img/@src',
                                                           mode='set'))
                        if not image_url:
                            image_url = "|".join(
                                general.xpath(source, '//div[@id="product-image"]//a/img/@src', mode='set'))

                        img_new = general.xpath(source, "//script[contains(text(),'galleryMediaZoom')]//text()")
                        data = img_new.split('"galleryMediaZoom":')[-1].split("],")[0] + "]"
                        load_data = json.loads(data)
                        img_list = []
                        for i in load_data:
                            img_url = i.get('uri')
                            img_list.append(img_url)
                        image_new = " | ".join(img_list)

                        spec = ''
                        spectxt = ''
                        specraw = general.midtext(savedata, '"attributes":[{"category":', ',"targetGroups')
                        specraw = '{"attributes":[{"category":' + specraw + '}'
                        specjson = json.loads(specraw)
                        attribut = specjson.get("attributes")
                        if attribut:
                            for echatt in attribut:
                                specdata = echatt.get("data")
                                if specdata:
                                    for eachspec in specdata:
                                        spechead = eachspec.get("name")
                                        specvalue = eachspec.get("values")
                                        spec = spechead + ":" + specvalue
                                        if spectxt == '':
                                            spectxt = spec
                                        else:
                                            spectxt = spec + "|" + spec
                                specification = spectxt
                                specification = specification.replace('\n','').replace('\t','')

                        product_url = cat_url
                        competitor_id = id.replace('ern:product::', '').strip()
                        product_name = name
                        product_name = source.xpath('//span[@class="EKabf7 R_QwOV"]/text()')
                        if product_name:
                            product_name = general.clean(product_name[0])
                            print("--------", product_name)
                        # product_name = general.xpath(source,
                        #                              '//h1[@class="OEhtt9 ka2E9k uMhVZi _6yVObe pVrzNP _9YcI4f _2MyPg2"]/span',
                        #                              mode='tc')
                        # product_name = general.clean(product_name)
                        brand = brand
                        sellername = ''
                        list_price = listprice
                        promo_price = promoprice
                        tax_info = tax_info
                        rating = rating
                        review = review
                        currency = "EURO"
                        specification = specification
                        description = general.xpath(source, '//div[@class="b3yJDY"]', mode='set_tc', sep='|')
                        description = general.clean(description).replace('\n','').replace('\t','')
                        varcolor = context.get("color").get("name")
                        stock_condition = ''
                        minimum_shipping_day = maximum_shipping_day = seller_details = seller_rating = product_condition = warranty = stock_count = shipping_location = shipping_type = shipping_price = ''

                        input_to_connector = input_row[0] + '^' + input_row[1]
                        now = L1.strftime('%Y-%m-%dT%H:%M:%SZ')
                        extra1 = image_new
                        extra2 = ''
                        if ',"description":null' in savedata:
                            extra3 = 'Description not available'
                        else:
                            extra3 = 'Description check'
                        catalog_sku_id = competitor_id
                        seller_ranking = 1
                        country = 'DE'
                        website_name = 'Zalando_De'
                        catalog_code = 'Zalando_De'
                        seller_name = general.xpath(source,
                                                    '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span[2]',
                                                    mode='set_tc', sep=' : ').replace('#','')
                        if not seller_name:
                            seller_name = general.xpath(source,
                                                        '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span',
                                                        mode='set_tc')
                        seller_code = ''
                        catalog_offer_code = ''
                        product_condition = general.xpath(source,'//div[@data-testid="product-flag-NEW"]/span',mode='tc')

                        variantraw = context.get("simples")
                        if variantraw:
                            for eachvar in variantraw:
                                size = eachvar.get("size")
                                stock = eachvar.get("offer").get("stock").get("quantity")
                                if 'OUT_OF_STOCK' in stock:
                                    stock_condition = 'Out Of stock'
                                else:
                                    stock_condition = 'Instock'

                                varsize = size

                                variant = varcolor + '|' + varsize
                                if 'Out Of Stock' in stock_condition:
                                    number_of_offers = '0'
                                else:
                                    number_of_offers = '1'

                                self.push_data2('found',
                                                [[competitor_id, product_url, product_name, category_path,
                                                  specification, description,
                                                  currency, list_price, promo_price, discount, tax_info, brand,
                                                  rating, review,
                                                  image_url, variant, seller_name, seller_code, seller_details,
                                                  seller_rating,
                                                  seller_ranking,
                                                  stock_count, stock_condition, warranty, product_condition,
                                                  shipping_price,
                                                  shipping_location,
                                                  shipping_details, minimum_shipping_day, maximum_shipping_day,
                                                  shipping_days_text,
                                                  shipping_type, cache_page, input_to_connector, website_name, now,
                                                  country,
                                                  catalog_sku_id,
                                                  catalog_code, catalog_offer_code, number_of_offers, extra1,
                                                  extra2, extra3,
                                                  catpath]])
                                print("Data Saved")
                    except:
                        name = general.midtext(variantraw,'"name":"','"')
                        id = general.midtext(variantraw,'entity_id":"ern:product::','"')
                        brand = general.midtext(variantraw,'brand":{"name":"','"')
                        pricetext = general.midtext(savedata,',"display_price":{"',',"flag')
                        promoprice = general.midtext(pricetext,'current":{"amount":','}')
                        listprice = general.midtext(pricetext, 'original":{"amount":', '}')

                        varjson = json.loads(variantraw)
                        data = varjson.get("data")
                        if data:
                            context = data.get("context")
                            if context:
                                name = context.get("name")
                                id = context.get("entity_id")
                                brand = ''
                                brandvalue = context.get("brand")
                                if brandvalue:
                                    brand = brandvalue.get("name")
                                promoprice = listprice = discount = ''
                                pricedata = context.get("display_price")
                                varcolor = context.get("color").get("name")
                                discount = general.midtext(savedata, 'u-6V88 ka2E9k uMhVZi FxZV-M z-oVg8 _88STHx">',
                                                           '<')
                                discount = discount.replace('sparen','').replace('bis zu','')
                                if pricedata:
                                    promoval = pricedata.get("current")
                                    if promoval:
                                        promoprice = promoval.get("amount")
                                    listval = pricedata.get("original")
                                    if listval:
                                        listprice = listval.get("amount")
                                rating = review = ''
                                familyval = context.get("family")
                                if familyval:
                                    try:
                                        rating = familyval.get("rating").get("average")
                                    except:
                                        rating = ''
                                    try:
                                        review = familyval.get("reviews").get("totalCount")
                                    except:
                                        review = ''
                        tax_info = general.midtext(savedata, '"wishlist.incTax":"', '"')
                        category_path = ''
                        category_path = general.xpath(source,
                                                      '//ul[@class="z-navicat-header_genderList"]/li/a/span',
                                                      mode='set_tc', sep='>')
                        shipptext = ''
                        shipptext = general.xpath(source,
                                                  '//div[@class="PBR5VH _0xLoFW EJ4MLB"]/span[contains(@class, "u-6V88 ka2E9k uMhVZi")]',
                                                  mode='set_tc', sep='|')
                        shipping_details = shipping_days_text = shipptext

                        image_url = ''
                        image_url = "|".join(general.xpath(source,
                                                           '//div[@class="JT3_zV mo6ZnF hPWzFB"]//div[@class="JT3_zV ZkIJC- _9QaS6n pckW89 csmaMi"]/div[@class="KVKCn3 u-C3dd jDGwVr mo6ZnF KLaowZ"]/img/@src',
                                                           mode='set'))
                        if not image_url:
                            image_url = "|".join(
                                general.xpath(source, '//div[@id="product-image"]//a/img/@src', mode='set'))

                        img_new = general.xpath(source, "//script[contains(text(),'galleryMediaZoom')]//text()")
                        data = img_new.split('"galleryMediaZoom":')[-1].split("],")[0] + "]"
                        load_data = json.loads(data)
                        img_list = []
                        for i in load_data:
                            img_url = i.get('uri')
                            img_list.append(img_url)
                        image_new = " | ".join(img_list)

                        # img = general.xpath(source,"//script[contains(text(),'galleryThumbnails')]//text()")
                        # data = img.split('"galleryThumbnails":')[-1].split("],")[0] + "]"
                        # load_data = json.loads(data)
                        # img_list = []
                        # for i in load_data:
                        #     img_url = i.get("uri")
                        #     img_list.append(img_url)

                        spec = ''
                        spectxt = ''
                        specraw = general.midtext(savedata, '"attributes":[{"category":', ',"targetGroups')
                        specraw = '{"attributes":[{"category":' + specraw + '}'
                        specjson = json.loads(specraw)
                        attribut = specjson.get("attributes")
                        if attribut:
                            for echatt in attribut:
                                specdata = echatt.get("data")
                                if specdata:
                                    for eachspec in specdata:
                                        spechead = eachspec.get("name")
                                        specvalue = eachspec.get("values")
                                        spec = spechead + ":" + specvalue
                                        if spectxt == '':
                                            spectxt = spec
                                        else:
                                            spectxt = spec + "|" + spec
                                specification = spectxt
                                specification = specification.replace('\n','').replace('\t','')

                        product_url = cat_url
                        competitor_id = id.replace('ern:product::', '').strip()
                        product_name = name
                        brand = brand
                        sellername = ''
                        list_price = listprice
                        promo_price = promoprice
                        tax_info = tax_info
                        rating = rating
                        review = review
                        currency = "EURO"
                        specification = specification
                        description = general.xpath(source, '//div[@class="b3yJDY"]', mode='set_tc', sep='|')
                        description = general.clean(description).replace('\n','').replace('\t','')
                        varcolor = context.get("color").get("name")
                        stock_condition = ''
                        minimum_shipping_day = maximum_shipping_day = seller_details = seller_rating = product_condition = warranty = stock_count = shipping_location = shipping_type = shipping_price =  ''

                        input_to_connector = input_row[0] + '^' + input_row[1]
                        now = L1.strftime('%Y-%m-%dT%H:%M:%SZ')
                        extra1 = image_new
                        extra2 = ''
                        if ',"description":null' in savedata:
                            extra3 = 'Description not available'
                        else:
                            extra3 = 'Description check'
                        catalog_sku_id = competitor_id
                        seller_ranking = 1
                        country = 'DE'
                        website_name = 'Zalando_De'
                        catalog_code = 'Zalando_De'
                        seller_name = general.xpath(source,
                                                    '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span[2]',
                                                    mode='set_tc', sep=' : ').replace('#','')

                        if not seller_name:
                            seller_name = general.xpath(source,
                                                        '//div[@class="oX3eAU _2LebSa Rft9Ae oW5DLR f2qidi _56Chwa OXMl2N"]/span',
                                                        mode='set_tc')
                        seller_code = ''
                        catalog_offer_code = ''

                        variantraw = context.get("simples")
                        if variantraw:
                            for eachvar in variantraw:
                                size = eachvar.get("size")
                                stock = eachvar.get("offer").get("stock").get("quantity")
                                if 'OUT_OF_STOCK' in stock:
                                    stock_condition = 'Out Of stock'
                                else:
                                    stock_condition = 'Instock'

                                varsize = size

                                variant = varcolor + '|' + varsize
                                if 'Out Of Stock' in stock_condition:
                                    number_of_offers = '0'
                                else:
                                    number_of_offers = '1'

                                self.push_data2('found',
                                                [[competitor_id, product_url, product_name, category_path,
                                                  specification, description,
                                                  currency, list_price, promo_price, discount, tax_info, brand,
                                                  rating, review,
                                                  image_url, variant, seller_name, seller_code, seller_details,
                                                  seller_rating,
                                                  seller_ranking,
                                                  stock_count, stock_condition, warranty, product_condition,
                                                  shipping_price,
                                                  shipping_location,
                                                  shipping_details, minimum_shipping_day, maximum_shipping_day,
                                                  shipping_days_text,
                                                  shipping_type, cache_page, input_to_connector, website_name, now,
                                                  country,
                                                  catalog_sku_id,
                                                  catalog_code, catalog_offer_code, number_of_offers, extra1,
                                                  extra2, extra3,
                                                  catpath]])



        except Exception as e:
            # print(e)
            # print(url)

            if 'find this page.<' in savedata:
                competitor_id = product_name = category_path = specification = description = currency = ''
                list_price = promo_price = discount = tax_info = brand = rating = review = image_url = variant = ''
                seller_name = seller_code = seller_details = seller_rating = seller_ranking = stock_count = ''
                stock_condition = warranty = product_condition = shipping_price = shipping_location = shipping_details = ''
                minimum_shipping_day = maximum_shipping_day = shipping_days_text = shipping_type = ''
                input_to_connector = website_name = now = country = catalog_sku_id = catalog_code = catalog_offer_code = ''
                number_of_offers = extra1 = extra2 = extra3 = catpath = ''
                self.push_data2('found', [['Delist', cat_url, product_name, category_path, specification, description, currency,list_price, promo_price, discount, tax_info, brand, rating, review, image_url, variant,seller_name, seller_code, seller_details, seller_rating, seller_ranking, stock_count,stock_condition, warranty, product_condition, shipping_price, shipping_location, shipping_details,minimum_shipping_day, maximum_shipping_day, shipping_days_text, shipping_type, cache_page,input_to_connector, website_name, now, country, catalog_sku_id, catalog_code, catalog_offer_code,number_of_offers, extra1, extra2, extra3, catpath]])

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
            # print(exc_type, fname, exc_tb.tb_lineno)
            general.write_csv('errors.txt', [[str(e), exc_type, fname, exc_tb.tb_lineno]])

crawl = Crawler(current_path)
crawl.start(crawl.initiate)
