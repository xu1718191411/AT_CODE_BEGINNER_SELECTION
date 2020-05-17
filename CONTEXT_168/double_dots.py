N, M = 6, 9
ARR = [
    [3, 4],
    [6, 1],
    [2, 4],
    [5, 3],
    [4, 6],
    [1, 5],
    [6, 2],
    [4, 5],
    [5, 6],
]

N, M = 4, 4
ARR = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 2],
]

N, M = map(int, input().split())
ARR = []

for i in range(M):
    ARR.append(list(map(int, input().split())))

from collections import deque


def prepare(n, m, arr):
    nodes = [[] for i in range(n)]
    nodeStates = [-1 for i in range(n)]
    prevs = [-1 for i in range(n)]
    for i in range(m):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1

        nodes[startNode].append(endNode)
        nodes[endNode].append(startNode)

    return nodes, nodeStates, prevs


nodes, nodeStates, prevs = prepare(N, M, ARR)


def bfs(nodes, nodeStates, prevs, n):
    q = deque()
    q.append({'prev': -1, 'to': 0})
    while len(q) > 0:
        first = q.popleft()
        currentNode = first['to']
        previousNode = first['prev']
        if nodeStates[currentNode] != -1:
            continue
        prevs[currentNode] = previousNode
        childNodes = nodes[currentNode]
        nodeStates[currentNode] = 1
        for childNode in childNodes:
            q.append({'prev': currentNode, 'to': childNode})

    print("Yes")
    for i in range(1, n):
        print(prevs[i] + 1)


bfs(nodes, nodeStates, prevs, N)
