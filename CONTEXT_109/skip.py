S = input().split(" ")
n = int(S[0])
x = int(S[1])

arr = [int(s) for s in input().split(" ")]

import fractions
def gcd(a, b):
    return fractions.gcd(a, b)

# import math
# def gcd(a, b):
#     return math.gcd(a, b)

def calculate(n,x,arr):
    data = []
    for ar in arr:
        if ar < x:
            data.append(x - ar)
        else:
            data.append(ar - x)

    return data

data = calculate(n,x,arr)

if len(data) == 1:
    print(data[0])
else:
    res = gcd(data[0],data[1])
    for index,da in enumerate(data):
        if index < 2:
            continue
        res = gcd(res,da)
    print(res)