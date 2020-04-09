import numpy as np
N = int(input())

ARR = []

for i in range(N):
    ARR.append([int(s) for s in input().split(" ")])

PRR = []

for i in range(N):
    PRR.append([int(s) for s in input().split(" ")])

def calculate(n, arr, prr):
    arr = np.array(arr)

    brr = []
    for i in range(1,2 ** 10):

        mask = np.zeros(10)
        for j in range(0, 10):
            m = i >> j & 1
            mask[9-j] = m
        s = np.count_nonzero((arr == mask) & (arr == 1),axis=1)

        sum = 0
        for _i in range(n):
            sum = sum + prr[_i][s[_i]]

        brr.append(sum)

    return brr

result = calculate(N, ARR, PRR)
print(max(result))


