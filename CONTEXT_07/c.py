from collections import deque

R, C = 7, 8
sy, sx = 2, 2
gy, gx = 4, 5

ARR = [
    "########",
    "#......#",
    "#.######",
    "#..#...#",
    "#..##..#",
    "##.....#",
    "########"
]

#
# R,C = 5, 8
# sy,sx = 2, 2
# gy,gx = 2, 4
# ARR = [
#     "########",
#     "#.#....#",
#     "#.###..#",
#     "#......#",
#     "########"
# ]


R, C = map(int, input().split())
sy, sx = map(int, input().split())

gy, gx = map(int, input().split())
ARR = []

for i in range(R):
    ARR.append(input())


def calclulate(r, c, sy, sx, gy, gx, arr):
    q = deque()

    status = [[0 for j in range(c)] for i in range(r)]
    q.append((sx - 1, sy - 1, 0))

    while len(q) > 0:
        currentX, currentY, cost = q.popleft()

        childrens = []
        childrens.append((currentX - 1, currentY))
        childrens.append((currentX, currentY - 1))
        childrens.append((currentX + 1, currentY))
        childrens.append((currentX, currentY + 1))

        for child in childrens:
            childX, childY = child

            if (childX >= 0) and (childX < c) and (childY >= 0) and (childY < r):
                if (arr[childY][childX] == "."):
                    if (status[childY][childX] == 0):
                        q.append((childX, childY, cost + 1))
                        status[childY][childX] = cost + 1
                    else:
                        if status[childY][childX] > (cost + 1):
                            q.append((childX, childY, cost + 1))
                            status[childY][childX] = cost + 1

    print(status[gy - 1][gx - 1])


calclulate(R, C, sy, sx, gy, gx, ARR)
