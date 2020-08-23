# N = 8
# S = "WRWWRWRR"
#
# N = 2
# S = "RR"
#
# N = 4
# S = "WWRR"

N = int(input())
S = input()

# N = 2
# S = "WW"

def calculate(n, s):
    arr = list(s)

    RNum = arr.count("R")

    leftW = 0
    rightR = RNum

    result = []
    for i in range(n):
        if arr[i] == "R":
            rightR -= 1
        if arr[i] == "W":
            leftW += 1

        if (leftW == 0) and arr[i] == "R":
            result.append(0)
            continue

        if (rightR == 0) and arr[i] == "W":
            result.append(0)
            continue

        result.append(max(leftW, rightR))

    print(min(result))


calculate(N, S)
