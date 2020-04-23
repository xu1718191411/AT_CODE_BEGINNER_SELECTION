# N = 8
# K = 9
# ARR = [7, 9, 3, 2, 3, 8, 4, 6]
#
# N = 3
# K = 0
# ARR = [1000000000, 1000000000, 1000000000]
#
#
# N = 3
# K = 1
# ARR = [4, 1, 5]

N,K = map(int,input().split())
ARR = list(map(int,input().split()))

def calculate(n,k,arr):
    result = 0
    arr = sorted(arr)
    for i in range(n-k):
        result = result + arr[i]

    print(result)

calculate(N,K,ARR)