import math

def process(a,b,x):
    S =  (a * b) / 2
    if x > S:
        m = ((2 * x) / a**2) - b
        return (b - m) / a
        return
    elif x < S:
        m = (2 * x) / (a*b)
        return b / m
        pass
    else:
        return b/a


arr = input().split(' ')

A = int(arr[0])
B = int(arr[1])
X = int(arr[2])

result = process(A,B,X)

print(math.degrees(math.atan(result)))