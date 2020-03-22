def isOK(x):
    return x == "".join(reversed(x))


def calculate(S):
    if isOK(S) == False:
        print("No")
        return

    arr = list(S)
    length = len(arr)

    s1 = arr[0:(length-1)//2]

    if isOK("".join(s1)) == False:
        print("No")
        return

    s2 = arr[(length+2)//2:length]

    if isOK("".join(s2)) == False:
        print("No")
        return

    print("Yes")




S = input()

calculate(S)
