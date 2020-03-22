# s = "aba"
# K = 4

# s = "atcoderandatcodeer"
# K = 5

# s = "z"
# K = 1

import sys
sys.setrecursionlimit(20000000)

s = input()
K = int(input())


def calculate(str, k):
    s = sorted(list(set(str)))
    criteron = s[:k]
    objs = {}
    for index, s in enumerate(str):
        if s in criteron:
            if len(str)+1 > index + 1 + k:
                made = index + 1 + k
            else:
                made = len(str)+1
            for i in range(index+1,made):
                objs.__setitem__(str[index:i],True)

    arr = sorted(objs.keys())

    print(arr[k-1])

calculate(s, K)

