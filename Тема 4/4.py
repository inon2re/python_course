list = [1, 1, 1, 1, 1, 2, 2, 3, 3]
list2 = []
ind = 0
for _ in range(len(list)):
    if list[ind] not in list2:
        list2.append(list[ind])
        ind += 1
    else:
        ind += 1
print(list2)