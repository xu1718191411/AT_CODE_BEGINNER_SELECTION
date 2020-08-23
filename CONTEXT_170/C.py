X, N = 6, 5
PRR = [4, 7, 10, 6, 5]

# X, N = 10, 5
# PRR = [4, 7, 10, 6, 5]

# X,N = 100, 0
# PRR = []

X, N = map(int, input().split())
PRR = list(map(int, input().split()))


def calculate(x, n, prr):
    up = x
    while up in prr:
        up = up + 1

    down = x - 1

    while down in prr:
        down = down - 1

    if abs(x - down) == abs(x - up):
        return min(down, up)

    if abs(x - down) < abs(x - up):
        return down
    else:
        return up


result = calculate(X, N, PRR)

print(result)
