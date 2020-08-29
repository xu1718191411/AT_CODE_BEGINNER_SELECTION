from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())

gy, gx = map(int, input().split())
ARR = []

for i in range(R):
    ARR.append(input())


def calclulate(r, c, sy, sx, gy, gx, arr):
    q = deque()

    status = [[-1 for j in range(c)] for i in range(r)]

    status[sy - 1][sx - 1] = 0
    q.append((sy - 1, sx - 1))
    while len(q) > 0:
        currentY, currentX = q.popleft()

        childrens = [(currentY, currentX - 1), (currentY + 1, currentX), (currentY, currentX + 1),
                     (currentY - 1, currentX)]

        for child in childrens:
            childY, childX = child
            if (childX >= 0) and (childX < c) and (childY >= 0) and (childY < r):
                if arr[childY][childX] == ".":
                        if (status[childY][childX] == -1):
                            q.append((childY,childX))
                            cost = status[currentY][currentX]
                            status[childY][childX] = status[currentY][currentX] + 1

    print(status[gy - 1][gx - 1])


calclulate(R, C, sy, sx, gy, gx, ARR)
