import numpy as np


def calculate(arr):
    h = arr.shape[0]
    w = arr.shape[1]

    res = []

    for i in range(h):
        ret = []
        for j in range(w):
            ret.append({'l': 0, 'r': 0, 'u': 0, 'd': 0})
        res.append(ret)

    for i in range(h):
        for j in range(w):

            if arr[i][j] == 1:
                res[i][j]['l'] = 0
                res[i][j]['r'] = 0
                res[i][j]['u'] = 0
                res[i][j]['d'] = 0
            else:
                if j == 0:
                    res[i][j]['l'] = 1
                else:
                    res[i][j]['l'] = res[i][j - 1]['l'] + 1

                if i == 0:
                    res[i][j]['u'] = 1
                else:
                    res[i][j]['u'] = res[i - 1][j]['u'] + 1

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if arr[i][j] == 1:
                res[i][j]['l'] = 0
                res[i][j]['r'] = 0
                res[i][j]['u'] = 0
                res[i][j]['d'] = 0
            else:
                if j == w - 1:
                    res[i][j]['r'] = 1
                else:
                    res[i][j]['r'] = res[i][j+1]['r'] + 1


                if i == h - 1:
                    res[i][j]['d'] = 1
                else:
                    res[i][j]['d'] = res[i + 1][j]['d'] + 1
    max = 0
    for i in range(h):
        for j in range(w):
            val = (res[i][j]['d'] + res[i][j]['u'] + res[i][j]['r'] + res[i][j]['l']) - 3
            if val > max:
                max = val
    return max



S = input().split(" ")
H = int(S[0])
W = int(S[1])

arr = []
for i in range(H):
    s = input()
    ret = []
    for item in s:
        if item == "#":
            ret.append(1)
        else:
            ret.append(0)
    arr.append(ret)

arr2 = np.array(arr)

res = calculate(arr2)

print(res)

