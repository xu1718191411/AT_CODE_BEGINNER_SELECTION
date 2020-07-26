import math

A, B, C = 7, 2, 5
K = 3

A, B, C = 7, 4, 2
K = 3

# A, B, C = 7, 7, 7
# K = 3
#
A, B, C = map(int, input().split())
K = int(input())


def calculate(a, b, c, k):
    res1 = 0
    while b <= a:
        b = b * 2
        res1 += 1

    res2 = 0
    while c <= b:
        c = c * 2
        res2 += 1

    result = res1 + res2
    if result <= k:
        print("Yes")
    else:
        print("No")


calculate(A, B, C, K)
