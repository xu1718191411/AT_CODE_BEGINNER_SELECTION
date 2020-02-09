def calculate():
    s = input()

    n0 = s.count("0")
    n1 = s.count("1")

    if n0 == n1:
        print(n0*2)
    elif n0 > n1:
        print(n1 * 2)
    else:
        print(n0 * 2)



calculate()