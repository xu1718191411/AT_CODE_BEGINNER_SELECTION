import fractions

A, B = map(int, input().split())

res = fractions.gcd(A, B)

print(int(A*B / res))