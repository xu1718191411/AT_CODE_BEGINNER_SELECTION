#pypy3

import math

# H, N = 9, 3
# ARR = [
#     [8, 3],
#     [4, 2],
#     [2, 1]
# ]
#
#
# H, N = 100, 6
# ARR = [
#     [1, 1],
#     [2, 3],
#     [3, 9],
#     [4, 27],
#     [5, 81],
#     [6, 243]
# ]
#

H, N = map(int, input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int, input().split())))


def calculate(h, n, arr):
    brr = [math.inf] * (h+1)
    brr[0] = 0

    for i in range(h + 1):
        for j in range(n):

            damage = arr[j][0]
            cost = arr[j][1]

            nextDamage = i + damage

            if nextDamage > h:
                nextDamage = h

            nextCost = min(brr[i] + cost, brr[nextDamage])

            brr[nextDamage] = nextCost

    print(brr[-1])


calculate(H, N, ARR)
