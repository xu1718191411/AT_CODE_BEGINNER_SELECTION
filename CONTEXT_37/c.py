N, K = 5, 3
ARR = [1, 2, 4, 8, 16]

N, K = map(int, input().split())
ARR = list(map(int, input().split()))


def calculate(n, k, arr):
    currentSum = sum(arr[:k])
    result = currentSum
    for i in range(1, n - k + 1):
        currentSum = currentSum + (arr[i + k - 1] - arr[i - 1])
        result += currentSum

    print(result)

calculate(N, K, ARR)