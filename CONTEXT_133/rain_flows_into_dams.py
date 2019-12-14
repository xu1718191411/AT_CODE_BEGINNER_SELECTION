def calculate(arr,S):

    result = []
    even = 0
    for i in range(len(arr)):

        if i % 2 == 0:
            even = S-calculate2(i+1,arr[i+1:])
            result.append(even)
        else:
            odd = arr[i-1]*2-even
            result.append(odd)
            S = S - even - odd

    return result

def calculate2(i,arr):
    # 取偶数项
    return sum(arr[::2])*2

def calculateTotaAmount(arr):
    return sum(arr)

def printArr(arr):
    result = ""
    for i in range(len(arr)):
        result += str(arr[i]) + " "

    return result



N = int(input())

S = input().split(" ")
aArr = [int(s) for s in S]


result = calculate(aArr,calculateTotaAmount(aArr))

print(" ".join([str(s) for s in result]))

