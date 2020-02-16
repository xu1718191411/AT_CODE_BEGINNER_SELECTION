S = input().split(" ")
n = int(S[0])
k = int(S[1])
arr = []
for i in range(n):
    arr.append(int(input()))

def calculate(n,k,arr):
    arr.sort()
    drr = []
    for i in range(1,n):
        drr.append(arr[i] - arr[i-1])

    i = 0
    sums = []
    while (i + k-1) <= len(drr):
        tmp = sum(drr[i:i + k-1])
        sums.append(tmp)
        i = i + 1
    print(min(sums))

calculate(n,k,arr)