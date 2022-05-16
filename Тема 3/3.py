lst = [10, 17, 13, 44, 23, 88, 100, 99]
MenuChoise = int(input("Четные числа последовательности - 1 \nНе четные числа последовательности - 2 \n"))
if MenuChoise == 1:
    for digit in lst:
        if digit % 2 == 0:
            print(digit)
elif MenuChoise == 2:
    for digit2 in lst:
        if digit2 % 2 != 0:
            print(digit2)