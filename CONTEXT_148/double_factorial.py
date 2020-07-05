def calculate(n):
    if n % 2 == 1:
        return 0

    s1 = n // 10

    index = 1

    s2 = 0
    while (5 ** index) <= s1:
        s2 += (s1 // (5 ** index))
        index += 1

    return s1 + s2


print(calculate(int(input())))