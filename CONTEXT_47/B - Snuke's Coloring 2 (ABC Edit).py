# W, H, N = 10, 10, 5
# ARR = [
#     [1, 6, 1],
#     [4, 1, 3],
#     [6, 9, 4],
#     [9, 4, 2],
#     [3, 1, 3]
# ]

# W, H, N = 5, 4, 2
# ARR = [
#     [2, 1, 1],
#     [3, 3, 4],
# ]


#
W, H, N = map(int, input().split())
ARR = []
for i in range(N):
    ARR.append(list(map(int, input().split())))


def calculate(w, h, n, arr):
    minX = 0
    minY = 0
    maxX = w
    maxY = h

    for i in range(n):
        x = arr[i][0]
        y = arr[i][1]
        type = arr[i][2]

        if type == 1:
            minX = max(minX, x)
            continue

        if type == 2:
            maxX = min(maxX, x)
            continue

        if type == 3:
            minY = max(minY, y)
            continue

        if type == 4:
            maxY = min(maxY, y)
            continue

    s1 = max(0, maxX - minX)
    s2 = max(0, maxY - minY)

    print(s1 * s2)


calculate(W, H, N, ARR)
