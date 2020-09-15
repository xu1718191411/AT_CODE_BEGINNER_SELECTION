S = input()
T = input()

import math


def calculate(s, t):
    lenS = len(s)
    lenT = len(t)

    count = math.inf

    for i in range(lenS - lenT + 1):
        value = s[i:i + lenT]

        tmp = 0
        isOk = True
        for j in range(len(value)):
            if value[j] != t[j]:
               tmp += 1
               if tmp > count:
                   isOk = False
                   break

        if isOk:
            count = min(count, tmp)

    print(count)
calculate(S, T)
