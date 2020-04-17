S = input().split(" ")
N = int(S[0])
M = int(S[1])

ARR = []

for i in range(M):
    ARR.append([int(s) for s in input().split(" ")])

def calculate(n, m, arr):
    dict1 = [0 for i in range(n)]
    if n > 1:
        dict1[0] = 1
    dict2 = [False for i in range(n)]
    res = True
    for ar in arr:
        if n > 1 and ar[0] == 1 and ar[1] == 0:
            res = False
            break

        if dict2[ar[0] - 1] == True:
            if dict1[ar[0] - 1] != ar[1]:
                res = False
                break

        dict1[ar[0]-1] = ar[1]
        dict2[ar[0] - 1] = True

    if res == False:
        print(-1)
    else:
        print("".join([str(s) for s in dict1]))


calculate(N, M, ARR)
