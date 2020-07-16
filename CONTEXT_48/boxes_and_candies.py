N, X = 6, 1
ARR = [1, 6, 1, 2, 0, 4]

N, X = 3, 3
ARR = [2, 2, 2]

N, X = 5, 9
ARR = [3, 1, 4, 1, 5]

N, X = 2, 0
ARR = [5, 5]

N, X = map(int, input().split())

ARR = list(map(int, input().split()))


def calculate(n, x, arr):
    result = 0
    for i in range(1, n):
        sSum = arr[i - 1] + arr[i]
        if sSum <= x:
            continue

        diff = sSum - x

        if diff <= arr[i]:
            arr[i] -= diff
            result += diff
        else:
            result += diff
            arr[i] = 0

    print(result)


calculate(N, X, ARR)
