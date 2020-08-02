A,B,C = map(int,input().split())

s1 = (A * B) % (1000000000 + 7)
s2 = (s1 * C) % (1000000000 + 7)

print(s2)