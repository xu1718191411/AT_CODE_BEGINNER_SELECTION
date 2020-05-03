A,B,N = map(int,input().split())

x = min(B-1,N)
result = (A * x) // B - A * (x // B)
print(result)