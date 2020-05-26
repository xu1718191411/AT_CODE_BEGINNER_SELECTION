import math

N, M = map(int,input().split())


def calculate(n, m):
    res = 1
    for i in range(1, int(math.pow(m, 0.5))):
        if m % i != 0:
            continue

        j = m // i

        if i <= m // n:
            res = max(res, i)

        if j <= m // n:
            res = max(res, j)

    print(res)


calculate(N, M)
