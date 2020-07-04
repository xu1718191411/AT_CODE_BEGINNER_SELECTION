H, W = 3, 2
ARR = [
    [1, 0],
    [2, 1],
    [1, 0]
]

H, W = map(int, input().split())
ARR = [list(map(int, input().split())) for i in range(H)]


def calculate(h, w, arr):
    ptt = []
    total = 0
    for i in range(h - 1):
        for j in range(w):
            if arr[i][j] % 2 == 1:
                arr[i][j] = arr[i][j] - 1
                arr[i + 1][j] = arr[i + 1][j] + 1
                total += 1
                ptt.append([str(i + 1), str(j + 1), str(i + 1 + 1), str(j + 1)])

    for j in range(w - 1):
        if arr[-1][j] % 2 == 1:
            arr[-1][j] = arr[-1][j] - 1
            arr[-1][j + 1] = arr[-1][j + 1] + 1
            total += 1
            ptt.append([str(h - 1 + 1), str(j + 1), str(h - 1 + 1), str(j + 1 + 1)])

    print(total)
    for pt in ptt:
        print(" ".join(pt))


calculate(H, W, ARR)
