import math
import numpy as np

N, M = 5, 5
ARR = [
    [1, 2, 12],
    [2, 3, 14],
    [3, 4, 7],
    [4, 5, 9],
    [5, 1, 18]
]

# N, M = 3, 2
# ARR = [
#     [1, 2, 10],
#     [2, 3, 10]
# ]


N, M = map(int, input().split())

ARR = []

for i in range(M):
    ARR.append(list(map(int, input().split())))


def calculate(n, m, arr):
    data = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if i == j:
                tmp.append(0)
            else:
                tmp.append(math.inf)
        data.append(tmp)

    for i in range(m):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1
        distance = arr[i][2]
        data[startNode][endNode] = distance
        data[endNode][startNode] = distance

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if data[i][j] > (data[i][k] + data[k][j]):
                    data[i][j] = data[i][k] + data[k][j]

    data = np.array(data)
    s = np.max(data, axis=1)
    result = np.min(s)
    print(result)


calculate(N, M, ARR)
