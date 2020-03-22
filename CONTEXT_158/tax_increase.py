import math

S = input().split(" ")
A = int(S[0])
B = int(S[1])

def calculate(a,b):
    theta = 1 - 1e-9

    s1 = a/0.08
    s2 = (a + theta)/0.08


    s3 = b/0.10
    s4 = (b + theta) / 0.10

    m1 = math.ceil(s1)
    m2 = math.floor(s2)

    m3 = math.ceil(s3)
    m4 = math.floor(s4)

    arr1 = [i for i in range(m1,m2+1)]
    arr2 = [i for i in range(m3,m4+1)]

    result = list(set(arr1).intersection(set(arr2)))


    if len(result) == 0:
        return -1
    else:
        return min(result)



result = calculate(A,B)
print(result)



