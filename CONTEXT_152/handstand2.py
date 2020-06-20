N = int(input())

# N = 25

def calculate(n):
    result = {}

    for index in range(1, n + 1):

        i = int(str(index)[0])
        j = int(str(index)[-1])
        if result.get((i, j)) == None:
            if i != 0:
                result.__setitem__((i, j), 1)
        else:
            result.__setitem__((i, j), result.get((i, j)) + 1)

    res = 0
    for i in range(10):
        for j in range(10):
            s1 = result.get((i, j))
            s2 = result.get((j, i))

            s1 = 0 if s1 == None else s1
            s2 = 0 if s2 == None else s2

            res += s1 * s2

    print(res)


calculate(N)
