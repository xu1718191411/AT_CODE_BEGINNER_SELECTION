N = 9
PRR = [1, 2, 4, 9, 5, 8, 7, 3, 6]

N = 5
PRR = [1, 2, 3, 4, 5]

#
# N = 2
# PRR = [2, 1]
#
# N = 2
# PRR = [1, 2]
#
# N = 5
# PRR = [1, 4, 3, 5, 2]

N = int(input())
PRR = list(map(int, input().split()))


def calculate(n, prr):
    result = 0
    for i in range(n - 1):
        if prr[i] == (i + 1):
            prr[i], prr[i + 1] = prr[i + 1], prr[i]
            result += 1

    if prr[n - 1] == n:
        result += 1
    print(result)


calculate(N, PRR)
