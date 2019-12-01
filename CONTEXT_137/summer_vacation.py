def calculate(arr,M):
    sum = 0
    for i in range(M):
        index = 0
        value = 0
        for j in range(len(arr)):
            lastDay = i + arr[j][0]
            if lastDay <= M:
                if arr[j][1] > value:
                    index = j
                    value = arr[j][1]

                if (arr[j][1] == value) and (arr[index][0] < arr[j][0]):
                    index = j
                    value = arr[j][1]

        if len(arr) > 0:
            sum += value
            arr.pop(index)

        if len(arr) == 0:
            break

    return sum

N, M = map(int, input().split())
arr = []
for i in range(N):
    day, mount = map(int, input().split())
    arr.append([day,mount])
result = calculate(arr,M)
print(result)