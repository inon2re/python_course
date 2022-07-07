import requests


url = 'https://yandex.ru/'
def GetFromUrlStatus(url):
    result = requests.get(url)
    return f"На сайте с url --> {url} статус равен: {result.status_code}"
print(GetFromUrlStatus(url))