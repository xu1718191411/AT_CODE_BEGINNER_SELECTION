a, b, x = 4, 8, 3
a, b, x = 0, 5, 1
a, b, x = 9, 9, 2
a, b, x = 1, 1000000000000000000, 3

a, b, x = map(int,input().split())


def calculate(a, b, x):
    s1 = (a - 1) // x

    if s1 < 0:
        s1 = 0
    else:
        s1 += 1
    s2 = b // x + 1

    print(s2 - s1)


calculate(a, b, x)
