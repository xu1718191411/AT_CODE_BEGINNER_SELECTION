from bisect import bisect_right
import numpy as np
def calculate(arr,sArr):


    for s in range(len(sArr)):
        arr = np.sort(arr, axis=0)

        k = bisect_right(arr,sArr[s][1])

        if k >= sArr[s][0]:
            arr[:sArr[s][0]] = sArr[s][1]
        else:
            arr[:k] = sArr[s][1]

    return arr


S = input()

N = int(S.split(" ")[0])
M = int(S.split(" ")[1])

arr = [int(s) for s in input().split(" ")]
arr = np.array(arr)


arr2 = []
for i in range(M):
    tmp = [int(s) for s in input().split(" ")]
    arr2.append(tmp)

arr2 = np.array(arr2)




result = calculate(arr,arr2)

print(np.sum(result))