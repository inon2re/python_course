# import requests
# # https://stopgame.ru/news
# #
# out = requests.get("https://images.stopgame.ru/news/2022/07/23/c270x153/IQ_xVC4sjq-srCUPKB9gTQ/_yFN7XWm.jpg")
# # print(out.content)
# with open('new_images.png', 'wb') as f:
#     f.write(out.content)

import requests
from bs4 import BeautifulSoup
import os

url = 'https://stopgame.ru/news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html')
images = soup.find_all('img')

UrlList = []

for image in images:
    src = image.get("src")
    if src:
        UrlList.append(src)
# print(UrlList)

for i in range(len(UrlList)-1):
    out = requests.get(UrlList[i])
    with open(f'img/new_images{i}.jpg', 'wb') as f:
        f.write(out.content)
        print(i)
