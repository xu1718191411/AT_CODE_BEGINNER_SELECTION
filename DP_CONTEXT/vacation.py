# N = 3
# ARR = [
#     [10, 40, 70],
#     [20, 50, 80],
#     [30, 60, 90]
# ]


# N = 7
# ARR = [
#     [6, 7, 8],
#     [8, 8, 3],
#     [2, 5, 2],
#     [7, 8, 6],
#     [4, 6, 8],
#     [2, 3, 4],
#     [7, 5, 1]
# ]
#

N = int(input())
ARR = []

for i in range(N):
    ARR.append(list(map(int,input().split())))



def calculate(n, arr):
    result = []
    for index, ar in enumerate(arr):
        if index == 0:
            result.append(ar)
        else:
            s1 = max(result[-1][1] + ar[0], result[-1][2] + ar[0])
            s2 = max(result[-1][0] + ar[1], result[-1][2] + ar[1])
            s3 = max(result[-1][0] + ar[2], result[-1][1] + ar[2])
            result.append([s1, s2, s3])

    print(max(result[-1]))


calculate(N, ARR)
