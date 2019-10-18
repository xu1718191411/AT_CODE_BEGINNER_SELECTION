a,b,c,x = map(int,[input() for i in range(4)])

count = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            amount = i * 500 + j * 100 + k * 50
            if amount == x:
                count += 1

print(count)
