def calculate(arr):

    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        result = (arr[0] + arr[1]) / 2
        return result

    if len(arr) > 2:
        res = (arr[-1] + arr[-2]) / 2
        newArr = arr[:-2]
        newArr.append(res)
        return calculate(newArr)

def rank(arr):
    lastIndex = len(arr) - 1
    while lastIndex > 0:
        for i in range(lastIndex):
            if arr[i + 1] > arr[i]:
                tmp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = tmp

        lastIndex = lastIndex - 1
    return arr

N = int(input())
S = input().split(" ")
arr = list(map(int, list(S)))
newArr = rank(arr)

result = calculate(list(arr))
print(result)