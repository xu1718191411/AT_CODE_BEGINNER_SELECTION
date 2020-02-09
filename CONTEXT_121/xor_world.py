def calculate(m,n):
    s1 = calculate2(m-1)
    s2 = calculate2(n)
    return xor(s1,s2)

# from 0
def calculate2(n):
    if n % 2 == 1:
        if ((n - 1) / 2) % 2 == 0:
            return xor(xor(0,n-1),n)
        else:
            return xor(xor(1,n-1),n)

    else:
        if ((n / 2) % 2) == 0:
            return xor(0,n)
        else:
            return xor(1,n)

def xor(m,n):
    return n ^ m


S = input().split(" ")

result = calculate(int(S[0]),int(S[1]))

print(result)