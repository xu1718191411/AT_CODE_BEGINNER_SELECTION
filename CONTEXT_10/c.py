import math

# txa, tya, txb, tyb, t, v = 7, 7, 1, 1, 3, 4
# n = 3
# arr = [
#     [8, 1],
#     [1, 7],
#     [9, 9],
# ]


txa, tya, txb, tyb, t, v = map(int,input().split())
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))


def calculate(txa, tya, txb, tyb, n, arr, maxDistance):

    isPossible = False
    for i in range(n):
        dx = arr[i][0]
        dy = arr[i][1]

        distance = math.sqrt(pow((dx - txa), 2) + pow((dy - tya), 2)) + math.sqrt(pow((dx - txb), 2) + pow((dy - tyb), 2))

        if maxDistance >= distance:
            isPossible = True
            break
    if isPossible:
        print("YES")
    else:
        print("NO")

calculate(txa, tya, txb, tyb, n, arr, t * v)
