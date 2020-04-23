import math

1# A = 2
# B = 2
# V = 4
#
# A = 12
# B = 21
# V = 10
#
# A = 3
# B = 1
# V = 8

A,B,V = map(int,input().split())

def process(a,b,v):
    if v > a**2*b/2:
        y = 2*b - 2*v/(a**2)
        return  y/a
    elif v == a**2*b:
        return b/a
    else:
        x = 2*v / (a*b)
        return b / x




result = process(A,B,V)

print( math.degrees(math.atan(result)))