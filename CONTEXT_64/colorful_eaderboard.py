import numpy as np
N = int(input())
ARR = [int(s) for s in input().split(" ")]

def calculate(n, arr):
    dict = {'gray': False, 'brown': False, 'green': False, 'water': False, 'blue': False, 'yellow': False,
            'orange': False, 'red': False}
    any = 0

    for ar in arr:
        if ar >= 1 and ar <= 399:
            dict.__setitem__('gray',True)
        elif ar >= 400 and ar <= 799:
            dict.__setitem__('brown', True)
        elif ar >= 800 and ar <= 1199:
            dict.__setitem__('green', True)
        elif ar >= 1200 and ar <= 1599:
            dict.__setitem__('water', True)
        elif ar >= 1600 and ar <= 1999:
            dict.__setitem__('blue', True)
        elif ar >= 2000 and ar <= 2399:
            dict.__setitem__('yellow', True)
        elif ar >= 2400 and ar <= 2799:
            dict.__setitem__('orange', True)
        elif ar >= 2800 and ar <= 3199:
            dict.__setitem__('red', True)
        else:
            any = any + 1

    l = np.array(list(dict.values()))

    goodNum = np.sum(l == True)
    badNum = np.sum(l == False)

    if goodNum == 0:
        print(1,goodNum + any)
    else:
        print(goodNum,goodNum + any)

calculate(N,ARR)