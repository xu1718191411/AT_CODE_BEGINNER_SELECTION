import math


# 冒泡排序
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


# 二分法找>=N 的最大的index
# 1 2 3 4 5 5

def half_search(arr, N, startIndex, endIndex):
    if startIndex == endIndex:
        return startIndex

    if arr[endIndex] == N:
        return endIndex

    if endIndex - startIndex == 1:
        if arr[endIndex] == N:
            return endIndex
        else:
            return startIndex

    m = (startIndex + endIndex) % 2
    if m == 1:
        # 偶数 2,5 => 3,4
        s1 = int((startIndex + endIndex - 1) / 2)
        s2 = s1 + 1
        value1 = arr[s1]

        if N <= value1:
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
            return half_search(arr, N, midIndex + 1, endIndex)


# 二分法找>N 的最小的index
# 1 2 3 4 5 5

def half_search_2(arr, N, startIndex, endIndex):
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
            return half_search_2(arr, N, startIndex, s2)
        else:
            return half_search_2(arr, N, s1, endIndex)
    else:
        # 奇数 3,6 => 5
        #
        midIndex = int((startIndex + endIndex + 1) / 2)
        midValue = arr[midIndex]

        if midValue > N:
            return half_search_2(arr, N, startIndex, midIndex)
        else:
            return half_search_2(arr, N, midIndex, endIndex)


def test_half_search():
    arr = [2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 7, 8, 12]

    arr = rank(arr)

    print(arr)

    index = half_search_2(arr, 468, 0, len(arr) - 1)

    print(index)


# atcoder 最小公倍数
import fractions


def smallestCommonAtcoder(a, b):
    return a * b / fractions.gcd(a, b)


# 一般情况下的最小公倍数smallestCommon
import math


def smallestCommon(a, b):
    return a * b / math.gcd(a, b)

# 二分查找
def find(start, end, arr, x):
    mid = (start + end) // 2
    midVal = arr[mid]

    if end - start == 1:
        s1 = x - arr[start]
        s2 = arr[end] - x
        if s1 < s2:
            return start
        else:
            return end

    if midVal > x:
        return find(start,mid,arr,x)
    elif midVal < x:
        return find(mid,end,arr,x)
    else:
        return mid


arr = [10,20,30,40,50,60,70,80,90,100]

result = find(0,10,arr,43)

print(result)