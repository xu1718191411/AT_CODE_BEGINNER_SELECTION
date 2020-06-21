# N, K = 5, 3
# ARR = [50, 100, 80, 120, 80]
#
#
# N,K = 1, 1
# ARR = [1000]

N,K = map(int,input().split())
ARR = list(map(int,input().split()))
arr = sorted(ARR)


result = 0
for i in range(K):
    result += arr[i]

print(result)