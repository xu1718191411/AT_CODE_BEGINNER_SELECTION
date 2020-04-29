N, K = 3, 4
ARR = [
    [1, 1],
    [2, 2],
    [3, 3],
]

# N,K = 10, 500000
# ARR = [
#     [1, 100000],
#     [1, 100000],
#     [1, 100000],
#     [1, 100000],
#     [1, 100000],
#     [100000, 100000],
#     [100000, 100000],
#     [100000, 100000],
#     [100000, 100000],
#     [100000, 100000]
# ]

N, K = map(int, input().split())
ARR = []
for i in range(N):
    ARR.append(list(map(int,input().split())))

def calculate(n, k, arr):
    dict = {}
    for ar in arr:
        if dict.get(int(ar[0])) == None:
            dict.__setitem__(int(ar[0]), int(ar[1]))
        else:
            dict.__setitem__(int(ar[0]), dict.__getitem__(ar[0]) + ar[1])

    kkk = 0
    for key in sorted(dict.keys()):
        kkk = kkk + dict.get(key)
        if kkk >= k:
            print(key)
            break


calculate(N, K, ARR)
