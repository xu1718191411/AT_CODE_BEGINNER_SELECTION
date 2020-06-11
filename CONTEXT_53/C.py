x = int(input())

# x = 149696127901
def calculate(x):

    if x <= 6:
        return 1

    a = x // 11
    mod = x % 11

    if mod == 0:
        return 2*a

    if mod >= 7:
        return 2*a + 2

    return 2*a + 1



res = calculate(x)

print(res)