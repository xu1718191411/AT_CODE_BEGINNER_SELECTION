N = int(input())

ARR = []
for i in range(N):
    ARR.append([int(s) for s in input().split(" ")])

CRR = []
for i in range(N):
    CRR.append([int(s) for s in input().split(" ")])


def calculate(n, arr, crr):

    reds = sorted(arr,key=lambda x:-x[1])
    blues = sorted(crr,key=lambda x:x[0])
    counts = 0

    for i,bl in enumerate(blues):
        for j,rd in enumerate(reds):

            if (rd[0] < bl[0]) and (rd[1] < bl[1]):
                counts = counts + 1
                reds[j][1] = 1000
                reds[j][0] = 1000
                break
    print(counts)

calculate(N, ARR, CRR)
