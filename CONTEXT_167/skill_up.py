N, M, X = 3, 3, 10
ARR = [
    [60, 2, 2, 4],
    [70, 8, 7, 9],
    [50, 2, 3, 9],
]

N, M, X = 3, 3, 10
ARR = [
    [100, 3, 1, 4],
    [100, 1, 5, 9],
    [100, 2, 6, 5]
]

N, M, X = 8, 5, 22
ARR = [
    [100, 3, 7, 5, 3, 1],
    [164, 4, 5, 2, 7, 8],
    [334, 7, 2, 7, 2, 9],
    [234, 4, 7, 2, 8, 2],
    [541, 5, 4, 3, 3, 6],
    [235, 4, 8, 6, 9, 7],
    [394, 3, 6, 1, 6, 2],
    [872, 8, 4, 3, 7, 2],
]

N, M, X = map(int, input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int, input().split())))


def calculate(n, m, x, arr):
    result = []
    for i in range(2 ** n):

        tmpValue = 0
        mrr = [0] * m
        krr = [False] * m
        for j in range(n):
            res = i >> j & 1
            if res == 1:
                tmpValue = tmpValue + arr[j][0]
                for mIndex in range(m):
                    mrr[mIndex] = mrr[mIndex] + arr[j][mIndex + 1]
                    if mrr[mIndex] >= x:
                        krr[mIndex] = True
        if sum(krr) == m:
            result.append(tmpValue)

    if len(result) == 0:
        print(-1)
    else:
        print(min(result))


calculate(N, M, X, ARR)
