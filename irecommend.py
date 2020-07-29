import random

import requests
from lxml import html
from lxml import etree
import re


def download_file(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
    random_time = 5 #random.randint(5,9)
    data = {"login_username": "uasr", "login_password": "K9yxzi@9Ee.SFKp"}
    r = requests.get(url, headers=headers, timeout=random_time, data=data)
    with open('test.html', 'w') as output_file:
         output_file.write(r.text)

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content

def parse_user_datafile_bs(filename):
    text = read_file('test.html')
    results_minus = []
    results_plus = []
    tree = html.fromstring(text)
    review_plus = tree.xpath('.//div[@class="ratio"]/div[@class="plus"]/ul/li/text()')
    for item_plus in review_plus:
        results_plus.append(item_plus)
    review_minus = tree.xpath('.//div[@class="ratio"]/div[@class="minus"]/ul/li/text()')
    for item_minus in review_minus:
        results_minus.append(item_minus)
    return results_minus, results_plus




