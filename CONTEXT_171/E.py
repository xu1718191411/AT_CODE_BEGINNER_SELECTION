N = 4
ARR = [20, 11, 9, 24]

N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    s = arr[0]
    for i in range(1, n):
        s = s ^ arr[i]

    result = []

    for i in range(n):
        result.append(str(arr[i] ^ s))

    print(" ".join(result))


calculate(N, ARR)
