InputList = []
while True:
    InputGuy = input("Введите что-нибудь ")
    if InputGuy == 'q':
        break
    else:
        InputList.append(InputGuy)
print(InputList)