def shift_only():
    n = int(input())
    s = input().split()
    arr = [int(_s) for _s in s]

    return calculate(arr,0)


def calculate(arr,num):

    final = 0
    for s in arr:
        final += s % 2
    if final > 0:
        return num
    else:
        res = [s/2 for s in arr]
        return calculate(res,num+1)


print(shift_only())