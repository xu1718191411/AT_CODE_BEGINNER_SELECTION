N = int(input())
ARR = []

for i in range(N):
    ARR.append([int(s) for s in input().split(" ")])


import math

def calculate(n,arr):

    arr.insert(0,[0,0,0])

    result = True

    for i in range(1,n+1):

        diff = arr[i][0] - arr[i-1][0]

        distance = int(math.fabs(arr[i][1] - arr[i-1][1]) + math.fabs(arr[i][2] - arr[i-1][2]))

        if diff < distance:
            result = False
            break

        if (diff + distance) % 2 == 1:
            result = False
            break

    if result:
        print("Yes")
    else:
        print("No")


calculate(N,ARR)

