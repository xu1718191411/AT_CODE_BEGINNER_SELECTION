N, K = 5, 3
ARR = [96, 98, 95, 100, 20]


N, K = 3, 2
ARR = [1001, 869120, 1001]

N ,K = 15, 7
ARR = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

N, K = map(int,input().split())
ARR = list(map(int,input().split()))


def calculate(n, k, arr):
    for i in range(k, n):
        s = arr[i] / arr[i-k]
        if s > 1:
            print("Yes")
        else:
            print("No")

calculate(N, K, ARR)
