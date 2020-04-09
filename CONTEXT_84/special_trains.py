import math

N = int(input())
ARR = []

for i in range(N-1):
    ARR.append([int(s) for s in input().split(" ")])


def calculate(n, arr):
    result = []
    for i in range(n-1):
        m = arr[i][1] + arr[i][0]
        for j in range(i+1,n-1):
            nextStart = arr[j][1]
            nextCost = arr[j][0]
            nextFrequency = arr[j][2]

            if m <= nextStart:
                m = nextStart

            if m  > nextStart:
                m = nextStart + math.ceil((m - nextStart)/ nextFrequency)*nextFrequency

            m = m + nextCost
        result.append(m)

    result.append(0)
    return result


result = calculate(N, ARR)


for res in result:
    print(res)