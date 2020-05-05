N, K = map(int,input().split())

ARR = []

for i in range(K):
    num = int(input())
    ele = list(map(int,input().split()))
    ARR.append({"num": num, "ele": ele})

def calculate(n, k, arr):
    result = {}
    for i in range(1, n + 1):
        result.__setitem__(i, False)

    for ar in arr:
        for sr in ar["ele"]:
            result.__setitem__(sr,True)
    tt = 0

    for index,res in result.items():
        if res == False:
            tt = tt + 1

    print(tt)


calculate(N, K, ARR)
