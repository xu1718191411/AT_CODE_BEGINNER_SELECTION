# N, K = 5, 3
# HRR = [10, 30, 40, 50, 20]

N, K = 3, 1
HRR = [10, 20, 10]

N, K = 2, 100
HRR = [10, 10]

N, K = 10, 4
HRR = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]

N, K = map(int, input().split())
HRR = list(map(int, input().split()))


def calculate(n, k, hrr):
    result = []
    for i in range(n):
        if i == 0:
            result.append(0)
            continue

        mins = -1
        for j in range(1, k + 1):
            index = i - j
            if index >= 0:
                value = result[index] + abs(hrr[i] - hrr[index])
                if mins == -1:
                    mins = value
                else:
                    if value < mins:
                        mins = value
        result.append(mins)

    print(result[-1])


calculate(N, K, HRR)
