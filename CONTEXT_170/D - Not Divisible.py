N = 5
ARR = [24, 11, 8, 3, 16]

N = int(input())
ARR = list(map(int,input().split()))

def calculate(n, arr):
    maxValue = max(arr) + 1
    maxValue = 1000006
    krr = [0 for i in range(maxValue)]

    for start in arr:
        if krr[start] > 0:
            krr[start] = 2
            continue

        for i in range(start, maxValue, start):
            krr[i] += 1

    result = 0
    for ar in arr:
        if krr[ar] == 1:
            result = result + 1

    print(result)


calculate(N, ARR)
