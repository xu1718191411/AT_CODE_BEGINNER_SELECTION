from collections import deque

N, M, K = 3, 4, 240
ARR = [60, 90, 120]
BRR = [80, 150, 80, 150]
#
# N, M, K = 3, 4, 730
# ARR = [60, 90, 120]
# BRR = [80, 150, 80, 150]

N, M, K = 5, 4, 1
ARR = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
BRR = [1000000000, 1000000000, 1000000000, 1000000000]

N, M, K = 7, 4, 14
ARR = [1, 6, 1, 1, 1, 7, 2]
BRR = [5, 1, 5, 6, 7]

N, M, K = map(int, input().split())
ARR = list(map(int, input().split()))
BRR = list(map(int, input().split()))


def calculate(n, m, k, arr, brr):
    q = deque()

    result = []
    total = 0

    for i in range(n):
        if (total + arr[i]) > k:
            break
        total += arr[i]
        q.append(arr[i])

    result.append(len(q))

    remain = k - total

    q2 = deque(brr)
    sss = 0

    while (len(q2) > 0) and ((sss + q2[0]) <= remain):
        v = q2.popleft()
        sss += v

    result.append(len(q) + (m - len(q2)))

    while len(q) > 0:
        right = q.pop()
        remain += right

        while (len(q2) > 0) and ((sss + q2[0]) <= remain):
            v = q2.popleft()
            sss += v

        result.append(len(q) + (m - len(q2)))

    print(max(result))


calculate(N, M, K, ARR, BRR)
