def calculate(a,b):
    s1 = list([str(a)]*b)
    s1 = "".join(s1)

    s2 = list([str(b)]*a)
    s2 = "".join(s2)

    arr = [s1,s2]

    arr = sorted(arr)

    print(arr[0])

S = input().split(" ")
a = int(S[0])
b = int(S[1])

calculate(a,b)
