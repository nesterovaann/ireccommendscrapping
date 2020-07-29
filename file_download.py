import requests

user_id = 12345
url = 'https://irecommend.ru/content/kolyaska-s-progulochnym-blokom-stokke-crusi'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
      }
r = requests.get(url, headers = headers)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)

