from collections import deque

N, M = map(int, input().split())

ARR = []

for i in range(M):
    ARR.append(list(map(int, input().split())))

def prepare(n, m, arr):
    childNodes = [[] for i in range(n)]
    for i in range(m):
        start = arr[i][0] - 1
        end = arr[i][1] - 1
        distance = arr[i][2]

        childNodes[start].append((end, distance))
        childNodes[end].append((start, distance))

    return childNodes


def calculate(n, m, arr):

    childNodes = prepare(n, m, arr)
    result = []

    for i in range(N):
        result.append(calculateDistance(n, i, childNodes))

    print(min(result))


def calculateDistance(n, startX, childNodes):
    status = [-1 for i in range(n)]
    status[startX] = 0

    q = deque()

    q.append(startX)

    while len(q) > 0:
        currentNode = q.popleft()

        children = childNodes[currentNode]

        for child in children:
            nextNode, distance = child
            if status[nextNode] == -1:
                status[nextNode] = status[currentNode] + distance
                q.append(nextNode)
            else:
                if status[nextNode] > (status[currentNode] + distance):
                    status[nextNode] = (status[currentNode] + distance)
                    q.append(nextNode)

    return max(status)


calculate(N, M, ARR)
