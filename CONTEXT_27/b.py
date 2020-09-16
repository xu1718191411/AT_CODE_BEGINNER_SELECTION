N = int(input())
ARR = list(map(int,input().split()))


def calculate(n,arr):

    if sum(arr) % n > 0:
        print(-1)
        return

    i = 0

    currentCount = 1
    currentSum = 0
    result = 0

    average = sum(arr) // n

    while i < n:

        currentSum += arr[i]
        if (currentSum / currentCount) == average:
            result += (currentCount-1)
            currentCount = 1
            currentSum = 0
        else:
            currentCount += 1

        i += 1

    print(result)

calculate(N, ARR)