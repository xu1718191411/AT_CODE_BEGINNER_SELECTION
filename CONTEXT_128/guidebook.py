N = 6
ARR = [
    ["khabarovsk", 20],
    ["moscow", 10],
    ["kazan", 50],
    ["kazan", 35],
    ["moscow", 60],
    ["khabarovsk", 40]
]
N = int(input())
ARR = []

for i in range(N):
    arr = input().split()
    ARR.append([arr[0], int(arr[1])])


def calculate(n, arr):
    dict = {}
    for i in range(N):
        if dict.get(arr[i][0]) == None:
            dict.__setitem__(arr[i][0], [[arr[i][1], i]])
        else:
            rates = dict.get(arr[i][0])
            rates.append([arr[i][1], i])
            rates = sorted(rates, key=lambda x: -x[0])
            dict.__setitem__(arr[i][0], rates)

    keys = sorted(dict.keys())

    for key in keys:
        aaa = dict.get(key)
        for a in aaa:
            print(a[1] + 1)


calculate(N, ARR)
