import math

X = int(input())
# X = 33981761


def calculate(x):

    b = 0
    while True:
        tmp1 = x + b ** 5
        a1 = math.pow(tmp1, 0.2)

        if (a1 - math.floor(a1) < 1e-7):
            print(int(a1), int(b))
            break

        tmp2 = x + (-1 * b) ** 5
        if tmp2 >= 0:
            a2 = math.pow(tmp2, 0.2)
            if (a2 - math.floor(a2) < 1e-7):
                print(int(a2), int(-1 * b))
                break

        b = b + 1


calculate(X)
