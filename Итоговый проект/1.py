
import requests
from bs4 import BeautifulSoup

url = 'https://stopgame.ru/news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html')
images = soup.find_all('img')

UrlList = []

for image in images:
    src = image.get("src")
    if src:
        UrlList.append(src)

for i in range(len(UrlList)-1):
    out = requests.get(UrlList[i])
    with open(f'img/new_images{i}.jpg', 'wb') as f:
        f.write(out.content)
        print(i)
