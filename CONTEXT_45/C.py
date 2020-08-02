import itertools

S = input()


def calculate(s):
    arr = list(s)

    totalLength = len(s)

    spliteIndexes = [i for i in range(1,totalLength)]

    result = 0
    for i in range(1, totalLength):
        for item in itertools.combinations(spliteIndexes, i):
            ttr = [0]
            ttr.extend(list(item))
            ttr.append(totalLength)


            for i in range(len(ttr) - 1):
                result += int("".join(arr[ttr[i]:ttr[i+1]]))
    print(result + int(s))


calculate(S)


