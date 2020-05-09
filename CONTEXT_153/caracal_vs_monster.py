H = int(input())

def calculate(h):
    if h == 1:
        return 1
    return 1 + 2*calculate(h//2)


result = calculate(H)

print(result)