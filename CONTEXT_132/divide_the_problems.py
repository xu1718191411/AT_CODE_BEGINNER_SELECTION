def calculate(arr):
    length = len(arr)
    s1 = (length // 2) - 1
    s2 = (length // 2)

    if arr[s2] == arr[s1]:
        return 0
    else:
        return arr[s2] - arr[s1]

N = int(input())

if N == 0:
    result = 0
else:
    list = list([int(s) for s in  input().split(" ")])
    list.sort()
    result = calculate(list)

print(result)