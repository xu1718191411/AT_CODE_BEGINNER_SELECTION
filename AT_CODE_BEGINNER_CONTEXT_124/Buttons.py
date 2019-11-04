def chooseBig(x, y):
    if x > y:
        return x, x - 1, y
    else:
        return y, x, y - 1

A, B = input().split(' ')
A = int(A)
B = int(B)

sum1, A, B = chooseBig(A, B)
sum2, A, B = chooseBig(A, B)
print(sum1 + sum2)



