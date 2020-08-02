# N = 8
# ARR = [1, 2, 3, 2, 2, 5, 6, 9]

N = int(input())

ARR = list(map(int,input().split()))
def calculate(n, arr):
    mrr = []
    flag = 0

    for i in range(n):
        flag += 1

        if i == n - 1:
            mrr.append(flag)
            continue

        if arr[i + 1] > arr[i]:
            continue
        else:
            mrr.append(flag)
            flag = 0

    # print(mrr)


    result = n

    for index in range(len(mrr)):
        val = mrr[index]
        result +=  val * (val - 1) // 2


    print(result)


calculate(N, ARR)
