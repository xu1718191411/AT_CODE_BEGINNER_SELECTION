N = int(input())
S = input()


def calculate(n, s):
    arr = list(s)
    result = []


    leftW = 0
    rightR = arr.count('R')


    if rightR == 0:
        print(0)
        return

    for i in range(n):
        val = arr[i]

        if val == 'R':
            rightR -= 1

        if val == 'W':
            leftW += 1

        result.append(max(leftW,rightR))

    if len(result) == 0:
        print(0)
    else:
        print(min(result))

calculate(N, S)
