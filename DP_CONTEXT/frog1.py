# N = 4
# HRR = [10, 30, 40, 20]
# N = 2
# HRR = [10, 10]

N = int(input())
HRR = list(map(int,input().split()))
result = []
for i in range(N):
    if i == 0:
        result.append(0)
    elif i == 1:
        s1 = result[i - 1] + abs(HRR[i] - HRR[i - 1])
        result.append(s1)
    else:
        s1 = result[i - 1] + abs(HRR[i] - HRR[i - 1])
        s2 = result[i - 2] + abs(HRR[i] - HRR[i - 2])
        result.append(min(s1, s2))

print(result[-1])
