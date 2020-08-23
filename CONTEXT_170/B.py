X,Y = map(int,input().split())

def calculate(x,y):
    a = (4 * x - y) / 2
    b = x - a
    if a < 0:
        print("No")
        return
    if b < 0:
        print("No")
        return

    if float.is_integer(a) and float.is_integer(b):
        print("Yes")
    else:
        print("No")

calculate(X,Y)