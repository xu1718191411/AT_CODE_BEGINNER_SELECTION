import math


# 最大公约数
def zuidagongyueshu(x, y):
    if y % x == 0:
        return x

    if x % y == 0:
        return y

    if x < y:
        return zuidagongyueshu(y % x, x)
    else:
        return zuidagongyueshu(x % y, y)


# 分解质因数
# 30 = 2*3*5
# 60 = (2,2)*3*5
# 420 = (2,2)*3*5*7
# 1260 = (2,2)*(3,2)*5*7
# 6300 = (2,2)*(3,2)*(5,2)*7

container = []
def fenjiezhiyinshu(x):
    for i in range(1, x + 1):
        if i == 1:
            continue
        else:
            flag = False
            while x % i == 0:
                x = int(x / i)
                flag = True

            if flag:
                container.append(i)
                return fenjiezhiyinshu(x)

S = input().split(' ')
arr = list(map(int, list(S)))
fenjiezhiyinshu(zuidagongyueshu(arr[0],arr[1]))
print(len(container)+1)


