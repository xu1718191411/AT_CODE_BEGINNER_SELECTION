N = int(input())

sum = 0
for i in range(1,N+1):
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        sum = sum + i

print(sum)