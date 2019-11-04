def convert(arr):
    return [int(n) for n in arr]


def first(arr):
    appended = False
    if arr[0] == 0:
        arr.insert(0, 1)
        appended = True
    return arr,appended


def tank(arr):
    tank = []

    if len(arr) == 1:
        tank.append(1)
        return tank

    tankItemCount = 0
    for i in range(0, len(arr)):
        if i == 0:
            tankItemCount = tankItemCount + 1
            continue

        if arr[i] == arr[i - 1]:
            tankItemCount = tankItemCount + 1
        else:
            tank.append(tankItemCount)
            tankItemCount = 1

        if i == len(arr) - 1:
            tank.append(tankItemCount)

    return tank


def sumArr(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum


def calculateSum(arr, indexes):
    sum = 0
    for index in indexes:
        sum = sum + arr[index]

    return sum


def calculateIndex(arr, k):
    bigest = 0
    finalIndexes = []
    sss = [n for n in range(1, len(arr), 2)]
    for s in range(len(sss)):
        tmpIndexes = sss[s:s + k]
        tmp = calculateSum(arr, tmpIndexes)
        if tmp > bigest:
            bigest = tmp
            finalIndexes = tmpIndexes

    return finalIndexes


def sumTotal(arr,indexs):
    sum = 0
    for i in range(len(indexs)):

        sum = sum + arr[indexes[i]-1]
        sum = sum + arr[indexes[i]]
        if i == len(indexs) - 1:
            if(len(arr)-1) > indexes[i]:
                sum = sum + arr[indexes[i]+1]

    return sum


N,K = input().split()
N = int(N)
K = int(K)

S = list(input())

arr = convert(S)

arr,appended = first(arr)
a = tank(arr)

if(len(a) == 1):
    print(len(a))
else:
    indexes = (calculateIndex(a, K))
    result = sumTotal(a, indexes)
    if indexes[0] == 1 and appended:
        result = result - 1

    print(result)