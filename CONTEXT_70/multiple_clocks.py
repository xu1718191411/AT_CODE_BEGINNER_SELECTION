import fractions
# import math


N = int(input())

ARR = []

for i in range(N):
    ARR.append(int(input()))

def calculate(arr):
    arr = sorted(arr)
    s = arr[0]
    for i, ar in enumerate(arr):
        if i == 0:
            continue
        else:
            s = zuixiaogongbeishuAtcoder(s,ar)

    print(s)


def zuixiaogongbeishuAtcoder(a, b):
    f = fractions.gcd(a, b)
    res = a * b // f
    return res

#
# def zuixiaogongbeishu(a, b):
#     f = math.gcd(a, b)
#     res = (a * b) // f
#     return res


calculate(ARR)
