N = int(input())
ARR = list(map(int,input().split()))

import math


def calculate(n, arr):
    result = -math.inf
    for i in range(n):
        j = len(arr) - 1

        maxEvenSum = -math.inf
        correctOddSum = 0

        while j >= 0:
            if j == i:
                j -= 1
                continue

            left = min(i, j)
            right = max(i, j)

            evenSum = 0
            oddSum = 0
            tmpArr = arr[left:right + 1]
            for index in range(len(tmpArr)):
                if (index) % 2 == 1:
                    evenSum += tmpArr[index]
                else:
                    oddSum += tmpArr[index]

            if evenSum >= maxEvenSum:
                maxEvenSum = evenSum
                correctOddSum = oddSum

            j -= 1


        result = max(result, correctOddSum)

    return result


res = calculate(N, ARR)

print(res)
