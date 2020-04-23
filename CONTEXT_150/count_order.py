import itertools
# N = 3
# P = [1, 3, 2]
# Q = [3, 1, 2]
#
# N = 8
# P = [7, 3, 5, 4, 2, 1, 6, 8]
# Q = [3, 8, 2, 5, 4, 6, 7, 1]
#
#
# N = 3
# P = [1, 2, 3]
# Q = [1, 2, 3]

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

def calculate(n,p,q):
    x = 0
    y = 0

    for index,ar in enumerate(itertools.permutations([i for i in range(1,n+1)],n)):
        if list(ar) == list(p):
            x = index

        if list(ar) == list(q):
            y = index

    if x >= y:
        print(x-y)
    else:
        print(y-x)
calculate(N,P,Q)