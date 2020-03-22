N = int(input())
ARR = [int(s) for s in input().split(" ")]
# N = 8
# ARR = [1, 2, 1, 4, 2, 1, 4, 1]

def calculate(n,arr):

    dict = {}
    brr = {}
    for ar in arr:

        if dict.get(ar) == None:
            dict.__setitem__(ar,1)
        else:
            tmp = dict.get(ar)
            tmp = tmp + 1
            brr.__setitem__(ar,(tmp * (tmp - 1)) // 2 )
            dict.__setitem__(ar,tmp)

    sumValue = sum(brr.values())

    for ar in arr:
        tmp = dict.get(ar)

        print(sumValue - (tmp - 1))

calculate(N,ARR)