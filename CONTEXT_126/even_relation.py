import sys
sys.setrecursionlimit(20000000)
def prepare(n,arr):
    nodeArr = [[] for i in range(n)]
    for ar in arr:
        nodeArr[ar[0]-1].append([ar[1]-1,ar[2]])
        nodeArr[ar[1]-1].append([ar[0]-1,ar[2]])
    return nodeArr

def dfs(currentNode,distance):
    res[currentNode] = distance
    for next in nodeArr[currentNode]:
        nextNode = next[0]
        nextNodeDistance = next[1]
        if res[nextNode] == -1:
            dfs(nextNode,distance + nextNodeDistance)




n = int(input())

arr = []

for i in range(n-1):
    arr.append([int(s) for s in input().split(" ")])

nodeArr = prepare(n, arr)


if n == 1:
    print(1)
else:
    res = [-1 for i in range(n)]

    dfs(0,0)

    result = [(re % 2) for re in res]

    for re in res:
        print(re % 2)

