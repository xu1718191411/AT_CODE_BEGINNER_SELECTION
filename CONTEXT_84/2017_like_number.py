import math
def sushu(n):
    arr = []
    for i in range(2, n + 1):
        arr.append(i)

    limit = int(math.sqrt(n)) + 1

    prev = []
    while True:
        start = arr[0]
        prev.append(start)
        if start > limit:
            break
        brr = []
        for i in arr:
            if i % start != 0:
                brr.append(i)
        arr = brr

    prev.extend(arr)
    return prev


n = 100000
shushu = sushu(100000)

marks = []
for i in range(n + 1):
    marks.append(False)

for j in shushu:
    marks[j] = True


marks2 = []
result = []
for i in range(n + 1):
    if i % 2 == 0:
        marks2.append(False)
        if i == 0:
            result.append(0)
        else:
            result.append(result[i - 1])
    else:
        if marks[(i + 1) // 2] and marks[i]:
            marks2.append(True)
            result.append(result[i-1] + 1)
        else:
            marks2.append(False)
            result.append(result[i - 1])

Q = 4
ARR = [
    [13, 13],
    [7, 11],
    [7, 11],
    [2017, 2017]
]

Q = 6
ARR = [
    [1, 53],
    [13, 91],
    [37, 55],
    [19, 51],
    [73, 91],
    [13, 49]
]


Q = int(input())

ARR = []

for i in range(Q):
    ARR.append(list(map(int,input().split())))


for i in range(Q):
    start = ARR[i][0]
    end = ARR[i][1]
    print(result[end] - result[start - 1])



