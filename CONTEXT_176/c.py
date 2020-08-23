N = int(input())
ARR = list(map(int,input().split()))



def calculate(n, arr):
    currentHeight = arr[0]
    result = 0
    for i in range(1,n):
        if arr[i] < currentHeight:
            result += (currentHeight - arr[i])
        else:
            currentHeight = arr[i]

    return result

res = calculate(N, ARR)

print(res)

