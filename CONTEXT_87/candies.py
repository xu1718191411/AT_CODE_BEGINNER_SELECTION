import numpy as np

N = 5
ARR1 = [3, 2, 2, 4, 1]
ARR2 = [1, 2, 2, 2, 1]

N = 4
ARR1 = [1, 1, 1, 1]
ARR2 = [1, 1, 1, 1]

N = 7
ARR1 = [3, 3, 4, 5, 4, 5, 3]
ARR2 = [5, 3, 4, 4, 2, 3, 2]

N = int(input())
ARR1 = [int(s) for s in input().split(" ")]
ARR2 = [int(s) for s in input().split(" ")]


def calculate(n, arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    k = 0

    res = [np.sum(arr1) + arr2[n-1]]

    for i in range(n+1):
        s1 = np.sum(arr1[:i+1])
        s2 = np.sum(arr2[i:])
        res.append(s1 + s2)

    print(max(res))

calculate(N, ARR1, ARR2)