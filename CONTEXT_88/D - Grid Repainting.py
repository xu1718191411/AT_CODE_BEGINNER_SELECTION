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

H, W = 4, 5
ARR = [
    ".....",
    "#....",
    ".....",
    "####.",
]


#
# H, W = map(int, input().split())
# ARR = []
#
# for i in range(H):
#     ARR.append(input())


def calculate(h, w, distance, arr):
    total = h * w
    alreadyPaiting = 0

    for s in arr:
        for ss in s:
            if ss == "#":
                alreadyPaiting += 1

    if total - alreadyPaiting < distance:
        return -1
    else:
        return total - distance - alreadyPaiting


def calculateDistance():
    q = deque()
    q.append((0, 0))

    while q.__len__() > 0:
        x, y = q.popleft()

        if x > 0:
            q.append((x - 1, y))




# def calculateDistance(h, w, x, y, arr, hist, currentStep, log):
#     q = deque()
#     currentStep = currentStep + 1
#     log.append((x, y))
#     hist[y][x] = 1
#     if x == w - 1 and (y == h - 1):
#         print(log)
#         return currentStep
#
#     # left
#     s1 = 99999999
#     if x > 0 and (hist[y][x - 1] == 0) and (arr[y][x - 1] == "."):
#         s1 = calculateDistance(h, w, x - 1, y, arr, hist, currentStep, log)
#
#     # right
#     s2 = 99999999
#     if x < w - 1 and (hist[y][x + 1] == 0) and (arr[y][x + 1] == "."):
#         s2 = calculateDistance(h, w, x + 1, y, arr, hist, currentStep, log)
#
#     # up
#     s3 = 99999999
#     if y > 0 and (hist[y - 1][x] == 0) and (arr[y - 1][x] == "."):
#         s3 = calculateDistance(h, w, x, y - 1, arr, hist, currentStep, log)
#
#     # down
#     s4 = 999999999
#     if y < h - 1 and (hist[y + 1][x] == 0) and (arr[y + 1][x] == "."):
#         s4 = calculateDistance(h, w, x, y + 1, arr, hist, currentStep, log)
#
#     return min(s1, s2, s3, s4)


hist = [[0 for j in range(W)] for i in range(H)]

log = []
distance = calculateDistance(H, W, 0, 0, ARR, hist, 0, log)

print(distance)
# if distance == 999999999:
#     print(-1)
# else:
#     result = calculate(H, W, distance, ARR)
#     print(result)
