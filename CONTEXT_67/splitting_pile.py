import math
# N = 2
# ARR = [10, -10]
#
# N = 6
# ARR = [1, 2, 3, 4, 5, 6]

N = int(input())
ARR = [int(s) for s in input().split(" ")]
def calculate(n,arr):
    lSum = 0
    tSum = sum(arr)
    res = []
    for index in range(n-1):
        ar = arr[index]
        lSum = lSum + ar
        rSum = tSum - lSum
        res.append(int(math.fabs(lSum-rSum)))

    print(min(res))



calculate(N,ARR)