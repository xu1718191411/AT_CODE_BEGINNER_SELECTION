N = 3
ARR = [
    [2, 0],
    [3, 1],
    [1, 3],
]

CRR = [
    [4, 2],
    [0, 4],
    [5, 5]
]


def calculate(n, arr, crr):

    blue = {}
    red = {}


    for index,value in enumerate(arr):
        if red.get(value[1]) == None:
            red.__setitem__(value[1],[value[0]])
        else:
            tmp = red.get(value[1])
            tmp.append(value[0])
            tmp = sorted(tmp,key=lambda x:-x)
            red.__setitem__(value[1],tmp)

    for index, value in enumerate(crr):
        if blue.get(value[0]) == None:
            blue.__setitem__(value[0], [value[1]])
        else:
            tmp = blue.get(value[0])
            tmp.append(value[1])
            tmp = sorted(tmp)
            blue.__setitem__(value[0], tmp)

    blues = sorted(blue.items(),key=lambda item:item[0])

    reds = sorted(red.items(),key=lambda item:-item[0])


    for bx in blues:
        print(bx)
        # for rx in reds:
        #     print(rx)




calculate(N, ARR, CRR)
