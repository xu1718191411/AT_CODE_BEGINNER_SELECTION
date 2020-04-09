from collections import deque

# K = int(input())
K = 15
n = 1
s = 9 * 2 ** (n - 1)
while s < K:
    n = n + 1
    s = 9 * 2 ** (n - 1)

result = []


def bianli(maxLevel):
    q = deque()

    q.append(["", 1])

    result = []

    while q.__len__() > 0:
        x = q.popleft()

        result.append("{}{}".format(x[0], x[1]))

        if len(x[0]) == maxLevel:
            break

        if x[-1] == 0:
            q.append(["{}{}".format(x[0], 1), 1])
        elif x[-1] == 9:
            q.append(["{}{}".format(x[0], 8), 8])
        else:
            q.append(["{}{}".format(x[0], x[-1] - 1), x[-1] - 1])
            q.append(["{}{}".format(x[0], x[-1] + 1), x[-1] + 1])
    print(result)


bianli(3)
