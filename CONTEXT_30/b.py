N, M = map(int, input().split())


def calculate(n, m):
    h1 = 360 * (n % 12 + (m / 60)) / 12
    m1 = 360 * (m / 60)

    print(min(abs(h1 - m1),360 - abs(h1 - m1)))


calculate(N, M)
