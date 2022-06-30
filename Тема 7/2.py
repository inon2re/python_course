def LastRead(lines, file):
    with open(f"{file}", encoding='utf-8') as stih:
        lst = list(stih)
        count = len(lst)
        count = count-lines
        lst = lst[count:]
        for i in lst:
            print(i)


LastRead(2, "Texts/7-1.txt")