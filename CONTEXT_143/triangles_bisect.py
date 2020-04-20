import bisect
# N = 7
# ARR = [218, 786, 704, 233, 645, 728, 389]
#
# N = 3
# ARR = [1, 1000, 1]

# N = 4
# ARR = [3, 4, 2, 1]

N = int(input())

ARR = list(map(int,input().split()))

def calculate(n,arr):
    arr = sorted(arr)
    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            mmm = arr[j] + arr[i] - 1
            nnn = bisect.bisect_right(arr,mmm)
            sum = sum + nnn - (j + 1)

    print(sum)


calculate(N,ARR)
