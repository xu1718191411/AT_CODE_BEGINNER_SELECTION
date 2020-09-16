def calculate(n, k):
    s1 = 3 * 2 * (k - 1) * (n - k)
    s2 = (n - 1) * 3
    s3 = 1

    res = (s1 + s2 + s3)

    total = pow(n, 3)

    print(res/total)

N, K =  map(int,input().split())

calculate(N, K)
