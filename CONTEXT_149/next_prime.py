X = int(input())


def calculate(x):
    if x == 2:
        return 2

    while not condition(x):
        x = x + 1

    return x

def condition(x):
    result = True
    for i in range(2,x):
        if x % i == 0:
            result = False
            break

    return result


result = calculate(X)

print(result)
