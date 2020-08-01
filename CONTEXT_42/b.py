# N, L = 3, 3
# SRR = [
#     "dxx",
#     "axx",
#     "cxx"
# ]

N, L = map(int,input().split())
SRR = []

for i in range(N):
    SRR.append(input())


srr2 = sorted(SRR)


result = "".join(srr2)

print(result)


