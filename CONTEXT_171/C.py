import math

N = int(input())

n = math.log((1 - (N * (1 - 26) // 26)), 26)

n = math.ceil(n)

S = 26 * (1 - 26 ** (n - 1)) // (1 - 26)

M = N - S - 1


res = ''

arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]

for i in range(n):
    index = i + 1

    s = M % (26 ** index)

    t = s // (26 ** i)

    res = arr[t] + res

    M -= s

print(res)
