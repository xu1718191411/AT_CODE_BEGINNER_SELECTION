def calculate(arr):
    N = len(arr)
    index = N - 1

    result = [0]*N
    result2 = []

    while index >= 0:

        if N // (index+1) > 1:
            v1 = calculate2(N // (index+1),index,result)

            if arr[index] % 2 == 0:
                if v1 % 2 == 0:
                    pass
                else:
                    result[index] = 1
                    result2.append(index + 1)
            else:
                if v1 % 2 == 0:
                    result[index] = 1
                    result2.append(index + 1)
                else:
                    pass

        else:
            if arr[index] == 0:
                result[index] = 0
            else:
                result[index] = 1
                result2.append(index + 1)

        index = index - 1

    return result,result2


def calculate2(len, base, arr):
    result = 0
    for i in range(2, len+1):
        result += arr[(base + 1) * i - 1]
    return result


N = int(input())
S = input().split(" ")
arr = [int(s) for s in S]

result, result2 = calculate(arr)

print(sum(result))
if len(result2) > 0:
    print(" ".join([str(s) for s in result2]))


