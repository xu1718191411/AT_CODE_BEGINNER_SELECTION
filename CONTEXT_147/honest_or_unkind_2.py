from collections import deque

#
# N = 3
# ARR = [[[2],[3]], [[3],[1]], [[1],[2]]]

# N = 3
# ARR = [[[2],[]],[[1],[]],[[],[2]]]


# N = 2
# ARR = [[[], [2]], [[], [1]]]

N = int(input())
ARR = []

for i in range(N):
    A = int(input())
    X = []
    Y = []
    for j in range(A):
        x, t = map(int, input().split())
        if t == 1:
            X.append(x)
        else:
            Y.append(x)
    ARR.append([X,Y])

def calculate(n, arr):
    result = []
    for i in range(2 ** n):
        q = deque()
        possibilities = []
        teacherGoods = set()
        teacherBads = set()
        for j in range(n):
            identity = (i >> j & 1) == 1
            if identity:
                q.append(j)
                possibilities.append(identity)
                teacherGoods.add(j + 1)
            else:
                teacherBads.add(j + 1)
            # j 第几号人
            # i >> j & 1 第几号人是好人还是坏人
        res = judge(q, arr, teacherGoods, teacherBads)
        if res == True:
            result.append(sum(possibilities))

    print(max(result))


def judge(possibilities, arr, teacherGoods, teacherBads):
    goodMans = set()
    badMans = set()
    trueStatus = {}
    result = True
    while len(possibilities) > 0:

        trueIndex = possibilities.popleft()
        if trueStatus.get(trueIndex) == True:
            continue
        trueStatus.__setitem__(trueIndex, True)
        for g in arr[trueIndex][0]:
            goodMans.add(g)
            possibilities.append(g - 1)
        for b in arr[trueIndex][1]:
            badMans.add(b)

        if len(list(goodMans & teacherBads)) > 0:
            result = False
            break

        if len(list(badMans & teacherGoods)) > 0:
            result = False
            break
    return result


calculate(N, ARR)
