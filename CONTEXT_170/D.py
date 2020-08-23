N = 5
ARR = [24, 11, 8, 3, 16]

N = 4
ARR = [5, 5, 5, 5]

N = 10
ARR = [33, 18, 45, 28, 8, 19, 89, 86, 2, 4]

N = int(input())
ARR = list(map(int,input().split()))

def calculate(n, arr):
    krr = [0 for i in range(1, 1000007)]

    for i in range(n):
        start = arr[i]

        if krr[start] > 0:
            krr[start] = 2
            continue

        for j in range(start, 1000006, start):
            krr[j] += 1

    result = 0
    for i in range(n):
        if krr[arr[i]] == 1:
            result += 1

    print(result)


calculate(N, ARR)
