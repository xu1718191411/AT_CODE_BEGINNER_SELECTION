# N, W = 3, 8
# ARR = [
#     [3, 30],
#     [4, 50],
#     [5, 60],
# ]
# #
N, W, = 6, 15
ARR = [
    [6, 5],
    [5, 6],
    [6, 4],
    [6, 6],
    [3, 5],
    [7, 2],
]



N,W = map(int,input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int,input().split())))


def calculate(n, w, arr):
    srr = [[0] * (w+1) for i in range(n+1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - arr[i - 1][0] >= 0:
                s1 = srr[i - 1][j]
                s2 = srr[i - 1][j - arr[i - 1][0]] + arr[i - 1][1]
                srr[i][j] = max(s1, s2)
            else:
                srr[i][j] = srr[i-1][j]

    print(srr[-1][-1])


calculate(N, W, ARR)
