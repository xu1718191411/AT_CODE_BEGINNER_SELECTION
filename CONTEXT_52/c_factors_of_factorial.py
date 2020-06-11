from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
count = Counter([])
for i in range(1, N + 1):
    res = prime_factorize(i)
    res = Counter(res)
    count += res

result = 1
for c in count.values():
    result = result * (c+1)
    result = result % 1000000007


print(result)