# N, K = 4, 5
# ARR = [3, 2, 4, 1]

# N, K = 6, 727202214173249351
# ARR = [6, 5, 2, 5, 3, 2]

import sys
sys.setrecursionlimit(100000000)

N,K = map(int,input().split())
ARR = list(map(int,input().split()))
NodeStatus = [False] * N
NodeFirstSteps = [0] * N
L = 0
STARTLINDEX = 0
OrderARR = []


def dfs(pos, arr, step):
    if NodeStatus[pos] == True:
        L = (step - NodeFirstSteps[pos])
        STARTLINDEX = NodeFirstSteps[pos]
        print(OrderARR[(K - STARTLINDEX) % L + STARTLINDEX] + 1)
        return

    if step == K:
        print(pos+1)
        return

    OrderARR.append(pos)
    NodeStatus[pos] = True
    NodeFirstSteps[pos] = step
    dfs(arr[pos] - 1, arr, step + 1)


dfs(0, ARR, 0)
