N, D, K = map(int, input().split())

LR = []

for i in range(D):
    LR.append(list(map(int, input().split())))

ST = []
for i in range(K):
    ST.append(list(map(int, input().split())))


def calculate(n, d, k, lrr, stt):
    result = [-1 for i in range(k)]
    for index, lr in enumerate(lrr):
        for i in range(len(stt)):
            if result[i] > -1:
                continue
            if (stt[i][1] - stt[i][0]) >= 0:
                if stt[i][0] >= lr[0] and (lr[1] > stt[i][0]):
                    stt[i][0] = lr[1]

                if stt[i][0] >= stt[i][1]:
                    result[i] = index + 1

            if (stt[i][1] - stt[i][0]) < 0:
                if stt[i][0] <= lr[1] and (lr[0] < stt[i][0]):
                    stt[i][0] = lr[0]

                if stt[i][0] <= stt[i][1]:
                    result[i] = index + 1

    for res in result:
        print(res)


calculate(N, D, K, LR, ST)
