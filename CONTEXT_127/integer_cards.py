# N, M = 10, 3
# ARR = [1, 8, 5, 7, 100, 4, 52, 33, 13, 5]
# BRR = [
#     [3, 10],
#     [4, 30],
#     [1, 4]
# ]


N,M = map(int,input().split())
ARR = list(map(int,input().split()))
BRR = []
for i in range(M):
    BRR.append(list(map(int,input().split())))

def calculate(n, m, arr, brr):
    raw = []
    for ar in arr:
        raw.append([ar, 1])
    for br in brr:
        raw.append([br[1], br[0]])

    raw = sorted(raw,key=lambda x:-x[0])
    # print(raw)

    offset = 0
    sum = 0
    for ra in raw:
        if offset + ra[1] <= n:
            sum = sum + ra[1] * ra[0]
            offset = offset + ra[1]
        else:
            sum = sum + (n - offset) * ra[0]
            offset = n
            break
    print(sum)

calculate(N, M, ARR, BRR)
