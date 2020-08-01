from copy import deepcopy
# H, W = 4, 4
# SRR = [
#     list("###."),
#     list("##.#"),
#     list("..##"),
#     list("..##")
# ]
#
#
# H, W = 4, 4
# SRR = [
#     list("###."),
#     list("####"),
#     list("..##"),
#     list("..##"),
# ]
#
#
# H,W = 4, 4
# ARR = [
#     list("##.."),
#     list("##.."),
#     list("..##"),
#     list("..##"),
# ]


H, W = map(int, input().split())
SRR = []

for i in range(H):
    SRR.append(list(input()))


def calculate(h, w, criterion):

    handMade = deepcopy(criterion)
    for i in range(h):
        for j in range(w):
            if criterion[i][j] == '.':
                if i - 1 >= 0 and j - 1 >= 0:
                    handMade[i-1][j-1] = '.'

                if i - 1 >= 0:
                    handMade[i-1][j] = '.'

                if j + 1 < w and i - 1 >= 0:
                    handMade[i-1][j+1] = '.'

                if j - 1 >= 0:
                    handMade[i][j-1] = '.'

                if j+1 < w:
                    handMade[i][j+1] = '.'

                if j-1 >= 0 and i + 1 < h:
                    handMade[i+1][j-1] = '.'

                if i + 1 < h:
                    handMade[i+1][j] = '.'

                if i + 1 < h and j + 1 < w:
                    handMade[i+1][j+1] = '.'

    finalMake = deepcopy(handMade)

    for i in range(h):
        for j in range(w):
            if handMade[i][j] == '#':
                if i - 1 >= 0 and j - 1 >= 0:
                    finalMake[i-1][j-1] = '#'

                if i - 1 >= 0:
                    finalMake[i-1][j] = '#'

                if j + 1 < w and i - 1 >= 0:
                    finalMake[i-1][j+1] = '#'

                if j - 1 >= 0:
                    finalMake[i][j-1] = '#'

                if j+1 < w:
                    finalMake[i][j+1] = '#'

                if j-1 >= 0 and i + 1 < h:
                    finalMake[i+1][j-1] = '#'

                if i + 1 < h:
                    finalMake[i+1][j] = '#'

                if i + 1 < h and j + 1 < w:
                    finalMake[i+1][j+1] = '#'

    isOk = True
    for i in range(h):
        s1 = "".join(criterion[i])
        s2 = "".join(finalMake[i])

        if s1 != s2:
            isOk = False
            break

    if isOk == True:
        print("possible")
        for i in range(h):
            print("".join(handMade[i]))
    else:
        print("impossible")

calculate(H, W, SRR)
