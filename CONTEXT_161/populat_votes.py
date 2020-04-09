import numpy as np
S = input().split(" ")
N = int(S[0])
M = int(S[1])

ARR = np.array([int(s) for s in input().split(" ")])


criterion = np.sum(ARR) / (4 * M)

res = ARR >= criterion

result = np.sum(res)

if result >= M:
    print("Yes")
else:
    print("No")
