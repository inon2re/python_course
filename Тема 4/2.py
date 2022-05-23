list1 = [5, 10, 15, 20, 25, 50, 20, 200, 20]
count = list1.count(20)
for _ in range(count):
    ind = list1.index(20)
    list1[ind] = 200
print(list1)
