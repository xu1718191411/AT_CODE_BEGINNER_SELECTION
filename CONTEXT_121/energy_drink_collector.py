S = input().split(" ")
N = int(S[0])
M = int(S[1])

arr = []
for i in range(N):
    Q = input().split(" ")
    arr.append([int(q)for q in Q])

arr.sort(key=lambda s: s[0])

count = 0
total = 0
for a in arr:
    if count + a[1] <= M:
        total += a[0] * a[1]
        count += a[1]
    else:
        total += a[0] * (M - count)
        count += (M - count)
        break

print(total)
