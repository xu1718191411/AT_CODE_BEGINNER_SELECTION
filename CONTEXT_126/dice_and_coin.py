import math
def calculate(n,k):
    res = 0
    for i in range(n):
        indexN = i + 1

        temp = k / indexN

        if temp < 1:
            res = res + (1/n)
        else:
            t = math.log(temp,2)
            t = math.ceil(t)
            res = res + (1/n) * math.pow(0.5,t)

    print("{:.12f}".format(res))

S = input()
S = S.split(" ")
n = int(S[0])
k = int(S[1])

calculate(n,k)

