A, B, C = int(input("Введите сторону треугольника ")), int(input("Введите сторону треугольника ")), int(input("Введите сторону треугольника "))
if (A + B > C) and (B + C > A) and (A + C > B):
    print('Существует')
else:
    print('Не существует')