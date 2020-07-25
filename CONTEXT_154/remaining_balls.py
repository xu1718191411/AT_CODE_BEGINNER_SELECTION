S, T = "red", "blue"
A, B = 3, 4
U = "red"

S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()


def calculate(s, t, a, b, u):
    if u == s:
        print("{} {}".format((a - 1), b))
    else:
        print("{} {}".format(a, (b - 1)))


calculate(S, T, A, B, U)
