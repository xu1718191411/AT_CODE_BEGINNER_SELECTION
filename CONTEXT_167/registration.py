S = input()
T = input()

a = T[0:-1]

if (a == S) and (len(T) > len(S)):
    print("Yes")
else:
    print("No")
