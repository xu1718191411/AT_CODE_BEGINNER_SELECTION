n = int(input())
arr = []
for i in range(n-1):
    arr.append([int(s) for s in input().split(" ")])

childNodeNums = [0 for i in range(n)]
childNodeStatus = [-1 for i in range(n)]
nodeLines = [0 for i in range(n - 1)]


def prepare(n, arr):
    s = [[] for i in range(n)]
    for ar in arr:
        s[ar[0] - 1].append(ar[1] - 1)
        s[ar[1] - 1].append(ar[0] - 1)
    return s


# x为记录入边的颜色
def dfs(currentNode, arr, x):
    m1 = childNodeNums
    m2 = childNodeStatus
    childNodes = arr[currentNode]
    if len(childNodes) == 0:
        return

    childNodeNums[currentNode] = childNodeNums[currentNode] + len(arr[currentNode])
    childNodeStatus[currentNode] = 1

    kk = 0
    for i, childNodeIndex in enumerate(childNodes):

        if childNodeStatus[childNodeIndex] == -1:
            kk = kk + 1
            if x == kk:
                kk = kk + 1
            appendIntoNode(currentNode+1,childNodeIndex+1,kk)
            dfs(childNodeIndex, arr, kk)


def appendIntoNode(currentNode,childNode,value):
    for i,v in enumerate(arr):
        if (v[0] == currentNode and v[1] == childNode):
            nodeLines[i] = value


data = prepare(n, arr)
dfs(0, data, -1)

print(max(childNodeNums))

for ar in nodeLines:
    print(ar)
