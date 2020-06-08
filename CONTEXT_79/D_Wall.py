H, W = 2, 4
ARR = [
    [0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 0, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 0, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 0, 9, 9, 9, 9, 2],
    [9, 9, 9, 9, 9, 0, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 0, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 0, 9, 9],
    [9, 9, 9, 9, 2, 9, 9, 9, 0, 9],
    [9, 2, 9, 9, 9, 9, 9, 9, 9, 0]
]

CRR = [
    [-1, -1, -1, -1],
    [8, 1, 1, 8],
]


H, W = map(int,input().split())

ARR = []

for i in range(10):
    res = list(map(int, input().split()))
    ARR.append(res)

CRR = []

for i in range(H):
    CRR.append(list(map(int, input().split())))


def calculate(h, w, arr, crr):
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                s1 = arr[j][i] + arr[i][k]
                s2 = arr[j][k]
                arr[j][k] = min(s1, s2)

    result = 0
    for cr in crr:
        for c in cr:
            if c == -1:
                continue
            else:
                result += arr[c][1]

    print(result)


calculate(H, W, ARR, CRR)
