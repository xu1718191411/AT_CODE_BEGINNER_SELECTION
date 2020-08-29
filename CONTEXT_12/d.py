import math

N, M = map(int, input().split())

ARR = []

for i in range(M):
    ARR.append(list(map(int, input().split())))


def prepare(n, m, arr):
    distance = [[math.inf for j in range(n)] for i in range(n)]

    for i in range(m):
        start = arr[i][0] - 1
        end = arr[i][1] - 1
        dis = arr[i][2]

        distance[start][end] = dis
        distance[end][start] = dis

    for i in range(n):
        distance[i][i] = 0

    return distance


def calculate(n, m, arr):
    dp = prepare(n, m, arr)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if dp[i][j] > (dp[i][k] + dp[k][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]

    result = math.inf

    for i in range(n):
        result = min(result,max(dp[i]))

    print(result)



calculate(N, M, ARR)
