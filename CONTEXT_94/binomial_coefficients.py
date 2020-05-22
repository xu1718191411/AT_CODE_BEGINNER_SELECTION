import bisect

N = 5
ARR = [6, 9, 4, 2, 11]


N = 2
ARR = [100, 0]

N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    arr = sorted(arr)

    mid = arr[n - 1] / 2

    a1 = bisect.bisect_left(arr, mid)

    s1 = abs(arr[a1 - 1] - (arr[n - 1] / 2))
    s2 = abs(arr[a1] - (arr[n - 1] / 2))

    if s1 > s2:
        return arr[n - 1],arr[a1]
    else:
        return arr[n-1],arr[a1-1]


n, a = calculate(N, ARR)
print(n, a)
