A, B = map(int,input().split())

def yinshufenjie(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf


def calculate(a,b):
    s1 = yinshufenjie(a)
    s2 = yinshufenjie(b)

    set1 = set()
    set2 = set()
    for key in s1.keys():
        set1.add(key)

    for key in s2.keys():
        set2.add(key)

    a = set1 & set2
    print(len(a)+1)


calculate(A,B)