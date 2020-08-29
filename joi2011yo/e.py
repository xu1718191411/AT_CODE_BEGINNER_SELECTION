from collections import deque

H, W, N = map(int, input().split())

ARR = []

for i in range(H):
    ARR.append(input())


def calclulate(h, w, n, arr):
    startX, startY = 0, 0

    cheeseHard = [None for i in range(n)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "S":
                startY = i
                startX = j
            elif arr[i][j].isnumeric():
                cheeseHard[int(arr[i][j]) - 1] = (i, j)

    cost = 0
    for i in range(len(cheeseHard)):
        endY, endX = cheeseHard[i]
        cost += calculateDistance(h, w, startX, startY, endX, endY, arr)
        startY,startX = endY,endX

    print(cost)


def calculateDistance(h, w, startX, startY, endX, endY, arr):
    status = [[0 for j in range(w)] for i in range(h)]

    q = deque()
    q.append((startY, startX))
    while len(q) > 0:
        currentY, currentX = q.popleft()

        children = [(currentY, currentX - 1), (currentY + 1, currentX), (currentY, currentX + 1),
                    (currentY - 1, currentX)]

        if (currentY == endY) and (currentX == endX):
            return status[currentY][currentX]

        cost = status[currentY][currentX]
        for child in children:
            childY, childX = child

            if childX >= 0 and childX < w and childY >= 0 and childY < h:
                if arr[childY][childX] != "X":
                    if status[childY][childX] == 0:
                        q.append((childY, childX))
                        status[childY][childX] = cost + 1

    return status[endY][endX]


calclulate(H, W, N, ARR)
