import math

N, D = map(int, input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int, input().split())))


def calculate(n, d, arr):

    result = 0
    for i in range(n):
        distance = math.sqrt(pow(arr[i][0], 2) + pow(arr[i][1], 2))
        if distance <= d:
            result += 1

    print(result)

calculate(N, D, ARR)
