N = input()

res = False
for s in N:
    if s == '7':
        res = True
        break

if res:
    print('Yes')
else:
    print('No')