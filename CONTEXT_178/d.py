import sys

sys.setrecursionlimit(100000)

MOD = 1000000000 + 7
sumArr = []


def calculate(n):
    global result
    result = 0

    if n >= 3:
        dfs([], n)
        print(result + 1)
    else:
        print(result)

    print(sumArr)


def dfs(parentArr, currentTotal):
    global result
    i = 3
    while (i <= currentTotal) and (currentTotal - i) >= 3:
        tmp = parentArr.copy()
        tmp.extend([i])
        tmp2 = parentArr.copy()
        tmp2.extend([i, currentTotal - i])
        sumArr.append(tmp2)
        dfs(tmp, currentTotal - i)
        i += 1
        result += 1
        result %= MOD


calculate(int(input()))
