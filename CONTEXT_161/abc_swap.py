S = input().split(" ")
X = int(S[0])
Y = int(S[1])
Z = int(S[2])

tmp = Y
Y = X
X = tmp

tmp = X
X = Z
Z = tmp

print("{} {} {}".format(X,Y,Z))