def calculate(n,m,arr):

    if n >= m:
        print(0)
        return

    arr.sort()
    drr = list([])
    for index in range(1,len(arr)):
        drr.append(arr[index] - arr[index-1])
    drr.sort()
    drr = drr[:(m-n)]
    print(sum(drr))



S = input().split(" ")
n = int(S[0])
m = int(S[1])

S = input().split(" ")

arr = list([int(s) for s in S])


calculate(n,m,arr)
