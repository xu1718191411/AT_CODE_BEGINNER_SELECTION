def calculate(n):
    mod = 1000000000 + 7

    result = pow(10, n, mod)

    # has 0 exists  9 not exists
    # 0 - 8
    s1 = pow(9, n, mod) - pow(8, n, mod)

    # has 9 exists 0 not exists
    # 1 - 9
    s2 = pow(9, n, mod) - pow(8, n, mod)

    # 9 not exists and 8 not exists
    # 1-8
    s3 = pow(8, n, mod)

    result = result - (s1 + s2 + s3)

    print(result % mod)


calculate(int(input()))
