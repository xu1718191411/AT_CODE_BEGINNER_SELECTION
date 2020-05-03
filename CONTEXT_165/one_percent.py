import math
base = 100
X = int(input())
n = 0
while base < X:
    n = n + 1
    base = math.floor(base*1.01)

print(n)
