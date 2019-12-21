import math
def smallestCommon(a,b):
    return a*b/math.gcd(a,b)

def caluclate(a, b, c, d):

    s1 = (a - 1) // c
    s2 = (a - 1) // d

    m1 = s2 + s1

    s3 = b // c
    s4 = b // d

    m2 = s4 + s3

    common = int(smallestCommon(c,d))

    m3 = (b // common) - (a-1)//common

    total = int(b - a + 1)

    return total - (m2 - m1 - m3)


S = input().split(" ")
A = int(S[0])
B = int(S[1])
C = int(S[2])
D = int(S[3])

result = caluclate(A,B,C,D)

print(result)