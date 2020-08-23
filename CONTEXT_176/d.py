from collections import deque
#PyPy3


H, W = map(int, input().split())
C0, C1 = map(int, input().split())
D0, D1 = map(int, input().split())

LARGEST = 999999999
ARR = []

for i in range(H):
    ARR.append(input())


def calculate(h, w, c0, c1, d0, d1, arr):
    c0 = c0 - 1
    c1 = c1 - 1
    d0 = d0 - 1
    d1 = d1 - 1

    status = []
    for i in range(H):
        tmp = [LARGEST] * W
        status.append(tmp)

    q = deque()

    q.append((c0, c1, 0))

    while len(q) > 0:
        hIndex, wIndex, index = q.popleft()

        if index > status[hIndex][wIndex]:
            continue

        sss = [(hIndex, wIndex - 1), (hIndex, wIndex + 1), (hIndex - 1, wIndex), (hIndex + 1, wIndex)]

        for sH, sW in sss:
            if sH < 0 or sH >= h or sW < 0 or sW >= w:
                continue

            if arr[sH][sW] == '#':
                continue

            tmpIndex = index
            if status[sH][sW] > tmpIndex:
                status[sH][sW] = tmpIndex
                q.insert(0, (sH, sW, tmpIndex))

        for _hIndex in range(hIndex - 2, hIndex + 3):
            for _wIndex in range(wIndex - 2, wIndex + 3):
                if (_hIndex < 0) or (_hIndex >= h) or (_wIndex < 0) or (_wIndex >= w):
                    continue

                if arr[_hIndex][_wIndex] == '#':
                    continue

                tmpIndex = index + 1

                if status[_hIndex][_wIndex] > tmpIndex:
                    status[_hIndex][_wIndex] = tmpIndex
                    q.append((_hIndex, _wIndex, tmpIndex))

    if status[d0][d1] == LARGEST:
        print(-1)
    else:
        print(status[d0][d1])


calculate(H, W, C0, C1, D0, D1, ARR)
