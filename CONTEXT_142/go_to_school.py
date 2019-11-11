def calculate(n, arr):
    result = [0] * len(arr)

    for index, value in enumerate(arr):
        result[value - 1] = str(index + 1)

    return result


N = int(input())
S = input().split(' ')
arr = list(map(int, list(S)))
result = calculate(N, arr)


print(' '.join(result))
