name = input('Введите свое имя')

class NameHaveDigit(Exception):
    def __init__(self, message="Введенное имя содержит цифру"):
        self.message = message
        super().__init__(self.message)

for i in name:
    if i.isdigit():
        raise NameHaveDigit()
print(name)