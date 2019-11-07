def divide(x):
    result = []

    if x == 1:
        return []

    if x == 2:
        return [2]

    if x % 2 == 0:
        result.extend([2])
        result.extend(divide(int(x/2)))
        return result

    if x % 3 == 0:
        result.extend([3])
        result.extend(divide(int(x/3)))
        return result

    if x % 5 == 0:
        result.extend([5])
        result.extend(divide(int(x/5)))
        return result

    if x % 7 == 0:
        result.extend([7])
        result.extend(divide(int(x/7)))
        return result

    return [x]

def rank(arr):
    lastIndex = len(arr) - 1
    while lastIndex > 0:

        for i in range(lastIndex):
            if arr[i+1] < arr[i]:
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp

        lastIndex = lastIndex - 1

    return arr


def calculate(result):
    if len(result) == 0:
        return 0

    if len(result) == 1:
        if result[0] > 1:
            return result[0] - 1
        return result[0]

    if len(result) == 2:

        if result[0] > 1:
            result[0] = result[0] - 1

        if result[1] > 1:
            result[1] = result[1] - 1

        return result[0] + result[1]

    else:

        if len(result) % 2 == 0:
            s1 = 1
            s2 = 1
            for i in range(int(len(result) / 2)):
                if i % 2 == 0:
                    s1 *= (result[i] * result[len(result) - 1 - i])
                else:
                    s2 *= (result[i] * result[len(result) - 1 - i])
            if s1 > 1:
                s1 = s1 - 1

            if s2 > 1:
                s2 = s2 - 1
            return s1 + s2

        else:
            s1 = 1
            s2 = 1
            for i in range(int((len(result)-1) / 2)):
                if i % 2 == 0:
                    s1 *= (result[i] * result[len(result) - 1 - i])
                else:
                    s2 *= (result[i] * result[len(result) - 1 - i])

            m = result[int((len(result)-1)/2)]
            if s1 > s2:
                 s2 = s2 * m
            else:
                 s1 = s1 * m

            if s1 > 1:
                s1 = s1 - 1

            if s2 > 1:
                s2 = s2 - 1
            return s1 + s2

N = int(input())

d = divide(N)
a = rank(d)
print(calculate(a))



