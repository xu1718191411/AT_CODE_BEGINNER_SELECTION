from sys import setrecursionlimit
setrecursionlimit(100000)
from collections import deque

S = input().split(" ")
N = int(S[0])
Q = int(S[1])

arr = []
prr = []
for i in range(N-1):
    S = input().split(" ")
    ar = [int(S[0]),int(S[1])]
    arr.append(ar)

for i in range(Q):
    S = input().split(" ")
    pr = [int(S[0]), int(S[1])]
    prr.append(pr)



def prepare(n, q, arr, prr):
    links = [[] for _ in range(n)]
    values = [0 for _ in range(n)]
    finalValues = [0 for _ in range(n)]
    for ar in arr:
        start = ar[0] - 1
        end = ar[1] - 1
        links[start].append(end)
        links[end].append(start)

    for pr in prr:
        i = pr[0] - 1
        x = pr[1]
        values[i] += x

    return links, values, finalValues


links, values, finalValues = prepare(N, Q, arr, prr)


def bfs():
    q = deque()

    q.append((0,-1,0))

    while len(q) > 0:
        currentNode,parentNode,parentAccumulate = q.popleft()
        parentAccumulate += values[currentNode]
        finalValues[currentNode] += parentAccumulate
        childNodes = links[currentNode]
        for ch in childNodes:
            if ch == parentNode:
                continue
            q.append((ch,currentNode,finalValues[currentNode]))

bfs()
print(*finalValues)