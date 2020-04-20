N,K = map(int,input().split())


sum = 0
for k in range(K,N+2):
    # sum(arr[0:0+k]), sum([l-,l])
    s1 = ((0 + k-1) * k) // 2
    s2 = (((N - k + 1) + N) * k) // 2
    sum = sum + (s2 - s1 + 1)

print(sum % (1000000000 + 7))