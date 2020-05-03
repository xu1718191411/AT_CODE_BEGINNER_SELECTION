K = int(input())
A, B = map(int, input().split())


def calculate(k, a, b):
    result = False
    for i in range(a, b + 1):
        if i % k == 0:
            result = True
            break

    if result == True:
        print("OK")
    else:
        print("NG")


calculate(K, A, B)
