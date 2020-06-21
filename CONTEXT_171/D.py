N = 4
ARR = [1, 1, 1, 1]
Q = 3
SRR = [
    [1, 2],
    [2, 1],
    [3, 5]
]

N = 4
ARR = [1, 2, 3, 4]
Q = 3
SRR = [
    [1, 2],
    [3, 4],
    [2, 4],
]


#
# N = 2
# ARR = [1, 2]
# Q = 3
# SRR = [
#     [1, 100],
#     [2, 100],
#     [100, 1000]
# ]

N = int(input())
ARR = list(map(int,input().split()))
Q = int(input())
SRR = []

for i in range(Q):
    SRR.append(list(map(int,input().split())))


def calculate(n, arr, q, srr):
    dict = {}
    sumValue = sum(arr)
    for i in range(n):
        value = arr[i]
        if dict.get(value) == None:
            dict.__setitem__(value, 1)
        else:
            dict.__setitem__(value, dict.get(value) + 1)

    for i in range(q):
        fromValue = srr[i][0]
        toValue = srr[i][1]

        if dict.get(fromValue) == None:
            print(sumValue)
        else:
            fromNum = dict.get(fromValue)
            dict.__setitem__(fromValue, 0)
            sumValue += fromNum * (toValue - fromValue)
            if dict.get(toValue) == None:
                dict.__setitem__(toValue, fromNum)
            else:
                dict.__setitem__(toValue, dict.get(toValue) + fromNum)
            print(sumValue)


calculate(N, ARR, Q, SRR)
