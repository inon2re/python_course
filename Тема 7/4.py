file = "Texts/7-1.txt"
def SearchWord(file, word):
    with open(file, encoding='utf-8') as stih:
        lstwords = []
        lstwords2 = []
        count = 0
        for _ in stih:
            lstwords.append(_.split())
        for i in lstwords:
            for a in i:
                lstwords2.append(a)
        for words in lstwords2:
            if words == word:
                count += 1
        return count
print(SearchWord(file, 'не'))