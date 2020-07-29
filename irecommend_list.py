import random

import requests
from lxml import html
from lxml import etree
import re




def download_file(url):
    #url = 'https://irecommend.ru/content/kolyaska-s-progulochnym-blokom-stokke-crusi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)'
        }
    random_time = 5 #random.randint(5, 9)
    data = {"login_username": "uasr", "login_password": "K9yxzi@9Ee.SFKp"}
    r = requests.get(url, timeout=random_time, data=data)
    with open('list_of_pages.html', 'w') as output_file:
         output_file.write(r.text)

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content

def get_links(filename):
    links = []
    text = read_file(filename)
    tree = html.fromstring(text)
    page = tree.xpath('.//div[@class="page"]')
    for node in page:
        link1 = node.xpath('.//div[@class="view view-referenced-nodes view-id-referenced_nodes rate noviews"]/div[@class="item-list"]/ul[@class="list-comments"]/li')
        for iter_link in link1:
            link = iter_link.xpath('.//div[@class="reviewTitle"]/a/@href')
            links.append(link)
    return links

def create_links(list_of_links):
    new_link = []
    for link in list_of_links:
        for llink in link: # очень тупое решение, будет работать если гарантируется что в списке link только один элемент
            new_link.append('https://irecommend.ru'+llink)
    return new_link


