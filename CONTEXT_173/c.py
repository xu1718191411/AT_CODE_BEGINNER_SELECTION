import itertools
import numpy as np

# H, W, K = 2, 3, 4
# ARR = [
#     "..#",
#     "###",
# ]
#
# H, W, K = 6, 6, 8
# ARR = [
#     "..##..",
#     ".#..#.",
#     "#....#",
#     "######",
#     "#....#",
#     "#....#"
# ]

H, W, K = map(int, input().split())
ARR2 = np.zeros((H, W))
for i in range(H):
    s = list(input())
    for j in range(W):
        if s[j] == ".":
            ARR2[i][j] == 0
        else:
            ARR2[i][j] = 1

# ARR2 = np.zeros((H, W))
# for i in range(H):
#     for j in range(W):
#         if ARR[i][j] == ".":
#             ARR2[i][j] == 0
#         else:
#             ARR2[i][j] = 1


def calclulate(h, w, k, arr):
    result = 0
    hIndex = [i for i in range(h)]
    wIndex = [i for i in range(w)]

    for hChooseNum in range(h + 1):
        for wChooseNum in range(w + 1):
            for m in itertools.combinations(hIndex, hChooseNum):
                for n in itertools.combinations(wIndex, wChooseNum):

                    tmpArr = arr.copy()

                    for _m in m:
                        tmpArr[_m, :] = 0
                    for _n in n:
                        tmpArr[:, _n] = 0

                    if np.sum(tmpArr == 1) == k:
                        result += 1
    print(result)


calclulate(H, W, K, ARR2)
