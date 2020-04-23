# N = 2
# M = 5
# ARR = [
#     [1, 'WA'],
#     [1, 'AC'],
#     [2, 'WA'],
#     [2, 'AC'],
#     [2, 'WA']
# ]
#
#
#
# N = 100000
# M = 3
# ARR = [
#     [7777, 'AC'],
#     [7777, 'AC'],
#     [7777, 'AC'],
# ]
#
#
# N = 6
# M = 0
# ARR = []

N, M = map(int, input().split())
ARR = []

for i in range(M):
    index, value = input().split()
    ARR.append([int(index), value])


def calculate(n, m, arr):
    acResult = [-1 for i in range(n)]
    waResult = [0 for i in range(n)]

    for index in range(m):
        i = arr[index][0] - 1
        if arr[index][1] == 'AC':
           if acResult[i] == -1:
               acResult[i] = index
           else:
               if acResult[i] > index:
                   acResult[i] = index

    for index in range(m):
        i = arr[index][0] - 1
        if arr[index][1] == 'WA':
            if index < acResult[i] and acResult[i] > -1:
                waResult[i] = waResult[i] + 1


    result1 = 0
    result2 = 0
    for index,ac in enumerate(acResult):
        if ac > -1:
            result1 = result1 + 1
            result2 = result2 + waResult[index]



    print(result1,result2)

calculate(N, M, ARR)
