import math

math.floor(3.2)


def main():
    n, y = input().split(" ")
    n = int(n)
    y = int(y)

    a = 0
    b = 0

    while a <= n:
        while (a + b) <= n:
            c = n - a - b
            total = 10000*a + 5000*b + 1000*c
            if total == y:
                return str(a) + " " + str(b) + " " + str(c)
            b = b + 1
        b = 0
        a = a + 1

    return "-1 -1 -1"

print(main())
