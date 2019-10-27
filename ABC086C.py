import math

def main():
    n = int(input())
    coordinates = [[0, 0, 0]]
    for i in range(n):
        coordinates.append(convert(input().split(" ")))

    if checkNode(coordinates):
        print("Yes")
    else:
        print("No")

def checkNode(coordinates):

    for key,arr in enumerate(coordinates):
        if key == 0:
            continue
        number = coordinates[key][0] - coordinates[key-1][0]
        xDistance = math.fabs(coordinates[key][1] - coordinates[key-1][1])
        yDistance = math.fabs(coordinates[key][2] - coordinates[key-1][2])

        if not judge(number,xDistance,yDistance):
            return False
        return True


def convert(arr):
    result = []
    for s in arr:
        result.append(int(s))
    return result

def judge(number, xDistance,yDistance):

    distance = xDistance + yDistance

    if number < distance:
        return False

    if not isEven(number % distance):
        return False

    return True


def isEven(x):

    if x % 2 == 0:
        return True
    else:
        return False

main()

