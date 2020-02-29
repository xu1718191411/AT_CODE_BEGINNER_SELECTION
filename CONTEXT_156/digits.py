S = input().split(" ")
n = int(S[0])
k = int(S[1])

def calculate(n,k):
    m = 0
    while k**m <= n:
        m = m + 1

    return m


result = calculate(n,k)

print(result)
