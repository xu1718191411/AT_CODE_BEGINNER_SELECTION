def calculate(arr):

    if len(arr) <= 1:
        return True

    index = len(arr) - 1
    while index >= 1:
        if arr[index - 1] - arr[index] > 1:
            return False
        if arr[index - 1] - arr[index] == 1:
            arr[index - 1] = arr[index -1 ] - 1
        index = index - 1
    return True




N = int(input())
arr = list(map(int, input().split()))

if len(arr) != N:
    print("No")
else:
    result = calculate(arr)
    if result:
        print("Yes")
    else:
        print("No")