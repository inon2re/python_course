lst1 = ['Санкт-Петербург', 'Москва', 'Казань']
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново', 'Москва', 'Казань']
Dupl = []
ind = 0
for _ in range(len(lst1)):
    if lst1[ind] in lst2:
        Dupl.append(lst1[ind])
        lst2.remove(lst1[ind])
        lst1.remove(lst1[ind])
print(Dupl)
lst1 += lst2
print(lst1)