S = input().split(" ")
N = int(S[0])
R = int(S[1])

def calculate(n,r):
    if n >= 10:
        return r
    else:
        return r + (10 - n) * 100


result = calculate(N,R)
print(result)
