import math
# N = 2
# ARR = [4, 8]
#
# N = 3
# ARR = [4, 2, 5]
#
#
# N = 4
# ARR = [-100, -100, -100, -100]

N = int(input())
ARR = list(map(int,input().split()))

def calculate(n, arr):

    a1 = math.floor(sum(arr)/n)
    a2 = math.ceil(sum(arr)/n)

    result1 = 0
    result2 = 0
    for i in range(n):
        result1 += pow(arr[i] - a1,2)
        result2 += pow(arr[i] - a2,2)

    print(min(result1,result2))


calculate(N, ARR)