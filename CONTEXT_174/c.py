K = int(input())

def calculate(k):

    if k % 2 == 0:
        print(-1)
        return

    if k % 5 == 0:
        print(-1)
        return

    res = 1

    m = (((10 ** res) - 1) // 9) * 7


    while m % k > 0:
        res += 1
        m = m % k
        m = m * 10 + 7

    print(res)


calculate(K)

