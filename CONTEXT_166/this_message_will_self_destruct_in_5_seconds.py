N = 6
ARR = [2, 3, 3, 1, 3, 1]

# N = 6
# ARR = [5, 2, 4, 2, 8, 8]

N = 32
ARR = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5]

N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    A = {}
    B = {}

    for i in range(1, n + 1):
        Ai = arr[i - 1]
        Aj = arr[i - 1]

        a = Ai + i
        b = (i - Aj)

        if A.get(a) == None:
            A.__setitem__(a, [i])
        else:
            tmp = A.__getitem__(a)
            tmp.append(i)
            A.__setitem__(a, tmp)

        if B.get(b) == None:
            B.__setitem__(b, [i])
        else:
            tmp = B.__getitem__(b)
            tmp.append(i)
            B.__setitem__(b, tmp)

    result = 0
    for key in A.keys():
        l1 = len(A.get(key))

        if B.get(key) != None:
            l2 = len(B.get(key))
            result += l1 * l2

    print(result)


calculate(N, ARR)
