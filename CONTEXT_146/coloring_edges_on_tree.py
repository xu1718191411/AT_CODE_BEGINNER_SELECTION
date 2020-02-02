n = 8
arr = [
    [1, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [4, 7],
    [5, 6],
    [6, 8]
]

childNodeNums = [0 for i in range(n)]
childNodeStatus = [-1 for i in range(n)]
lineColors = [0 for i in range(n-1)]

def prepare(n, arr):
    s = [[] for i in range(n)]
    for ar in arr:
        s[ar[0]-1].append(ar[1] - 1)
        s[ar[1]-1].append(ar[0] - 1)
    return s

def dfs(currentNode,arr):
    childNodes = arr[currentNode]
    if len(childNodes) == 0:
        return

    childNodeNums[currentNode] = childNodeNums[currentNode] + len(arr[currentNode])

    childNodeStatus[currentNode] = 1

    for childNodeIndex in childNodes:
        if childNodeStatus[childNodeIndex] == -1:
            dfs(childNodeIndex, arr)

def order(root,num,data):
    print(1)

data = prepare(n, arr)
dfs(3,data)

print(childNodeNums)