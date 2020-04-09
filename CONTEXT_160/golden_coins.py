X = int(input())

def calculate(x):
    a = x // 500
    b = x % 500

    c = b // 5
    d = b % 5
    print(a * 1000 + c * 5)


calculate(X)
