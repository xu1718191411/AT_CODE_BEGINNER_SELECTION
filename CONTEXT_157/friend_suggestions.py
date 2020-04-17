from collections import deque

# N = 4
# M = 4
# K = 1
# ARR = [
#     [2, 1],
#     [1, 3],
#     [3, 2],
#     [3, 4]
# ]
#
# BRR = [
#     [4, 1]
# ]


# N = 5
# M = 10
# K = 0
# ARR = [
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [1, 5],
#     [3, 2],
#     [2, 4],
#     [2, 5],
#     [4, 3],
#     [5, 3],
#     [4, 5]
# ]

# N = 10
# M = 9
# K = 3
# ARR = [
#     [10, 1],
#     [6, 7],
#     [8, 2],
#     [2, 5],
#     [8, 4],
#     [7, 3],
#     [10, 9],
#     [6, 4],
#     [5, 8],
# ]
#
# BRR = [
#     [2,6],
#     [7,5],
#     [3,1]
# ]

S = input().split(" ")
N = int(S[0])
M = int(S[1])
K = int(S[2])
ARR = []
BRR = []
for i in range(M):
    ARR.append([int(s) for s in input().split(" ")])

for i in range(K):
    BRR.append([int(s) for s in input().split(" ")])


def prepare(n, arr):
    nodes = [[] for i in range(n)]
    nodeStates = [False for i in range(n)]
    nodeLabels = [0 for i in range(n)]
    for ar in arr:
        fromNode = ar[0] - 1
        toNode = ar[1] - 1
        nodes[fromNode].append(toNode)
        nodes[toNode].append(fromNode)

    return nodes, nodeStates, nodeLabels

def prepare2(n,brr):
    nodes = [[] for i in range(n)]
    for ar in brr:
        fromNode = ar[0] - 1
        toNode = ar[1] - 1
        nodes[fromNode].append(toNode)
        nodes[toNode].append(fromNode)

    return nodes


def calculate(n, m, k, nodes, nodeStates, nodeLabels):
    q = deque()

    label = 0
    labelDict = {}
    while nodeStates.count(False) > 0:

        falseIndex = nodeStates.index(False)

        q.append(falseIndex)

        while len(q) > 0:
            node = q.popleft()
            if nodeStates[node] == True:
                continue
            nodeStates[node] = True
            nodeLabels[node] = label
            childNodes = nodes[node]
            if labelDict.get(label) == None:
                labelDict.__setitem__(label,1)
            else:
                labelDict.__setitem__(label,labelDict.get(label)+1)

            for childNode in childNodes:
                if nodeStates[childNode] == False:
                    q.append(childNode)
        label = label + 1


    result = []
    for i in range(n):
        l = nodeLabels[i]
        s = 0

        for blockNode in blockNodes[i]:
            if nodeLabels[blockNode] == l:
                s = s + 1
        result.append(str(labelDict[l] - len(nodes[i]) - 1 - s))

    print(" ".join(result))


nodes, nodeStates, nodeLabels = prepare(N, ARR)
blockNodes = prepare2(N,BRR)
calculate(N, M, K, nodes, nodeStates, nodeLabels)
