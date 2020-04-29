# A = 10
# B = 9
# C = 10
# D = 10


# A = 46
# B = 4
# C = 40
# D = 5

A,B,C,D = map(int,input().split())


while A > 0 and C > 0:
    C = C - B
    if C <= 0:
        print("Yes")
        break
    A = A - D
    if A <= 0:
        print("No")
        break