N, A, B = 7, 1, 2
ARR = [24, 35, 40, 68, 72, 99, 103]

N, A, B = map(int, input().split())
ARR = list(map(int, input().split()))


def calculate(n, a, b, arr):
    result = 0
    for i in range(1, n):
        result += min(B, (arr[i] - arr[i - 1]) * A)

    print(result)


calculate(N, A, B, ARR)
