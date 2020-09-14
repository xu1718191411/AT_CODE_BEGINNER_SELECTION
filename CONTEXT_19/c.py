N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    resSet = set()
    for i in range(n):
        resSet.add(bunkai(arr[i]))
    print(len(resSet))


def bunkai(n):
    while n % 2 == 0:
        n = n // 2
    return n


calculate(N, ARR)
