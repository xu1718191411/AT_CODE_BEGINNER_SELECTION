n, a, b = 10, 2, 3

n, a, b = map(int,input().split())


def jiecheng(start, end):
    res = 1

    for i in range(start, end + 1):
        res = (res * i) % (10 ** 9 + 7)

    return res

def comb(n, a):
    X = jiecheng(n - a + 1, n) % (10**9  + 7)
    Y = jiecheng(1, a)

    S = X * pow(Y, 10 ** 9 + 5, 10 ** 9 + 7)
    return S


def calculate(n, a, b):
    s = pow(2, n, 10 ** 9 + 7) - 1
    s1 = comb(n, a)
    s2 = comb(n, b)
    res = s - s1 - s2
    res = res % (10**9 + 7)
    return res


result = calculate(n, a, b)
print(result)


