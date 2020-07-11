# N = 10
# ARR = [3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
#
# # N = 6
# # ARR = [3, 1, 2, 4, 2, 1]
#
# # N = 4
# # ARR = [1, 2, 3, 4]

N = int(input())
ARR = [int(s) for s in input().split(" ")]


def calculate(n, arr):

    dict = {}

    for ar in arr:
        if dict.get(ar) == None:
            dict.__setitem__(ar, 1)
        else:
            dict.__setitem__(ar, dict.get(ar) + 1)

    dict2 = {changedu: geshu for changedu, geshu in dict.items() if geshu >= 2}

    dict3 = sorted(dict2.items(), key=lambda x: -x[0])


    if len(dict3) == 0:
        print(0)
    elif len(dict3) == 1:
        print(1)
        if dict3[0][1] >= 4:
            print(dict3[0][0]**2)
        else:
            print(0)
    else:
        if dict3[0][1] >= 4:
            print(dict3[0][0]**2)
        else:
            print(dict3[0][0] * dict3[1][0])


calculate(N, ARR)
