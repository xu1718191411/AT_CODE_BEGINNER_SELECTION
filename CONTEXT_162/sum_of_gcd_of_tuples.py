K = int(input())

import math
import itertools


def common(a, b):
    return math.gcd(a, b)


def calculate(k):
    sum = 0
    for i in itertools.combinations([i for i in range(1,k+1)],2):
        val1 = common(i[0],i[1]) * 6
        sum = sum + val1

    for i in range(1,k+1):
        val1 = i
        sum = sum + val1

    for  i in itertools.combinations([i for i in range(1,k+1)],3):
        val1 = common(i[0],i[1])
        val2 = common(val1,i[2])
        sum = sum + val2*6


    print(sum)




calculate(K)