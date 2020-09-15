D, T, S = map(int, input().split())


def calculate(d, t, s):

    if t * s >= d:
        print("Yes")
    else:
        print("No")


calculate(D, T, S)
