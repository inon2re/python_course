class ListWorker:
    def __init__(self, *args):
        self.lst = []
        self.lst = list(args)


    def OutputsStr(self):
        for i in range(len(self.lst)):
            if type(self.lst[i]) is str:
                print((self.lst[i]))


    def OutputsInt(self):
        for i in range(len(self.lst)):
            if type(self.lst[i]) is int:
                print((self.lst[i]))


    def OutputsOther(self):
        for i in range(len(self.lst)):
            if type(self.lst[i]) is not str or not int:
                print((self.lst[i]))

Lst = ListWorker(4, "rex", 'barbi', None, False, True, [1,2,3,4])


Lst.OutputsStr()
print("-" * 20)
Lst.OutputsInt()
print("-" * 20)
Lst.OutputsOther()
