list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
a = (list(filter(lambda x: x != "", list1)))
print(a)