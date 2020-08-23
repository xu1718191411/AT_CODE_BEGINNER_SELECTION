import numpy as np

H, W, M = 3, 3, 4
ARR = [
    [3, 3],
    [3, 1],
    [1, 1],
    [1, 2],
]


def calculate(h, w, m, arr):
    srr = np.zeros((h, w))
    print(srr)

    for i in range(m):
        c0 = arr[i][0] - 1
        c1 = arr[i][1] - 1
        srr[c0][c1] = 1

    print(srr)

    res0 = np.sum(srr, axis=0)
    res1 = np.sum(srr, axis=1)

    res0Max = np.max(res0)
    res1Max = np.max(res1)
    res0MaxIndex = np.argwhere(res0 == res0Max)
    res1MaxIndex = np.argwhere(res1 == res1Max)

    print(res0MaxIndex)
    print(res1MaxIndex)

    result = 0

    for mH in res1MaxIndex:
        for mW in res0MaxIndex:
            print(mH[0],mW[0])
            result = max(result,res0Max + res1Max - srr[mH[0]][mW[0]])

    print(int(result))

calculate(H, W, M, ARR)
