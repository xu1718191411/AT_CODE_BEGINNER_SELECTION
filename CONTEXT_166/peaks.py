N, M = 4, 3
HRR = [1, 2, 3, 4]
ARR = [
    [1, 3],
    [2, 3],
    [2, 4],
]

N,M =  map(int,input().split())
HRR = list(map(int,input().split()))
ARR = []
for i in range(M):
    ARR.append(list(map(int,input().split())))


def calculate(n, m, hrr, arr):
    dict = {}
    for i in range(n):
        dict.__setitem__(i, True)

    for ar in arr:
        start = ar[0] - 1
        end = ar[1] - 1
        if hrr[start] > hrr[end]:
            dict.__setitem__(end, False)
        if hrr[start] == hrr[end]:
            dict.__setitem__(start, False)
            dict.__setitem__(end, False)

        if hrr[start] < hrr[end]:
            dict.__setitem__(start,False)


    print(sum(list(dict.values())))

calculate(N,M,HRR,ARR)