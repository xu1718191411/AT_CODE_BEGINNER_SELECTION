from collections import deque

# N, W = 3, 5
# ARR = [
#     ['.', '.', '.', '#', '.'],
#     ['.', '#', '.', '#', '.'],
#     ['.', '#', '.', '.', '.']
# ]

N, W, = 3, 3
ARR = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]

N, W = map(int, input().split())

ARR = []

for i in range(N):
    ARR.append(list(map(str, input())))


def dfs(start, n, w, arr):
    d = deque()
    d.append(start)

    states = [[0 for j in range(w)] for i in range(n)]

    maxDistance = start[2]
    while len(d) > 0:
        coordinate = d.popleft()
        coorY = coordinate[0]
        coorX = coordinate[1]
        distance = coordinate[2]
        if states[coorY][coorX] == 1:
            continue
        maxDistance = max(distance, maxDistance)

        states[coorY][coorX] = 1
        leftX, leftY = coorX - 1, coorY
        rightX, rightY = coorX + 1, coorY
        topX, topY = coorX, coorY - 1
        bottomX, bottomY = coorX, coorY + 1

        if leftX >= 0 and leftY >= 0:
            if arr[leftY][leftX] == ".":
                d.append([leftY, leftX, distance + 1])

        if rightX <= w - 1 and rightY <= n - 1:
            if arr[rightY][rightX] == ".":
                d.append([rightY, rightX, distance + 1])

        if topY >= 0:
            if arr[topY][topX] == ".":
                d.append([topY, topX, distance + 1])

        if bottomY <= n - 1:
            if arr[bottomY][bottomX] == ".":
                d.append([bottomY, bottomX, distance + 1])

    return maxDistance


def calculate(n, w, arr):
    distances = []

    for i in range(n):
        for j in range(w):
            if arr[i][j] == ".":
                distance = dfs([i, j, 0], n, w, arr)
                distances.append(distance)

    maxDistance = max(distances)
    print(maxDistance)


# dfs([0, 0, 0], N, W, ARR)

calculate(N, W, ARR)
