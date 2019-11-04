n = input()
arr = input().split()

def changeType(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr

def sort(arr):

    index = len(arr) - 1
    while index >= 1:
        for i in range(index):
            if arr[i] < arr[i+1]:
                value = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = value
        index = index - 1

    return arr

def calculate(arr):
    aValue = 0
    bValue = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            aValue += arr[i]
            pass
        else:
            bValue += arr[i]
            pass
    return aValue,bValue




aValue,bValue = calculate(sort(changeType(arr)))

if(aValue > bValue):
    print(aValue - bValue)
else:
    print(bValue - aValue)
