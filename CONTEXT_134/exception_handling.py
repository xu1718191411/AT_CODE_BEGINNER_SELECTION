def calculate(arr):

    largest,second = findLargetAndSecond(arr)

    for i in range(len(arr)):
        value = arr[i]
        if largest != value:
            print(largest)
        else:
            print(second)


def findLargetAndSecond(arr):
    largest = 0
    second = 0

    for i in range(0,len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        else:
            if arr[i] >= second:
                second = arr[i]

    return largest,second



N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

calculate(arr)

