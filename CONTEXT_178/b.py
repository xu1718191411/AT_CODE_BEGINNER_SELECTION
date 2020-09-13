a, b, c, d = map(int, input().split())
result = []

# a * c

result.append(a * c)
result.append(a * d)
result.append(b * c)
result.append(b * d)

print(max(result))
