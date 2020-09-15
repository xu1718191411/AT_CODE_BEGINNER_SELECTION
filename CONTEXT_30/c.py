# N, M = 3, 4
# X, Y = 2, 3
# ARR = [1, 5, 7]
# BRR = [3, 8, 12, 13]

N, M = map(int, input().split())
X, Y = map(int, input().split())
ARR = list(map(int, input().split()))
BRR = list(map(int, input().split()))


# N,M = 1, 1
# X,Y = 1, 1
# ARR = [1]
# BRR = [1]

def calculate(N, M, X, Y, ARR, BRR):
    times = []

    for i in range(N):
        times.append({'t': ARR[i], 'type': "A"})

    for i in range(M):
        times.append({'t': BRR[i], 'type': "B"})

    times = sorted(times, key=lambda x: x['t'])

    currentCount = 0
    currentTime = 0
    for time in times:
        if currentCount % 2 == 0:
            # A airport
            if time['type'] == "B":
                continue
            if time['t'] >= currentTime:
                currentTime = time['t'] + X
                currentCount += 1
        else:
            # B Airport
            if time['type'] == "A":
                continue
            if time['t'] >= currentTime:
                currentTime = time['t'] + Y
                currentCount += 1

    print(currentCount // 2)


calculate(N, M, X, Y, ARR, BRR)
