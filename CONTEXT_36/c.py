N = int(input())
ARR = []

for i in range(N):
    ARR.append(int(input()))


def calculate(n,arr):
    dict = {}
    mmr = set()

    for i in range(n):
        mmr.add(arr[i])

    arr2 = sorted(list(mmr))

    for i in range(len(arr2)):
        dict.__setitem__(arr2[i],i)
    for i in range(n):
        print(dict.get(arr[i]))



calculate(N, ARR)