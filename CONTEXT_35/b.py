S = input()
T = int(input())

def calculate(s,t):
    currentX = 0
    currentY = 0

    unDefinedNum = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'U':
            currentY += 1
            continue

        if s[i] == 'L':
            currentX -= 1
            continue

        if s[i] == 'R':
            currentX += 1
            continue

        if s[i] == 'D':
            currentY -= 1
            continue

        if s[i] == '?':
            unDefinedNum += 1

    mk2 = abs(currentX) + abs(currentY)
    if t == 1:
        print(mk2 + unDefinedNum)
    else:
        if mk2 >= unDefinedNum:
            print(mk2 - unDefinedNum)
        else:
            s = unDefinedNum - mk2

            print(s % 2)

calculate(S, T)