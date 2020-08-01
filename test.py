a1 = set()

a1.add("o")
a1.add("v")
a1.add("l")
a1.add("e")

a2 = set()
a2.add("l")
a2.add("o")
a2.add("v")
a2.add("e")


res = a2.difference(a1)
print(len(res))
