from collections import deque

H, W = 10, 37
ARR = [
    ".....................................",
    "...#...####...####..###...###...###..",
    "..#.#..#...#.##....#...#.#...#.#...#.",
    "..#.#..#...#.#.....#...#.#...#.#...#.",
    ".#...#.#..##.#.....#...#.#.###.#.###.",
    ".#####.####..#.....#...#..##....##...",
    ".#...#.#...#.#.....#...#.#...#.#...#.",
    ".#...#.#...#.##....#...#.#...#.#...#.",
    ".#...#.####...####..###...###...###..",
    ".....................................",
]

H, W = map(int, input().split())
ARR = []

for i in range(H):
    ARR.append(input())


def calculate(h, w, arr):
    q = deque()

    q.append((0, 0))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    distance = [[0 for i in range(w)] for j in range(h)]
    distance[0][0] = 1
    while q.__len__() > 0:
        y, x = q.popleft()
        for i in range(4):
            my = y + dy[i]
            mx = x + dx[i]
            if (my >= 0) and (mx >= 0) and (my <= (h - 1)) and (mx <= (w - 1)) and (distance[my][mx] == 0) and (
                    arr[my][mx] == "."):
                distance[my][mx] = distance[y][x] + 1
                q.append((my, mx))

    mmk = 0
    for j in range(h):
        mmk += arr[j].count("#")

    if distance[h - 1][w - 1] == 0:
        print(-1)
    else:
        print(h * w - distance[h - 1][w - 1] - mmk)


calculate(H, W, ARR)
