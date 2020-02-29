S = input().split(" ")
n = int(S[0])
k = int(S[1])

def calculate(n,k):
    if k % 2 == 0:
        #选取所有能被K整除的数
        s1 = n // k
        s2 = 0
        for i in range(1,n+1):
            if i % k == k/2:
                s2 = s2 + 1
        return s1**3 + s2**3
    else:
        s1 = n // k
        return s1**3

result = calculate(n,k)

print(result)