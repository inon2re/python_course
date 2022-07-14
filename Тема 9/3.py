def ConnectorLst():
    lang = ['python', 'c++', 'java', 'javascript', 'ruby', 'c#']
    CounterRepos = [6909587, 2569474, 9827505, 14240090, 1904129, 2893002]
    ResultLst = []
    for i in range(len(lang)):
        lst = [lang[i], CounterRepos[i]]
        ResultLst.append(lst)
    return ResultLst

print(ConnectorLst())