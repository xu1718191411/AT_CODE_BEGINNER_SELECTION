def max(arr):
    if len(arr) == 0:
        return 0
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def calculate(arr,n):

    if len(arr) == 0:
        return []

    start = 0
    ret = []

    for i in range(n):
        if i == 0:
            continue
        else:
            if arr[i] > arr[i-1]:
                ret.append(i-1-start)
                start = i

            if i == (len(arr) - 1):
                ret.append(i - start)
    return ret

N = int(input())
S = input().split()
arr = list(map(int, list(S)))

ret = max(calculate(arr,N))
print(ret)