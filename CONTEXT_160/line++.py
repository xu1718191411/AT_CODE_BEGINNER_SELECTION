import math
S = input().split(" ")
N = int(S[0])
X = int(S[1])
Y = int(S[2])


def calculate(n, x, y):
    result = []
    x = x - 1
    y = y - 1
    for i in range(1, n):
        result.append(0)

    for i in range(n):
        for j in range(i+1,n):
            distance1 = int(math.fabs(x-i) + math.fabs(y-j) + 1)
            distance2 = j - i
            distance = min(distance1,distance2)

            result[distance-1] = result[distance-1] + 1


    for res in result:
        print(res)


calculate(N, X, Y)
