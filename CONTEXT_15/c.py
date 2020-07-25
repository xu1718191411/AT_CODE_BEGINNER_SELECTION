N, K = 3, 4

ARR = [
    [1, 3, 5, 17],
    [2, 4, 2, 3],
    [1, 3, 2, 9],
]

N, K = map(int, input().split())
ARR = []

for i in range(N):
    ARR.append(list(map(int, input().split())))


def dfs(currentNode, currentLevel, arr):
    if currentLevel == (N - 1):
        if currentNode == 0:
            return True
        else:
            return False

    else:
        childNodes = arr[currentLevel + 1]
        isOk = False
        for childNode in childNodes:
            res = dfs(childNode ^ currentNode, currentLevel + 1, arr)
            if res == True:
                isOk = True
                break

        return isOk


def calculate(n, k, arr):
    isOk = False
    for i in range(k):
        res = dfs(arr[0][i], 0, arr)
        if res == True:
            isOk = True
            break
    if isOk == True:
        print("Found")
    else:
        print("Nothing")


calculate(N, K, ARR)
