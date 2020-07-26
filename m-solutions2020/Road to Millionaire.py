N = 2
ARR = [157, 193]

N = 6
ARR = [200, 180, 160, 140, 120, 100]

N = 7
ARR = [100, 130, 130, 130, 115, 115, 150]

N = int(input())
ARR = list(map(int, input().split()))
#

# N = 5
# ARR = [111, 111, 111, 111, 111]

def prepare(n,arr):
    result = []
    for i in range(n):
        if i == 0:
            result.append(arr[0])
        else:
            if arr[i] != arr[i-1]:
                result.append(arr[i])
    return result


def calculate(arr):
    n = len(arr)
    result = []
    for i in range(n):
        if i == n-1:
            if arr[i] > arr[i-1]:
                result.append({'type': 1, 'value': arr[i]})
            continue

        if i == 0:
            if arr[1] > arr[0]:
                result.append({'type': 0, 'value': arr[i]})
            continue

        if (arr[i + 1] > arr[i]) and (arr[i] < arr[i - 1]):
            result.append({'type': 0, 'value': arr[i]})

        if (arr[i + 1] < arr[i]) and (arr[i] > arr[i - 1]):
            result.append({'type': 1, 'value': arr[i]})

    money = 1000
    num = 0
    for index,res in enumerate(result):
        type = res.get('type')
        value = res.get('value')

        if index == (len(result) - 1):
            if value == 1:
                continue

        if type == 0:
            tmpNum = money // value
            num += tmpNum
            money -= value * tmpNum
        else:
            money += num * value
            num = 0

    print(money)


arr = prepare(N, ARR)
calculate(arr)
