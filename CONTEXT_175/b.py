import itertools

N = 5
ARR = [4, 4, 9, 7, 5]


N = 10
ARR = [9, 4, 6, 1, 9, 6, 10, 6, 6, 8]

N = int(input())
ARR = list(map(int,input().split()))

result = 0
for item in itertools.combinations(ARR, 3):
    x, y, z = item

    if x == y:
        continue
    if x == z:
        continue
    if y == z:
        continue

    if x + y > z:
        if abs(x - y) < z:
            result += 1

print(result)
