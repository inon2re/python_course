url = 'https://www.ozon.ru/search/?from_global=@&sorting=@&text=@'

def UrlSearchReplace(url):
    lst1 = ['true', 'price', '3d']
    lst2 = []
    count = 0
    resultUrl = ''
    lst = url.split('?')
    lst += lst[1].split('&')
    lst.remove(lst[1])
    resultUrl = lst[0] + '?'
    for i in range(len(lst)):
        if i == 0:
            pass
        else:
            lst2.append(lst[i].replace('@', lst1[count]))
            count += 1
    print(resultUrl)
    for a in range(len(lst)-1):
        resultUrl += lst2[a] + '&'
    resultUrl = resultUrl.rstrip(resultUrl[-1])
    return resultUrl


print(UrlSearchReplace(url))