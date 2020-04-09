K = int(input())

n = 1
s = 9 * 2 ** (n - 1)
while s < K:
    n = n + 1
    s = 9 * 2 ** (n - 1)

result = []


def bianli(currentIndex, currentValue, currentValueStr, maxLevel):
    if currentIndex < maxLevel:

        nextIndex = currentIndex + 1

        result.append(int(currentValueStr))

        bianli(nextIndex, currentValue, "{}{}".format(currentValueStr, currentValue), maxLevel)

        if currentValue == 0:
            nextValue = 1
            bianli(nextIndex, nextValue, "{}{}".format(currentValueStr, nextValue), maxLevel)
        elif currentValue == 9:
            nextValue = 8
            bianli(nextIndex, nextValue, "{}{}".format(currentValueStr, nextValue), maxLevel)
        else:
            nextValue = currentValue + 1
            bianli(nextIndex, nextValue, "{}{}".format(currentValueStr, nextValue), maxLevel)
            nextValue = currentValue - 1
            bianli(nextIndex, nextValue, "{}{}".format(currentValueStr, nextValue), maxLevel)

    else:
        result.append(int(currentValueStr))


bianli(1, 1,"1", n)
bianli(1, 2,"2", n)
bianli(1, 3,"3", n)
bianli(1, 4,"4", n)
bianli(1, 5,"5", n)
bianli(1, 6,"6", n)
bianli(1, 7,"7", n)
bianli(1, 8,"8", n)
bianli(1, 9,"9", n)

print(sorted(result)[K-1])
