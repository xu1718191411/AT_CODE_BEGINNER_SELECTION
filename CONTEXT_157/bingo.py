ARR = [
    [84, 97, 66],
    [79, 89, 11],
    [61, 59, 7],
]


N = 7
BRR = [
    89,
    7,
    87,
    79,
    24,
    84,
    30,
]


ARR = []

for i in range(3):
    ARR.append(list(map(int,input().split())))

N = int(input())

BRR = []

for i in range(N):
    BRR.append(int(input()))


def calculagte(arr, n, brr):
    status = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]

    for h in range(3):
        for w in range(3):
            for i in range(n):
                if arr[h][w] == brr[i]:
                    status[h][w] = True

    isOk = False

    if status[0][0] and status[0][1] and status[0][2]:
        isOk = True

    if status[1][0] and status[1][1] and status[1][2]:
        isOk = True

    if status[2][0] and status[2][1] and status[2][2]:
        isOk = True


    if status[0][0] and status[1][0] and status[2][0]:
        isOk = True

    if status[0][1] and status[1][1] and status[2][1]:
        isOk = True

    if status[0][2] and status[1][2] and status[2][2]:
        isOk = True

    if status[0][0] and status[1][1] and status[2][2]:
        isOk = True

    if status[2][0] and status[1][1] and status[0][2]:
        isOk  = True

    if isOk:
        print("Yes")
    else:
        print("No")

calculagte(ARR, N, BRR)
