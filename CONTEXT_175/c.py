import math

# X, K, D = 6, 2, 4

# X, K, D = 7, 4, 3

# X, K, D = 10, 1, 2


# X, K, D = 1000000000000000, 1000000000000000, 1000000000000000

# X, K, D = 4, 4, 4


X, K, D = map(int,input().split())

def calculate(x, k, d):
    x = abs(x)
    d = abs(d)
    n = x / d
    kk = math.floor(n)

    if k <= kk:
        return x - k * d

    k = k - kk

    if k % 2 == 0:
        return x - kk * d
    else:
        current = x - kk * d
        return abs(current - d)


result = calculate(X, K, D)

print(result)
