N = int(input())



def calculate(n):
    index = 1

    if n % 2 == 0:
        print(-1)
        return

    while not condition(index,n):
        index = index + 1

    print(index)

def condition(index,n):
    return (((pow(10,index) - 1) / 9)  %  n) == 0

calculate(N)