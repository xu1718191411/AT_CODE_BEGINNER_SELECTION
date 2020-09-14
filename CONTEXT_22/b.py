from collections import defaultdict

N = int(input())
ARR = []

for i in range(N):
    ARR.append(int(input()))

def calculate(n, arr):
    dict = defaultdict(lambda :0)
    result = 0
    for i in range(n):
        value = arr[i]
        if dict[value] == 0:
            dict[value] += 1
        else:
            dict[value] -= 0
            result += 1
    print(result)

calculate(N, ARR)
