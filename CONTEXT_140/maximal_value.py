def minValue(a,b):
    return b if a > b else a

def getSum(arr):
    return sum(list(arr))

def calculate(arr,n):

    ret = []

    for i in range(n):
        if i == 0:
            ret.append(arr[0])
        elif i == len(arr):
            ret.append(arr[i-1])
        else:
            ret.append(minValue(arr[i],arr[i-1]))

    return ret


N = int(input())
S = input().split()
arr = list(map(int, list(S)))
result = calculate(arr,N)
ret = getSum(list(result))
print(ret)