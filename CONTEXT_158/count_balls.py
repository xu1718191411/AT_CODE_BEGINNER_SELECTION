S = input().split(" ")
N = int(S[0])
A = int(S[1])
B = int(S[2])

def calculate(n,a,b):
    s1 = n // (a + b)
    sum = a * s1

    s2 = n % (a + b)

    if s2 <= a:
        sum = sum + s2
    else:
        sum = sum + a

    return sum

result = calculate(N,A,B)

print(result)