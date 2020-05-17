import itertools
N = 6
ARR = [5, 2, 4, 2, 8, 8]


def calculate(n,arr):
    print(n)
    print(arr)

    dict = {}
    dict2 = {}
    for index,val in enumerate(arr):
        index = index + 1
        s = index + val
        if dict.get(s) == None:
            dict.__setitem__(s,1)
        else:
            dict.__setitem__(s,dict.get(s)+1)

        s2 = index - val
        if dict2.get(s2) == None:
            dict2.__setitem__(s2,1)
        else:
            dict2.__setitem__(s2,dict2.get(s2)+1)
    print(dict)
    print(dict2)


calculate(N,ARR)