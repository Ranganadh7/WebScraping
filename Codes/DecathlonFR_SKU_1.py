import time

import pandas as pd
import numpy as np
import requests
import json
import re
from datetime import datetime
import  general
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
from lxml import html
import random
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '>'.join(list_string)
    return string


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def join_string1(list_string):
    # Join the string based on '-' delimiter
    string = ' | '.join(list_string)

    return string


def join_string2(list_string):
    # Join the string based on '-' delimiter
    string = ': '.join(list_string)

    return string




# assortment_df = pd.read_csv('Pending-1.csv')
assortment_df = pd.read_csv('ASS-1.csv')

decathlon_sku = pd.DataFrame()

c = 1
all_product_data = []
for url3 in range(len(assortment_df['PDP URL'])):
    try:
        proxy_iplum = ["lum-customer-c_127755f5-zone-us_zone-ip-205.237.95.118",
                       "lum-customer-c_127755f5-zone-us_zone-ip-205.237.94.12",
                       "lum-customer-c_127755f5-zone-us_zone-ip-205.237.93.15",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.138.24",
                       "lum-customer-c_127755f5-zone-us_zone-ip-66.56.81.81",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.101.195",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.185.214",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.166.124",
                       "lum-customer-c_127755f5-zone-us_zone-ip-216.19.221.179",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.174.51",
                       "lum-customer-c_127755f5-zone-us_zone-ip-74.85.208.20",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.114.58",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.119.236",
                       "lum-customer-c_127755f5-zone-us_zone-ip-198.240.89.44",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.199.211",
                       "lum-customer-c_127755f5-zone-us_zone-ip-199.244.60.208",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.120.29",
                       "lum-customer-c_127755f5-zone-us_zone-ip-74.85.210.146",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.124.31",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.115.29",
                       "lum-customer-c_127755f5-zone-us_zone-ip-198.240.101.9",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.126.198",
                       "lum-customer-c_127755f5-zone-us_zone-ip-67.213.122.166",
                       "lum-customer-c_127755f5-zone-us_zone-ip-216.19.200.134",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.240.143",
                       "lum-customer-c_127755f5-zone-us_zone-ip-216.19.199.1",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.196.121",
                       "lum-customer-c_127755f5-zone-us_zone-ip-91.92.218.14",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.113.199",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.131.157",
                       "lum-customer-c_127755f5-zone-us_zone-ip-46.232.209.111",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.217.58",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.193.211",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.17.222",
                       "lum-customer-c_127755f5-zone-us_zone-ip-203.78.175.112",
                       "lum-customer-c_127755f5-zone-us_zone-ip-188.119.117.166",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.184.31",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.59.134",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.200.246",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.203.25",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.25.80",
                       "lum-customer-c_127755f5-zone-us_zone-ip-188.211.24.139",
                       "lum-customer-c_127755f5-zone-us_zone-ip-91.192.215.74",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.202.151",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.6.40",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.26.196",
                       "lum-customer-c_127755f5-zone-us_zone-ip-91.92.217.112",
                       "lum-customer-c_127755f5-zone-us_zone-ip-193.200.104.140",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.54.25",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.2.89",
                       "lum-customer-c_127755f5-zone-us_zone-ip-206.204.38.62",
                       "lum-customer-c_127755f5-zone-us_zone-ip-213.188.83.143",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.53.18",
                       "lum-customer-c_127755f5-zone-us_zone-ip-91.245.235.235",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.85.212",
                       "lum-customer-c_127755f5-zone-us_zone-ip-78.138.40.246",
                       "lum-customer-c_127755f5-zone-us_zone-ip-185.246.173.58",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.198.227",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.57.142",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.60.18",
                       "lum-customer-c_127755f5-zone-us_zone-ip-89.38.132.172",
                       "lum-customer-c_127755f5-zone-us_zone-ip-213.188.76.146",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.182.89",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.51.212",
                       "lum-customer-c_127755f5-zone-us_zone-ip-208.86.196.158",
                       "lum-customer-c_127755f5-zone-us_zone-ip-168.151.179.15",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.188.46",
                       "lum-customer-c_127755f5-zone-us_zone-ip-213.188.75.89",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.12.190.164",
                       "lum-customer-c_127755f5-zone-us_zone-ip-213.188.68.39",
                       "lum-customer-c_127755f5-zone-us_zone-ip-89.40.81.29",
                       "lum-customer-c_127755f5-zone-us_zone-ip-185.223.56.108",
                       "lum-customer-c_127755f5-zone-us_zone-ip-161.129.160.90",
                       "lum-customer-c_127755f5-zone-us_zone-ip-213.188.88.130",
                       "lum-customer-c_127755f5-zone-us_zone-ip-152.39.153.185",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.205.38",
                       "lum-customer-c_127755f5-zone-us_zone-ip-203.78.174.235",
                       "lum-customer-c_127755f5-zone-us_zone-ip-206.204.49.106",
                       "lum-customer-c_127755f5-zone-us_zone-ip-94.176.61.225",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.23.229",
                       "lum-customer-c_127755f5-zone-us_zone-ip-95.215.38.210",
                       "lum-customer-c_127755f5-zone-us_zone-ip-209.95.161.115",
                       "lum-customer-c_127755f5-zone-us_zone-ip-162.43.236.118",
                       "lum-customer-c_127755f5-zone-us_zone-ip-45.142.97.199",
                       "lum-customer-c_127755f5-zone-us_zone-ip-152.39.160.7",
                       "lum-customer-c_127755f5-zone-us_zone-ip-119.13.221.75",
                       "lum-customer-c_127755f5-zone-us_zone-ip-139.5.105.86",
                       "lum-customer-c_127755f5-zone-us_zone-ip-180.149.0.122",
                       "lum-customer-c_127755f5-zone-us_zone-ip-206.204.5.224",
                       "lum-customer-c_127755f5-zone-us_zone-ip-203.109.62.114",
                       "lum-customer-c_127755f5-zone-us_zone-ip-139.5.107.122",
                       "lum-customer-c_127755f5-zone-us_zone-ip-84.39.228.157",
                       "lum-customer-c_127755f5-zone-us_zone-ip-203.109.63.54",
                       "lum-customer-c_127755f5-zone-us_zone-ip-95.215.37.169",
                       "lum-customer-c_127755f5-zone-us_zone-ip-162.43.235.85",
                       "lum-customer-c_127755f5-zone-us_zone-ip-152.39.214.9",
                       "lum-customer-c_127755f5-zone-us_zone-ip-110.238.215.203",
                       "lum-customer-c_127755f5-zone-us_zone-ip-162.43.229.39",
                       "lum-customer-c_127755f5-zone-us_zone-ip-185.10.4.83",
                       "lum-customer-c_127755f5-zone-us_zone-ip-216.194.92.180"]

        port = '22225'
        rand_ips = "zproxy.lum-superproxy.io"
        rndusername = random.choice(proxy_iplum)
        usern_passw = rndusername + ':dngrv4oofa9a'
        proxy = {'https': "https://{}@{}:{}/".format(usern_passw, rand_ips, port)}
        p1 = ['154.28.67.106', '154.28.67.111', '154.28.67.116', '154.28.67.117', '154.28.67.125',
              '154.28.67.131',
              '154.28.67.133', '154.28.67.142', '154.28.67.156', '154.28.67.163', '154.28.67.173',
              '154.28.67.18',
              '154.28.67.182', '154.28.67.184', '154.28.67.20', '154.28.67.200', '154.28.67.210',
              '154.28.67.218',
              '154.28.67.222', '154.28.67.223', '154.28.67.231', '154.28.67.240', '154.28.67.243',
              '154.28.67.253',
              '154.28.67.39', '154.28.67.4', '154.28.67.49', '154.28.67.5', '154.28.67.61', '154.28.67.80',
              '154.28.67.81', '154.28.67.87', '154.28.67.88', '154.28.67.96', '154.28.67.99', '154.7.230.100',
              '154.7.230.101', '154.7.230.103', '154.7.230.107', '154.7.230.109', '154.7.230.130',
              '154.7.230.132',
              '154.7.230.14', '154.7.230.140', '154.7.230.147', '154.7.230.151', '154.7.230.156',
              '154.7.230.163',
              '154.7.230.170', '154.7.230.18', '154.7.230.183', '154.7.230.188', '154.7.230.189',
              '154.7.230.19',
              '154.7.230.190', '154.7.230.198', '154.7.230.204', '154.7.230.209', '154.7.230.235',
              '154.7.230.238',
              '154.7.230.246', '154.7.230.29', '154.7.230.41', '154.7.230.42', '154.7.230.51', '154.7.230.55',
              '154.7.230.60', '154.7.230.61', '154.7.230.74', '154.7.230.82', '154.7.230.89', '23.131.8.112',
              '23.131.8.115', '23.131.8.117', '23.131.8.12', '23.131.8.121', '23.131.8.124', '23.131.8.150',
              '23.131.8.161', '23.131.8.166', '23.131.8.171', '23.131.8.173', '23.131.8.176', '23.131.8.177',
              '23.131.8.181', '23.131.8.19', '23.131.8.192', '23.131.8.194', '23.131.8.199', '23.131.8.202',
              '23.131.8.203', '23.131.8.204', '23.131.8.207', '23.131.8.209', '23.131.8.213', '23.131.8.216',
              '23.131.8.225', '23.131.8.228', '23.131.8.231', '23.131.8.238', '23.131.8.254', '23.131.8.36',
              '23.131.8.5', '23.131.8.76', '23.131.8.93', '23.131.8.95', '23.131.8.99', '23.131.88.105',
              '23.131.88.12', '23.131.88.137', '23.131.88.139', '23.131.88.140', '23.131.88.145',
              '23.131.88.150',
              '23.131.88.151', '23.131.88.153', '23.131.88.154', '23.131.88.156', '23.131.88.165',
              '23.131.88.18',
              '23.131.88.191', '23.131.88.192', '23.131.88.194', '23.131.88.198', '23.131.88.202',
              '23.131.88.206',
              '23.131.88.220', '23.131.88.223', '23.131.88.228', '23.131.88.233', '23.131.88.24',
              '23.131.88.242',
              '23.131.88.244', '23.131.88.47', '23.131.88.63', '23.131.88.67', '23.131.88.73', '23.131.88.80',
              '23.131.88.81', '23.131.88.82', '23.131.88.88', '23.131.88.97', '23.170.144.149',
              '23.170.144.209',
              '23.170.144.212', '23.170.144.242', '23.170.144.83', '23.170.145.117', '23.170.145.167',
              '23.170.145.182', '23.170.145.19', '23.170.145.203', '23.226.17.101', '23.226.17.109',
              '23.226.17.112', '23.226.17.113', '23.226.17.115', '23.226.17.123', '23.226.17.129',
              '23.226.17.143',
              '23.226.17.148', '23.226.17.165', '23.226.17.186', '23.226.17.199', '23.226.17.201',
              '23.226.17.207',
              '23.226.17.210', '23.226.17.219', '23.226.17.220', '23.226.17.222', '23.226.17.229',
              '23.226.17.250',
              '23.226.17.254', '23.226.17.26', '23.226.17.33', '23.226.17.4', '23.226.17.49', '23.226.17.5',
              '23.226.17.55', '23.226.17.66', '23.226.17.7', '23.226.17.72', '23.226.17.78', '23.226.17.8',
              '23.226.17.86', '23.226.17.90', '23.226.17.93', '23.230.177.105', '23.230.177.110',
              '23.230.177.113',
              '23.230.177.121', '23.230.177.130', '23.230.177.14', '23.230.177.143', '23.230.177.15',
              '23.230.177.150', '23.230.177.154', '23.230.177.165', '23.230.177.173', '23.230.177.191',
              '23.230.177.196', '23.230.177.203', '23.230.177.206', '23.230.177.208', '23.230.177.217',
              '23.230.177.220', '23.230.177.221', '23.230.177.224', '23.230.177.228', '23.230.177.231',
              '23.230.177.235', '23.230.177.237', '23.230.177.241', '23.230.177.27', '23.230.177.38',
              '23.230.177.52', '23.230.177.61', '23.230.177.67', '23.230.177.72', '23.230.177.80',
              '23.230.177.88',
              '23.230.177.94', '23.230.177.99', '23.230.197.103', '23.230.197.106', '23.230.197.109',
              '23.230.197.11', '23.230.197.12', '23.230.197.122', '23.230.197.124', '23.230.197.146',
              '23.230.197.155', '23.230.197.156', '23.230.197.174', '23.230.197.179', '23.230.197.181',
              '23.230.197.196', '23.230.197.2', '23.230.197.201', '23.230.197.207', '23.230.197.208',
              '23.230.197.225', '23.230.197.227', '23.230.197.233', '23.230.197.236', '23.230.197.239',
              '23.230.197.240', '23.230.197.244', '23.230.197.251', '23.230.197.50', '23.230.197.52',
              '23.230.197.54', '23.230.197.60', '23.230.197.71', '23.230.197.80', '23.230.197.81',
              '23.230.197.84',
              '23.230.197.97', '23.230.74.102', '23.230.74.110', '23.230.74.116', '23.230.74.125',
              '23.230.74.133',
              '23.230.74.135', '23.230.74.14', '23.230.74.141', '23.230.74.149', '23.230.74.15',
              '23.230.74.157',
              '23.230.74.16', '23.230.74.170', '23.230.74.172', '23.230.74.174', '23.230.74.183',
              '23.230.74.187',
              '23.230.74.19', '23.230.74.198', '23.230.74.208', '23.230.74.212', '23.230.74.215',
              '23.230.74.23',
              '23.230.74.230', '23.230.74.231', '23.230.74.252', '23.230.74.30', '23.230.74.41', '23.230.74.57',
              '23.230.74.58', '23.230.74.59', '23.230.74.6', '23.230.74.75', '23.230.74.81', '23.230.74.88',
              '23.230.74.91', '23.27.222.108', '23.27.222.109', '23.27.222.134', '23.27.222.138',
              '23.27.222.159',
              '23.27.222.161', '23.27.222.164', '23.27.222.166', '23.27.222.178', '23.27.222.19',
              '23.27.222.195',
              '23.27.222.201', '23.27.222.202', '23.27.222.203', '23.27.222.208', '23.27.222.21',
              '23.27.222.211',
              '23.27.222.218', '23.27.222.223', '23.27.222.228', '23.27.222.234', '23.27.222.236',
              '23.27.222.242',
              '23.27.222.251', '23.27.222.253', '23.27.222.34', '23.27.222.61', '23.27.222.62', '23.27.222.69',
              '23.27.222.70', '23.27.222.72', '23.27.222.73', '23.27.222.74', '23.27.222.81', '23.27.222.93',
              '38.131.131.110', '38.131.131.114', '38.131.131.123', '38.131.131.125', '38.131.131.137',
              '38.131.131.142', '38.131.131.145', '38.131.131.147', '38.131.131.15', '38.131.131.154',
              '38.131.131.16', '38.131.131.17', '38.131.131.173', '38.131.131.18', '38.131.131.193',
              '38.131.131.204', '38.131.131.207', '38.131.131.227', '38.131.131.229', '38.131.131.233',
              '38.131.131.238', '38.131.131.246', '38.131.131.248', '38.131.131.250', '38.131.131.31',
              '38.131.131.36', '38.131.131.50', '38.131.131.58', '38.131.131.64', '38.131.131.70',
              '38.131.131.71',
              '38.131.131.74', '38.131.131.83', '38.131.131.94', '38.131.131.99', '38.75.75.104',
              '38.75.75.111',
              '38.75.75.112', '38.75.75.119', '38.75.75.120', '38.75.75.123', '38.75.75.127', '38.75.75.139',
              '38.75.75.14', '38.75.75.143', '38.75.75.155', '38.75.75.156', '38.75.75.158', '38.75.75.170',
              '38.75.75.179', '38.75.75.188', '38.75.75.2', '38.75.75.201', '38.75.75.231', '38.75.75.232',
              '38.75.75.241', '38.75.75.246', '38.75.75.251', '38.75.75.26', '38.75.75.29', '38.75.75.4',
              '38.75.75.44', '38.75.75.49', '38.75.75.56', '38.75.75.58', '38.75.75.62', '38.75.75.72',
              '38.75.75.76', '38.75.75.79', '38.75.75.88', '38.96.156.108', '38.96.156.112', '38.96.156.128',
              '38.96.156.131', '38.96.156.14', '38.96.156.142', '38.96.156.143', '38.96.156.149',
              '38.96.156.16',
              '38.96.156.163', '38.96.156.165', '38.96.156.169', '38.96.156.186', '38.96.156.188',
              '38.96.156.190',
              '38.96.156.192', '38.96.156.194', '38.96.156.199', '38.96.156.218', '38.96.156.236',
              '38.96.156.240',
              '38.96.156.252', '38.96.156.28', '38.96.156.32', '38.96.156.35', '38.96.156.56', '38.96.156.57',
              '38.96.156.6', '38.96.156.67', '38.96.156.77', '38.96.156.80', '38.96.156.83', '38.96.156.84',
              '38.96.156.89', '38.96.156.92', '45.238.157.100', '45.238.157.104', '45.238.157.106',
              '45.238.157.110', '45.238.157.116', '45.238.157.118', '45.238.157.119', '45.238.157.12',
              '45.238.157.123', '45.238.157.132', '45.238.157.14', '45.238.157.149', '45.238.157.15',
              '45.238.157.183', '45.238.157.186', '45.238.157.189', '45.238.157.2', '45.238.157.212',
              '45.238.157.214', '45.238.157.217', '45.238.157.22', '45.238.157.228', '45.238.157.23',
              '45.238.157.247', '45.238.157.43', '45.238.157.48', '45.238.157.51', '45.238.157.52',
              '45.238.157.53',
              '45.238.157.56', '45.238.157.61', '45.238.157.65', '45.238.157.72', '45.238.157.79',
              '45.238.157.8',
              '45.238.159.103', '45.238.159.107', '45.238.159.110', '45.238.159.114', '45.238.159.116',
              '45.238.159.123', '45.238.159.126', '45.238.159.144', '45.238.159.148', '45.238.159.15',
              '45.238.159.156', '45.238.159.165', '45.238.159.167', '45.238.159.183', '45.238.159.20',
              '45.238.159.208', '45.238.159.217', '45.238.159.220', '45.238.159.23', '45.238.159.230',
              '45.238.159.235', '45.238.159.237', '45.238.159.238', '45.238.159.24', '45.238.159.249',
              '45.238.159.251', '45.238.159.32', '45.238.159.34', '45.238.159.51', '45.238.159.6',
              '45.238.159.66',
              '45.238.159.77', '45.238.159.79', '45.238.159.82', '45.238.159.91']

        p_auth = str("csimonra:h19VA2xZ")

        p_host = random.choice(p1)
        p_port = "29842"
        proxy1 = {
            'http': "https://{}@{}:{}/".format(p_auth, p_host, p_port),
            'https': "http://{}@{}:{}/".format(p_auth, p_host, p_port)
        }








        url = assortment_df['PDP URL'][url3]
        #url = 'https://www.decathlon.fr/p/mp/reebok/tapis-de-course-reebok-sl8-0/_/R-p-b4137ff6-6b2c-4aef-a322-3e27881e6772?mc=b4137ff6-6b2c-4aef-a322-3e27881e6772_c1.c249'
        time.sleep(2)
        response = requests.get(url=url, headers=headers, proxies=proxy1, timeout=30)
        time.sleep(5)
        print(response.status_code)
        print(url)
        tree = html.fromstring(response.text)
        MPC = '-'
        product_name = tree.xpath('//div[@class="product-summary svelte-g7h70q"]/h1/text()')
        if not product_name:
            product_name = tree.xpath('//h1/text()')
        product_name = listToString(product_name)

        # category_path = general.xpath(tree, '//ol[@class="svelte-13eh8lr"]/li', mode='set_tc', sep='>')
        # print(category_path)
        category_path = general.xpath(tree, '//ol[@class="svelte-1plueod"]/li', mode='set_tc', sep='>')
        print(('Category path', category_path))
        sellername = tree.xpath('//a[@class="seller-link seller-btn"]/text()')
        if sellername:
            sellername = sellername[0]
        sellername = general.clean(sellername)

        try :
            brand = general.xpath(tree, '//a[@class="brand-logo brand-logo-link svelte-afqqgf"]/@aria-label')
            brand = brand.lower()
        except:
            brand = ''
        if brand == '':
            brand = general.xpath(tree, '//p[@class="product-brand-label svelte-g7h70q"]/text()')
            brand = brand.lower()
        if brand=='':
            brand=general.xpath(tree,'//*[contains(@class,"product-brand")]/text()')
            brand = brand.lower()
        else:
            brand = '-'
        print(('brand', brand))
        if brand=='':
            brand= tree.xpath('//h1/preceding-sibling::p/text()')
        else:
            brand=brand
        if brand == []:
            brand = re.findall(r',"brand":{"@type":"Brand","name":"(.*?)","image"',str(response.text))
        else:
            brand=brand
        listprice = tree.xpath(
            '//div[@class="product-summary svelte-g7h70q"]/div/div/div[@class="prc__active-price"]/text()')
        if len(listprice) > 0:
            List_Price = listprice[1].strip('€')
            List_Price = " " + List_Price
            Promo_Price = listprice[1].strip('€')
            Promo_Price = " " + Promo_Price
            Discount = '-'
        else:
            listprice = tree.xpath('//div[@class="product-summary svelte-g7h70q"]/div/span/span/text()')
            for price2 in range(len(listprice)):
                if '€' in listprice[price2]:
                    List_Price = listprice[price2].strip('€')
                    List_Price = " " + List_Price
                if '%' in listprice[price2]:
                    Discount = listprice[price2].strip('-').strip('%').strip('−')
            Promo_Price = tree.xpath(
                '//div[@class="product-summary svelte-g7h70q"]/div/div[@class="prc__financing"]/div[@class="prc__active-price prc__active-price--sale"]/text()')
            if Promo_Price:
                Promo_Price = Promo_Price[1].strip('€')
                Promo_Price = " " + Promo_Price
            else:
                Promo_Price='-'
                List_Price='-'
                Discount='-'
        if List_Price =='-':
            List_Price=tree.xpath('//h1/following-sibling::div//span[@class="prc__previous"]/text()')
            if not List_Price:
                List_Price = ''.join(tree.xpath('//h1/following-sibling::div//div[@class="prc__active-price"]/@data-price'))
                Promo_Price = List_Price
                Discount='-'
            else:
                List_Price = ''.join(List_Price).strip()
                Promo_Price = ''.join(tree.xpath('//h1/following-sibling::div/div/div[@class="prc__active-price prc__active-price--sale"]/@data-price'))
                Discount=tree.xpath('//h1/following-sibling::div//span[@class="prc__rate"]/text()')
                Discount = ''.join(Discount).replace('−','').strip()
        List_Price = List_Price.replace("soit", '').replace('€', '').replace("d'économie", '').strip()
        Promo_Price = Promo_Price.strip()
        print((List_Price, Promo_Price))

        # review count
        Reviews = tree.xpath('//span[@class="count svelte-3gle04"]/text()')
        Reviews = listToString(Reviews)
        if Reviews != '':
            Reviews = Reviews.strip('\n')
            Reviews = Reviews.split(' ')
            Reviews = Reviews[2]
        else:
            Reviews = '-'

        # rating count
        Ratings = tree.xpath('//span[@class="notation svelte-3gle04"]/strong/text()')
        Ratings = listToString(Ratings)
        if Ratings == '':
            Ratings = '-'

        # colour
        Colour_Name = tree.xpath(
            '//div[@class="current-model"]/span[@class="current-model-color svelte-ag2xiw"]/text()')
        Colour_Name = listToString(Colour_Name)
        if Colour_Name == '':
            Colour_Name = '-'

        # product id
        Product_ID = tree.xpath('//div[@class="product-summary-model-code svelte-g7h70q"]/span/text()')
        try:
            if not Product_ID:
                Product_ID=re.findall(r',"productID":"(.*?)","brand":',str(response.text))
        except:
            Product_ID = ''
        Product_ID = listToString(Product_ID)

        if Product_ID == '':
            Product_ID = '-'

        # colour grouping
        Colour_Grouping = tree.xpath('//div[@class="model-choice svelte-ag2xiw"]/button/@aria-label')

        if len(Colour_Grouping) > 0:
            Colour_Grouping = join_string1(Colour_Grouping)
        else:
            Colour_Grouping = '-'

        # variant
        Variant = tree.xpath('//div[@class="select  svelte-1cr01ag"]/select/option/text()')
        Variant = Variant[1:]
        for i in range(len(Variant)):
            Variant[i] = Variant[i].strip(' ').strip('\n')

        # Variant ID
        Variant_ID = re.findall(r'"Offer","sku":"(.*?)","price":', response.text)
        print(Variant_ID)

        stock_message = []
        stock_condition = []
        stock_count = []
        # Stocks
        for sku_ID in Variant_ID:
            url1 = 'https://www.decathlon.fr/fr/ajax/nfs/stocks/online?skuIds=' + sku_ID
            response1 = requests.get(url=url1, headers=headers, proxies = proxy1)
            stock1 = response1.json()
            print(stock1)
            stock1 = list(stock1.values())[0]
            Stock_Message = list(stock1.values())[0]
            print(Stock_Message)
            stock_count.append(Stock_Message)

            if Stock_Message > 5:
                stock_condition.append('In Stock')
                stock_message.append('En Stock')
            elif 0 < Stock_Message <= 5:
                stock_condition.append('In Stock')
                stock_message.append(Stock_Message)
            elif Stock_Message == 0:
                stock_condition.append('Out of Stock')
                stock_message.append('En rupture de stock')
        print(("stock count",stock_count))
        # description
        # Description = tree.xpath('//div[@class="product-summary-infos svelte-g7h70q"]/p/text()')
        # for i in range(len(Description)):
        #     Description[i] = Description[i].replace('\n', '')
        # Description = listToString(Description)
        # if Description == '':
        #     Description = '-'
        description1 = general.xpath(tree,
            '//div[@id="MarketplaceProductDescription-c796bc48ce0427bde8f1f9690ae2565e18ef92a0"]//p/text()', mode='set')
        print(len(description1))
        description1 = ''.join(description1)
        description2 = general.xpath(tree, '//div[@class="product-summary-infos svelte-f3iv9g"]//p/text()', mode='set')
        description2 = ''.join(description2)
        description = description1 + description2
        Description = general.clean(description)
        product_url = url
        print(Description)
        # image urls
        image_urls1 = re.findall(r'"product":\[{"url":"(.*?)","media":', response.text)
        image_urls2 = re.findall(r'jpg"}},{"url":"(.*?)","media"', response.text)
        image_urls = image_urls1 + image_urls2
        image_urls = join_string1(image_urls)

        # specification
        specification_header = tree.xpath('//span[@class="svelte-1my2ziw"]/h3/text()')

        # specification_text
        specification_text = tree.xpath('//span[@class="svelte-1my2ziw"]/p/text()')

        b = []
        a = list(zip(specification_header, specification_text))
        for i in range(len(a)):
            b.append(join_string2(a[i]))
        Specifications = join_string1(b)

        if len(Specifications) == 0:
            Specifications = '-'

        # time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

        # RPC
        RPC = re.findall(r'\?mc=(.*?)&', response.url)
        if listToString(RPC) == '':
            RPC = re.findall(r'(?<=mc=).*', response.url)
        RPC = listToString(RPC)

        datazone = datetime.now()
        f_date = datazone.strftime("%d_%m_%Y")
        strdate = datazone.day
        strm = datazone.month
        stry = datazone.year
        pageid = assortment_df['SKU_ID'][url3]
        # strdate = '02'
        # f_date = '02_04_2022'
        cpid = pageid + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
        ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Decathlon_FR\\SKU"
        sos_date_wise_folder = ASS_folder + f"\\{f_date}"
        if os.path.exists(sos_date_wise_folder):
            pass
        else:
            os.mkdir(sos_date_wise_folder)
        sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
        sos_filename = sos_filename.replace("+", "_")

        page_path = sos_filename.replace('/', '')
        print(page_path)
        page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                      'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                             '//').replace(
            '//', '/')
        print(page_path)
        if os.path.exists(sos_filename):
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
        else:
            with open(sos_filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
                f.close()
        if len(Variant)!=0:
            for siz in range(len(Variant)):

                data_dict ={'SKU_ID': assortment_df['SKU_ID'][url3], "Website": 'www.decathlon.fr',
                     'Country': 'FR', 'RPC': RPC, 'MPC': 'Not Available',
                     'Product_ID': Product_ID, 'Product_URL': url,
                     'Product_Name': general.clean(product_name), 'Category_Path': general.clean(category_path),
                     'Specification': general.clean(Specifications), 'Description': general.clean(Description),
                     'Currency': 'EURO', 'List_Price': List_Price,
                     'Promo_Price': Promo_Price, 'Discount': Discount, 'Brand': general.clean(brand),
                     'Rating_Count': Ratings, 'Review_Count': Reviews,
                     'Image_URLS': image_urls, 'Variant': Variant[siz], 'Variant_ID': Variant_ID[siz],
                     'Colour_of_Variant': general.clean(Colour_Name), 'Colour_Grouping': general.clean(Colour_Grouping),
                     'Seller_Name': sellername, 'Stock_Count': stock_count[siz],
                     'Stock_Condition': stock_condition[siz], 'Stock_Message': general.clean(stock_message[siz]),
                     'Sustainability_Badge': 'Not Available', 'Reason_Code': 'Success-PF',
                     'Crawling_TimeStamp': date_time, 'Cache_Page_Link': page_path,
                     'Extra1': '-', 'Extra2': '-', 'Extra3': '-', 'Extra4': '-',
                     'Extra5': '-'}
                all_product_data.append(data_dict)
                print(data_dict)
        else:
            data_dict = {'SKU_ID': assortment_df['SKU_ID'][url3], "Website": 'www.decathlon.fr',
                         'Country': 'FR', 'RPC': RPC, 'MPC': 'Not Available',
                         'Product_ID': Product_ID, 'Product_URL': url,
                         'Product_Name': general.clean(product_name), 'Category_Path': general.clean(category_path),
                         'Specification': general.clean(Specifications), 'Description': general.clean(Description),
                         'Currency': 'EURO', 'List_Price': List_Price,
                         'Promo_Price': Promo_Price, 'Discount': Discount, 'Brand': general.clean(brand),
                         'Rating_Count': Ratings, 'Review_Count': Reviews,
                         'Image_URLS': image_urls, 'Variant': '-', 'Variant_ID': '-',
                         'Colour_of_Variant': general.clean(Colour_Name), 'Colour_Grouping': general.clean(Colour_Grouping),
                         'Seller_Name': sellername, 'Stock_Count': '-',
                         'Stock_Condition': 'In Stock', 'Stock_Message': '-',
                         'Sustainability_Badge': 'Not Available', 'Reason_Code': 'Success-PF',
                         'Crawling_TimeStamp': date_time, 'Cache_Page_Link': page_path,
                         'Extra1': '-', 'Extra2': '-', 'Extra3': '-', 'Extra4': '-',
                         'Extra5': '-'}
            all_product_data.append(data_dict)
            print(data_dict)
        data_df = pd.DataFrame(all_product_data)
        f_date = datazone.strftime("%d-%m")
        data_csv = data_df.to_csv(f'{f_date}-Decathlon_fr-1.csv', index=False, encoding="utf-8-sig")
        print(c)
        c = c + 1
        response.raise_for_status()
    except Exception as e:
        print(e)
        pass

