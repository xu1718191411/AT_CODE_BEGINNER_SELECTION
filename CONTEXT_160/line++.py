N = 5
X = 2
Y = 4


def calculate(n, x, y):
    for distance in range(n-1):
        distance = distance + 1

        if (y - x) == distance:
            m = n - distance  + 1
        else:
            m = n - distance - (y - x)
        print(distance,m)



calculate(N, X, Y)
