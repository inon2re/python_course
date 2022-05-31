def ArMean(*args):
    summ = 0
    for i in args:
        summ += i
        count = len(args)
    return summ / count


print(ArMean(1, 3, 5, 7, 8, 9))