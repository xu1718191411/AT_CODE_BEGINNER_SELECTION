N, X = map(int, input().split())
ARR = list(map(int, input().split()))


def calculate(n, x, arr):
    result = 0
    for i in range(n):
        if (x >> i & 1) == 1:
            result += arr[i]
    print(result)
calculate(N, X, ARR)
