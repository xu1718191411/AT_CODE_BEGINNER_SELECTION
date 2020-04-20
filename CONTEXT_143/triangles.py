import math


def rank(arr):
    lastIndex = len(arr) - 1
    while lastIndex > 0:

        for i in range(lastIndex):
            if arr[i + 1] < arr[i]:
                tmp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = tmp

        lastIndex = lastIndex - 1

    return arr

def half_search(arr, N, startIndex, endIndex):
    if startIndex == endIndex:
        if arr[startIndex] > N:
            return startIndex
        else:
            return -1

    if endIndex - startIndex == 1:

        if arr[startIndex] > N:
            return startIndex
        else:

            if arr[endIndex] <= N:
                return -1

            return endIndex

    m = (startIndex + endIndex) % 2

    if m == 1:
        # 偶数 2,5 => 3,4
        s1 = int((startIndex + endIndex - 1) / 2)
        s2 = s1 + 1
        value1 = arr[s1]

        if N < value1:
            return half_search(arr, N, startIndex, s2)
        else:
            return half_search(arr, N, s1, endIndex)
    else:
        # 奇数 3,6 => 5
        #
        midIndex = int((startIndex + endIndex + 1) / 2)
        midValue = arr[midIndex]

        if midValue > N:
            return half_search(arr, N, startIndex, midIndex)
        else:
            return half_search(arr, N, midIndex, endIndex)

def calculate(arr):
    if len(arr) < 3:
        return 0

    index = len(arr) - 1
    result = 0
    while index - 2 >= 0:

        s1 = arr[index] # 最大的值

        secondIndex = index - 1

        while secondIndex - 1 >= 0:

            s2 = arr[secondIndex]

            left = arr[:secondIndex]

            dirrerence = math.fabs(s2 - s1)
            t = half_search(left, dirrerence, 0, len(left) - 1)
            res = 0
            if t >= 0:
                res = len(left) - t
            result = result + res

            secondIndex = secondIndex - 1
        index = index - 1

    return result

N = input()
S = list(input().split(' '))
S = list(map(int, S))

arr = rank(S)
result = calculate(arr)
print(result)