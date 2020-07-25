# N = 5
# ng1 = 1
# ng2 = 4
# ng3 = 2

# N = 2
# ng1 = 1
# ng2 = 7
# ng3 = 15
#
N = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())


def calculate(n, ngs):
    stepsNum = [0 for i in range(n + 1)]

    if ngs.__contains__(n):
        print("NO")
        return
    for i in range(n - 1, -1, -1):
        if ngs.__contains__(i):
            stepsNum[i] = 0
            continue

        if i + 1 == n:
            stepsNum[i] = 1
            continue

        if i + 2 == n:
            stepsNum[i] = 1
            continue

        if i + 3 == n:
            stepsNum[i] = 1
            continue

        tmp = []
        if i + 1 <= n:
            if stepsNum[i + 1] > 0:
                tmp.append(stepsNum[i + 1] + 1)
        if i + 2 <= n:
            if stepsNum[i + 2] > 0:
                tmp.append(stepsNum[i + 2] + 1)

        if i + 3 <= n:
            if stepsNum[i + 3] > 0:
                tmp.append(stepsNum[i + 3] + 1)

        if len(tmp) == 0:
            stepsNum[i] = 0
        else:
            stepsNum[i] = min(tmp)

    if stepsNum[0] == 0:
        print("NO")
        return

    if stepsNum[0] <= 100:
        print("YES")
        return

    print("NO")


calculate(N, [ng1, ng2, ng3])
