

S = input()
N = int(S.split(" ")[0])
M = int(S.split(" ")[1])


lArr = []
rArr = []
for i in range(M):
    S = input()
    l1 = int(S.split(" ")[0])
    r1 = int(S.split(" ")[1])
    lArr.append(l1)
    rArr.append(r1)

lArr.sort()
rArr.sort()

l1 = max(lArr)
r1 = min(rArr)

if r1 < l1:
    print(0)
else:
    print(r1 - l1 + 1)
