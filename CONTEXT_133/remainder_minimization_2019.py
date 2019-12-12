def calculate(l,r):
    K = 2019

    min = r*r

    if r > l + K * 2:
        r = l + K * 2

    for i in range(l,r+1):
        for j in range(i+1,r+1):
            ret = (i*j) % K
            if ret < min:
                min = ret
                if min == 0:
                    return min

    return min

S = input().split()

L = int(S[0])
R = int(S[1])

print(calculate(L,R))


