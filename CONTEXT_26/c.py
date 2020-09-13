N = int(input())
BRR = []

for i in range(N-1):
    BRR.append(int(input()))


import sys
import math

sys.setrecursionlimit(1000000)

def calculate(n, brr):
    links = [[] for i in range(n)]

    for i in range(len(brr)):
        if (i+1) == (brr[i] - 1):
            continue
        links[brr[i] - 1].append(i+1)

    result = dfs(0, links)
    print(result)


def dfs(currentIndex, links):
    if len(links[currentIndex]) == 0:
        return 1

    maxValue = -math.inf
    minValue = math.inf
    childrens = links[currentIndex]

    for child in childrens:
        value = dfs(child,links)
        maxValue = max(maxValue, value)
        minValue = min(minValue, value)


    return minValue + maxValue + 1



calculate(N, BRR)
