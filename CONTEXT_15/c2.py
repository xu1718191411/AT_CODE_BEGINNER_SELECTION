import itertools

ARR = [
    [1, 3, 5, 17],
    [2, 4, 2, 3],
    [1, 3, 2, 9],
]


N, K = map(int, input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int, input().split())))


def calclulate(arr):
    iters = list(itertools.product(*arr))
    for item in iters:
        isOK = False
        res = item[0]
        for index, value in enumerate(item):
            if index == 0:
                continue

            res = res ^ value

        if res == 0:
            isOK = True
            break

    if isOK == True:
        print("Found")
    else:
        print("Nothing")

calclulate(ARR)
