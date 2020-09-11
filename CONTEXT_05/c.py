T = int(input())
N = int(input())
ARR = list(map(int,input().split()))
M = int(input())
BRR = list(map(int,input().split()))

def calculate(t, n, arr, m, brr):

    brrIndex = 0
    for i in range(n):
        if (brrIndex < m) and (arr[i] >= (brr[brrIndex] - t)) and (arr[i] <= brr[brrIndex]):
            brrIndex += 1

    if brrIndex >= (m):
        print("yes")
    else:
        print("no")

calculate(T, N, ARR, M, BRR)
