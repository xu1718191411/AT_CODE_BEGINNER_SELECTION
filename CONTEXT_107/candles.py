import math
S = input().split(" ")
N = int(S[0])
K = int(S[1])
arr = [int(s) for s in input().split(" ")]


def calculate(n, k, arr):
    minsArr = []
    plusArr = []
    for ar in arr:
        if ar < 0:
            minsArr.append(ar)
        else:
            plusArr.append(ar)

    # find start index
    startIndex = -10000

    if len(minsArr) > k:
        startIndex = len(minsArr) - k
    else:
        startIndex = 0

    minValues = []
    while startIndex <= len(minsArr):

        if k == N:
            s1 = arr[0]
            s2 = arr[-1]
            minValue = math.fabs(s2 - s1) + min(math.fabs(s2), math.fabs(s1))
            minValues.append(minValue)
            break

        if startIndex + k > len(arr):
            break

        s1 = arr[startIndex]
        s2 = arr[startIndex + k - 1]

        minValue = 0

        if s1 * s2 < 0:
            minValue = math.fabs(s2 - s1) + min(math.fabs(s2), math.fabs(s1))
        else:
            # 全部为正数
            if s1 >= 0:
                minValue = math.fabs(s2)
            # 全部为负数
            else:
                minValue = math.fabs(s1)

        minValues.append(minValue)
        startIndex = startIndex + 1

    return int(min(minValues))


result = calculate(N, K, arr)
print(result)
