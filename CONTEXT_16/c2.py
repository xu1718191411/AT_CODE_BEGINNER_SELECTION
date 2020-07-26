N, M = 3, 2
ARR = [
    [1, 2],
    [2, 3]
]

N, M = map(int,input().split())
ARR = []

for i in range(M):
    ARR.append(list(map(int,input().split())))


def calculate(n, m, arr):

    childNodes = [set() for i in range(n)]

    for i in range(m):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1

        tmp = childNodes[startNode]
        tmp.add(endNode)

        childNodes[startNode] = tmp

        tmp2 = childNodes[endNode]
        tmp2.add(startNode)

        childNodes[endNode] = tmp2


    result = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if childNodes[i].__contains__(j):
                continue

            if childNodes[j].__contains__(i):
                continue


            s1 = childNodes[i]
            s2 = childNodes[j]

            if len(s1 & s2) > 0:
                tmp = result[i]
                result[i] = tmp + 1

    for res in result:
        print(res)

calculate(N, M, ARR)
