import sys
sys.setrecursionlimit(20000000)
S = input().split(" ")
n = int(S[0])
m = int(S[1])

py = []

for i in range(m):
    py.append([int(s) for s in input().split(" ")])

def prepare(n, data):
    result = [0 for i in range(n)]
    dict = {}
    data = sorted(data,key=lambda x:x[1])
    for d in data:
        i = d[0] - 1
        result[i] = result[i] + 1
        dict.__setitem__(generateID(d[0], d[1]), str(d[0]).zfill(6) + str(result[i]).zfill(6))

    return dict


def generateID(start, to):
    if start < to:
        start, to = to, start

    return start * 100000 + to

dict = prepare(n, py)

for p in py:
    print(dict[generateID(p[0],p[1])])


