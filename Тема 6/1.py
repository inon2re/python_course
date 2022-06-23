class Pyralepiped():
    width = 1
    lenght = 1
    height = 1

    def Volume(self):
        print(f"Обьем параллепипеда равен - {self.height * self.lenght * self.width}")

    def BaseArea(self):
        print(f"Площадь основания равна - {self.width * self.lenght}")

    def BaseFront(self):
        print(f"Площадь стороны равна - {2 * (self.lenght * self.height + self.width * self.height)}")

    def __init__(self):
        self.width = int(input("Введите ширину "))
        self.lenght = int(input("Введите длинну "))
        self.height = int(input("Введите высоту "))

    @classmethod
    def info(cls):
        return "\nКласс включает в себя методы для расчета его объема, площади основания и площади боковой стороны\n"
        # print(dir(cls))


Para = Pyralepiped()
print(Para.info())
Para.Volume()
Para.BaseFront()
Para.BaseArea()
