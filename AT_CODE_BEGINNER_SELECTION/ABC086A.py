def product():
    a,b = input().split()
    a = int(a)
    b = int(b)
    return "Even" if (a % 2 == 0 or b % 2 == 0) else "Odd"

print(product())