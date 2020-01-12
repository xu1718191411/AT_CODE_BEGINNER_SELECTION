import fractions
import math


def gcd(a,b):
    return fractions.gcd(a, b)

# def gcd(a,b):
#     return math.gcd(a,b)

def calculate(arr):
    # L length (N)
    L = [arr[0]]*len(arr)

    # R length (N)
    R = [arr[-1]]*len(arr)

    for i in range(len(arr)):
        if i == 0:
            continue

        L[i] = gcd(L[i-1],arr[i])


        R[len(arr) - (i + 1)] = gcd(R[len(arr) - i],arr[len(arr) - (i + 1)])

    max = 0
    for i in range(len(arr)):

        if i == 0:
            max = R[i+1]

        elif i == len(arr) - 1:
            if max < L[i-1]:
                max = L[i-1]
        else:
            if max < gcd(L[i-1],R[i+1]):
                max = gcd(L[i-1],R[i+1])

    print(max)

N = int(input())
arr = [int(s) for s in input().split(" ")]
calculate(arr)