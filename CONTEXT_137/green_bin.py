def ccc(n):
    #c(n,2)
    result = (n * (n-1))//2
    return result

def calculate(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return 0

    criteron = arr[0]
    res = [0]

    nextarr = []

    for i in range(1,len(arr)):
        if tellIsTheSame(criteron,arr[i]):
            res.append(i)
        else:
            nextarr.append(arr[i])

    return ccc(len(res)) + calculate(nextarr)

def tellIsTheSame(s1,s2):
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    length = len(s1)

    for i in range(length):
        if s1[i] != s2[i]:
            return False

    return True


arr = []

N = int(input())
for i in range(N):
    arr.append(input())


result = calculate(arr)
print(result)