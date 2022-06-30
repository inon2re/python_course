class Nicola():
    _name = "Николай"
    def __init__(self):
        NamePerson = input()
        if NamePerson == "Николай":
            self.__name = NamePerson
        else:
            __name = "Николай"
            print(f"Я не {NamePerson}, а Николай")
        self.age = input()

Person = Nicola()
print(Person._name, Person.age)