import sys
sys.setrecursionlimit(20000000)
N = int(input())
memo = [-1 for i in range(110000)]
def calculate(n):

    if n == 0:
        memo[n] = 0
        return 0

    if memo[n] != -1:
        return memo[n]

    res = n

    pow6Num = 1
    while pow6Num*6 <= n:
        pow6Num = pow6Num * 6
        res = min(res, calculate(n - pow6Num) + 1)


    pow9Num = 1
    while pow9Num*9 <= n:
        pow9Num = pow9Num * 9
        res = min(res, calculate(n - pow9Num) + 1)

    memo[n] = int(res)
    return int(res)



result = calculate(N)
print(memo[N])
