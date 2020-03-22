S = input().split(" ")
N = int(S[0])
M = int(S[1])
def calculate(n,m):

    s1 = (n * (n - 1)) // 2
    s2 = (m * (m - 1)) // 2

    print(s1 + s2)

calculate(N,M)