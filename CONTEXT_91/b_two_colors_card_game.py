from collections import Counter

# N = 3
# ARR = ["apple", "orange", "apple"]
# BRR = ["grape"]

N = int(input())
ARR = []

for i in range(N):
    ARR.append(input())

M = int(input())
BRR = []

for j in range(M):
    BRR.append(input())


def calculate(a, b):
    result = {}

    for i in a:
        if result.get(i) == None:
            result.__setitem__(i, 1)
        else:
            result.__setitem__(i, result.get(i) + 1)

    for i in b:
        if result.get(i) == None:
            result.__setitem__(i, -1)
        else:
            result.__setitem__(i, result.get(i) - 1)

    print(max(0,max(result.values())))


calculate(ARR, BRR)
