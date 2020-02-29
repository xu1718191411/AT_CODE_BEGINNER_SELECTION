# S = input().split(" ")
# n = int(S[0])
# a = int(S[1])
# b = int(S[2])

n = 4
a = 1
b = 3
def calculate(n,a,b):
    sum = 0

    if n % 2 == 0:

        for i in range(1,n//2 + 1):

            if a > n // 2:
                a = n - a

            if b > n //2:
                b = n - b

            if i == a:
                if a == b:
                    continue
                else:
                    sum += comb(n, i, 10 ** 9 + 7)
            elif i == b:
                if a == b:
                    continue
                else:
                    sum += comb(n, i, 10 ** 9 + 7)
                continue

            sum += comb(n,i,10**9+7) * 2

    else:

        for i in range(1,n//2 + 1):

            if a > n //2 + 1:
                a = n - a + 1

            if b > n //2 + 1:
                b = n - b + 1

            if i == a:
                sum += comb(n, i, 10 ** 9 + 7)
                continue
            if i == b:
                sum += comb(n, i, 10 ** 9 + 7)
                continue

            sum += comb(n, i, 10 ** 9 + 7) * 2

        mid = comb(n, n //2 + 1)

        if (a != (n //2 + 1)) and (b != (n //2 + 1)):
            sum += mid

    return sum % (10**9+7)


def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod



result = calculate(n,a,b)

print(result)