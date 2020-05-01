import math
# N, A, B, C = 7, 100, 90, 80
# ARR = [
#     98,
#     40,
#     30,
#     21,
#     80,
#     25,
#     100
# ]

N, A, B, C = map(int, input().split())
ARR = []
for i in range(N):
    ARR.append(int(input()))
result = []


def dfs(deep, crr):
    if deep == N:
        ok, res = calculate(crr)
        if ok:
            result.append(int(res))
    else:
        for i in range(4):
            crr[deep] = i
            dfs(deep + 1, crr)


def calculate(crr):
    sA = []
    sB = []
    sC = []
    sN = []
    for index, cr in enumerate(crr):
        if cr == 0:
            sN.append(ARR[index])
        if cr == 1:
            sA.append(ARR[index])
        if cr == 2:
            sB.append(ARR[index])
        if cr == 3:
            sC.append(ARR[index])

    if len(sA) == 0:
        return False, -1
    if len(sB) == 0:
        return False, -1
    if len(sC) == 0:
        return False, -1


    s1 = (len(sA) - 1) * 10 + math.fabs(sum(sA) - A)
    s2 = (len(sB) - 1) * 10 + math.fabs(sum(sB) - B)
    s3 = (len(sC) - 1) * 10 + math.fabs(sum(sC) - C)

    return True, s1 + s2 + s3


dfs(0, [0 for i in range(N)])

print(min(result))