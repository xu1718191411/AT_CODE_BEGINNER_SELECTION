s = input()
t = input()
result = 0
for i in range(len(s)):
    if s[i] != t[i]:
        result += 1


print(result)