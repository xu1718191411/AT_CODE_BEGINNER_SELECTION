# n = 4
# arr = [3, 1, 3, 2]
#
#
# n = 6
# arr = [105, 119, 105, 119, 105, 119]
#
# n = 4
# arr = [1, 1, 1, 1]




n = int(input())

arr = [int(s) for s in input().split(" ")]

def calculate(n, arr):
    evenDict = {}
    oddDict = {}

    for i in range(0, n, 2):
        if oddDict.get(arr[i]) == None:
            oddDict.__setitem__(arr[i], 1)
        else:
            oddDict.__setitem__(arr[i], oddDict.get(arr[i]) + 1)

    for i in range(1, n, 2):
        if evenDict.get(arr[i]) == None:
            evenDict.__setitem__(arr[i], 1)
        else:
            evenDict.__setitem__(arr[i], evenDict.get(arr[i]) + 1)

    if (len(evenDict.values()) == 1) and (len(oddDict.values()) == 1):
        if arr[0] == arr[1]:
            return n // 2

    evenMaxIndex = max(evenDict, key=evenDict.get)
    oddMaxIndex = max(oddDict, key=oddDict.get)

    s1 = (n // 2) - evenDict[evenMaxIndex]

    s2 = (n - n // 2) - oddDict[oddMaxIndex]

    return (s1 + s2)


result = calculate(n, arr)

print(result)
