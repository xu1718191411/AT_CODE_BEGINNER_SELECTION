def prepare(n,arr):
    nodeArr = [[] for i in range(n)]
    for ar in arr:
        nodeArr[ar[0]-1].append([ar[1]-1,ar[2]])
        nodeArr[ar[1]-1].append([ar[0]-1,ar[2]])
    return nodeArr

def dfs(parent,currentNode,distance):

    if len(nodeArr[currentNode]) == 1:
        if currentNode != 0:
            # 末点
            res[currentNode] = distance
            return

    for next in nodeArr[currentNode]:
        nextNode = next[0]
        nextNodeDistance = next[1]
        if nextNode != parent:
            dfs(currentNode,nextNode,distance + nextNodeDistance)
    res[currentNode] = distance


n = int(input())

arr = []

for i in range(n-1):
    arr.append([int(s) for s in input().split(" ")])

nodeArr = prepare(n, arr)


if n == 1:
    print(1)
else:
    res = [-1 for i in range(n)]

    dfs(-1,0,0)

    result = [(re % 2) for re in res]

    for re in res:
        print(re % 2)

