import math
N, X, T = map(int, input().split())

res = math.ceil(N / X) * T

print(res)