from lxml import html
from lxml import etree
import re

filemane = 'test.html'

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content


def parse_user_datafile_bs(filename):
    results = []
    text = read_file(filename)

    tree = html.fromstring(text)
    film_list_lxml = tree.xpath('//div[@class = "profileFilmsList"]')[0]
    items_lxml = film_list_lxml.xpath('//div[@class = "item even" or @class = "item"]')
    for item_lxml in items_lxml:
        # getting movie id
        movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]
        movie_desc = item_lxml.xpath('.//div[@class = "nameRus"]/a/text()')[0]
        movie_id = re.findall('\d+', movie_link)[0]

        # getting english name
        name_eng = item_lxml.xpath('.//div[@class = "nameEng"]/text()')[0]

        # getting watch time
        watch_datetime = item_lxml.xpath('.//div[@class = "date"]/text()')[0]
        date_watched, time_watched = re.match('(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2})', watch_datetime).groups()

        # getting user rating
        user_rating = item_lxml.xpath('.//div[@class = "vote"]/text()')
        if user_rating:
            user_rating = int(user_rating[0])

        results.append({
            'movie_id': movie_id,
            'name_eng': name_eng,
            'date_watched': date_watched,
            'time_watched': time_watched,
            'user_rating': user_rating,
            'movie_desc': movie_desc
        })
    return results

results = parse_user_datafile_bs(filemane)
for i in results:
    print(i)





