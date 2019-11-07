def calculate(S):
    arr = list(S)

    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return 1

    N = len(arr)

    tmp = 1
    for i in range(1,N):
        if arr[i] != arr[i-1]:
            tmp = tmp + 1
    return tmp

N = input()
S = input()
res = calculate(S)
print(res)