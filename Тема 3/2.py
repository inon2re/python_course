Password = 'qwerty123'
while True:
    InputPassword = input('Введите пароль ')
    if InputPassword == Password:
        print('Верно')
        break
    elif InputPassword == 'q':
        break
    else:
        continue