n = int(input())

S = input().split(" ")

arr = [int(s) for s in S]


def calculate(m, n):
    if m == n:
        return m
    elif m > n:
        s = m % n
        if s == 0:
            return n
        else:
            return calculate(n, s)
    else:
        s = n % m
        if s == 0:
            return m
        else:
            return calculate(m, s)


v = arr[0]

for index in range(1, n):
    v = calculate(v, arr[index])

print(v)