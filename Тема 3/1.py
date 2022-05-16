result = 0
while True:
    a = int(input("Введите число "))
    if a % 2 == 0:
        result += 1
        print(f"Четных чисел: {result}")
    else:
        print(f"Четных чисел: {result}")