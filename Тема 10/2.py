try:
    a = int(input("ff"))
    b = int(input("fff"))
    print(a+b)
except:
    raise TypeError('Ожидаемый тип данных — число')