ARR = [
    [2, 1, 3, 4, 5, 6],
    [2, 3, 1, 4, 5, 6],
    [2, 3, 4, 1, 5, 6],
    [2, 3, 4, 5, 1, 6],
    [2, 3, 4, 5, 6, 1],
    [3, 2, 4, 5, 6, 1],
    [3, 4, 2, 5, 6, 1],
    [3, 4, 5, 2, 6, 1],
    [3, 4, 5, 6, 2, 1],
    [3, 4, 5, 6, 1, 2],
    [4, 3, 5, 6, 1, 2],
    [4, 5, 3, 6, 1, 2],
    [4, 5, 6, 3, 1, 2],
    [4, 5, 6, 1, 3, 2],
    [4, 5, 6, 1, 2, 3],
    [5, 4, 6, 1, 2, 3],
    [5, 6, 4, 1, 2, 3],
    [5, 6, 1, 4, 2, 3],
    [5, 6, 1, 2, 4, 3],
    [5, 6, 1, 2, 3, 4],
    [6, 5, 1, 2, 3, 4],
    [6, 1, 5, 2, 3, 4],
    [6, 1, 2, 5, 3, 4],
    [6, 1, 2, 3, 5, 4],
    [6, 1, 2, 3, 4, 5],
    [1, 6, 2, 3, 4, 5],
    [1, 2, 6, 3, 4, 5],
    [1, 2, 3, 6, 4, 5],
    [1, 2, 3, 4, 6, 5],
    [1, 2, 3, 4, 5, 6]
]


N = int(input())

print("".join(map(str,ARR[(N-1) % 30])))