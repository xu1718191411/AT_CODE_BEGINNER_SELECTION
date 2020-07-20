import math

# N = 4
# ARR = [10, 30, 40, 20]

N, K = 5, 3
ARR = [10, 30, 40, 50, 20]

#
# N,K = 3, 1
# ARR = [10, 20, 10]

# N,K = 2, 100
# ARR = [10, 10]


N, K = map(int, input().split())
ARR = list(map(int, input().split()))

def calculate(n, k, arr):
    result = [math.inf for i in range(n)]

    result[0] = 0
    result[1] = abs(arr[1] - arr[0])


    for i in range(2, n):
        srr = []
        for j in range(i-1, i -1 - k, -1):
            srr.append(abs(arr[i] - arr[j]) + result[j])

        result[i] = min(srr)

    print(result[-1])


calculate(N, K, ARR)