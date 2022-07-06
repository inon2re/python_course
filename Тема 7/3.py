file = "Texts/7-1.txt"
def WordsInTxt(file):
    with open(file, encoding='utf-8') as stih:
        lstwords = []
        lstwords2 = []
        count = 0
        word = ''
        for _ in stih:
            lstwords.append(_.split())
        for i in lstwords:
            for a in i:
                lstwords2.append(a)
        for index in range(len(lstwords2)):
            if count < len(lstwords2[index]):
                count = len(lstwords2[index])
                word = lstwords2[index]
        lstwords.clear()
        lstwords.append(word)
        for words in lstwords2:
            if count == len(words) and not words == word:
                lstwords.append(words)
        return lstwords
print(WordsInTxt(file))