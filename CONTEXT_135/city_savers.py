def calculate(arr1,arr2):

    result = 0
    for i in range(len(arr2)):

        if (arr1[i] + arr1[i+1]) >= arr2[i]:
            result += arr2[i]
        else:
            result += arr1[i] + arr1[i+1]

        res1 = arr2[i] - arr1[i]

        if arr2[i] >= arr1[i]:
            arr1[i] = 0
        else:
            arr1[i] = arr1[i] - arr2[i]

        if res1 > 0:
            if arr1[i+1] >= res1:
                arr1[i+1] = arr1[i+1] - res1
            else:
                arr1[i+1] = 0


    return result


N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = calculate(arr1, arr2)

print(result)




