import math
import numpy as np
N, M = 3, 2
ARR = [
    [1, 2],
    [2, 3]
]

N, M = 3, 3
ARR = [
    [1, 2],
    [1, 3],
    [2, 3],
]


N, M = map(int,input().split())
ARR = []

for i in range(M):
    ARR.append(list(map(int,input().split())))



def prepare(n, m, arr):
    result = []

    for i in range(n):
        tmp = []
        for j in range(n):
            if i == j:
                tmp.append(0)
            else:
                tmp.append(math.inf)

        result.append(tmp)


    for i in range(m):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1

        result[startNode][endNode] = 1
        result[endNode][startNode] = 1

    return result


def calculate(n, m, arr):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    arr = np.array(arr)

    for i in range(n):
        res = np.count_nonzero(arr[i] == 2)
        print(res)


data = prepare(N, M, ARR)

calculate(N, M, data)
