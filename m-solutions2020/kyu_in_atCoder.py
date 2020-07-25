N = int(input())


def calculate(n):
    if n <= 599:
        print(8)
        return

    if n <= 799:
        print(7)
        return

    if n <= 999:
        print(6)
        return

    if n <= 1199:
        print(5)
        return

    if n <= 1399:
        print(4)
        return

    if n <= 1599:
        print(3)
        return

    if n <= 1799:
        print(2)
        return

    if n <= 1999:
        print(1)
        return

calculate(N)