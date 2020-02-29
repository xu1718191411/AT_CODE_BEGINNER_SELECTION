# n = 4
# arr = [
#     [2, 3, 5],
#     [2, 1, 5],
#     [1, 2, 5],
#     [3, 2, 5],
# ]


# n = 2
# arr = [
#     [0, 0, 100],
#     [1, 1, 98],
# ]
#

# n = 3
# arr = [
#     [99, 1, 191],
#     [100, 1, 192],
#     [99, 0, 192]
# ]


arr = []
n = int(input())

for i in range(n):
    arr.append([int(s) for s in input().split(" ")])



import math

def calculate(n, arr):
    for i in range(101):
        for j in range(101):

            centerH = -100

            for ar in arr:
                posX = ar[0]
                posY = ar[1]
                posH = ar[2]

                if posH > 0:

                    if centerH == -100:
                        centerH = posH + int(math.fabs(i - posX)) + int(math.fabs(j - posY))
                        continue

                    tmp = posH + int(math.fabs(i - posX)) + int(math.fabs(j - posY))

                    if tmp != centerH:
                        centerH = -2
                        break

            for ar in arr:
                posX = ar[0]
                posY = ar[1]
                posH = ar[2]
                if posH == 0:
                    if int(math.fabs(i - posX)) + int(math.fabs(j - posY)) < centerH:
                        centerH = -2
                        break

            if centerH != -2:
                print(i, j, centerH)





calculate(n, arr)
