import numpy as np

N = int(input())

ARR = []
for i in range(N):
    ARR.append(int(input()))


def calculate(n,arr):
    arr = sorted(arr)
    arr = np.array(arr)


    total = np.sum(arr)

    indexes = np.where(arr % 10 != 0)

    if total % 10 != 0:
        print(total)
        return

    if indexes[0].__len__() == 0:
        print(0)
        return


    print(total - arr[indexes[0][0]])
    return


calculate(N,ARR)