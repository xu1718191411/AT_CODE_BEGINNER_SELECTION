X, Y, A, B, C = 2, 2, 2, 2, 2
prr = [8, 6]
qrr = [9, 1]
krr = [2, 1]

X, Y, A, B, C = 2, 2, 4, 4, 4
prr = [11, 12, 13, 14]
qrr = [21, 22, 23, 24]
krr = [1, 2, 3, 4]

X, Y, A, B, C = 1, 2, 2, 2, 1
prr = [2, 4]
qrr = [5, 1]
krr = [3]

X, Y, A, B, C = map(int, input().split())
prr = list(map(int, input().split()))
qrr = list(map(int, input().split()))
krr = list(map(int, input().split()))


def calculate(x, y, a, b, c, prr, qrr, krr):
    prr = sorted(prr, key=lambda x: -x)
    qrr = sorted(qrr, key=lambda x: -x)

    prr = prr[:x]
    qrr = qrr[:y]

    result = []
    result.extend(prr)
    result.extend(qrr)
    result.extend(krr)

    result = sorted(result, key=lambda x: -x)

    result = result[:(x + y)]

    print(sum(result))


calculate(X, Y, A, B, C, prr, qrr, krr)
