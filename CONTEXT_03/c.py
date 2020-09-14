N, K = map(int, input().split())
ARR = list(map(int, input().split()))

def calculate(n, k, arr):
    arr = sorted(arr)
    arr = arr[n-k:]
    currentValue = 0
    for ar in arr:
        currentValue = (currentValue + ar) / 2
    print(currentValue)

calculate(N, K, ARR)
