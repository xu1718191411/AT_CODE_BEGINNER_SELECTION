import math

def getMax(arr):
    maxValue = max(list(arr))
    maxIndex = list(arr).index(maxValue)

    return maxIndex,maxValue


def getSum(arr):
    return sum(list(arr))

def calculate(arr,n):
    if n == 0:
        return getSum(arr)
    else:
        index,value = getMax(arr)
        if value == 0:
            return value
        n -= 1
        arr[index] = math.floor(value/2)
        return calculate(arr,n)

S = input().split(' ')
m = int(S[0])
n = int(S[1])

T = input().split(' ')
arr = list(map(int, list(T)))


result = calculate(arr,n)
print(result)