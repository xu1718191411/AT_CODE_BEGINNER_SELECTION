N = 4
ARR = [2, 2, 1, 3]

N = 7
ARR = [1, 1, 1, 1, 1, 1, 1]

N = int(input())
ARR = list(map(int,input().split()))

# 3 2 2 1
def calculate(n, arr):
    endIndex = 0
    ans = 0

    arr = sorted(arr, reverse=True)
    for i in range(n):

        if i == 0:
            ans += arr[i]
            endIndex += 1
            continue

        endIndex += 1
        if endIndex >= n:
            break
        ans += arr[i]

        endIndex += 1
        if endIndex >= n:
            break
        ans += arr[i]

    print(ans)


calculate(N, ARR)
