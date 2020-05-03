import itertools

# N, M, Q = 3, 4, 3
# ARR = [
#     [1, 3, 3, 100],
#     [1, 2, 2, 10],
#     [2, 3, 2, 10]
# ]

# 4 6 10
# 2 4 1 86568
# 1 4 0 90629
# 2 3 0 90310
# 3 4 1 29211
# 3 4 3 78537
# 3 4 2 8580
# 1 2 1 96263
# 1 4 2 2156
# 1 2 0 94325
# 1 4 3 94328


N, M, Q = map(int, input().split())
ARR = []
for i in range(Q):
    ARR.append(list(map(int, input().split())))


def calculate(n, m, q, arr):
    result = []
    for comb in itertools.combinations_with_replacement(range(1, m + 1), n):
        result.append(mmm(list(comb), arr))

    print(max(result))


def mmm(comb, arr):
    result = 0

    for ar in arr:
        if (comb[ar[1] - 1] - comb[ar[0] - 1]) == ar[2]:
            result = result + ar[3]
    return result


calculate(N, M, Q, ARR)
