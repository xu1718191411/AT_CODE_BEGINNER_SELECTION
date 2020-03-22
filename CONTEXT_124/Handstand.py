# n = 5
# k = 1
# arr = [0,0,0,1,0]


n = 14
k = 2
arr = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1]


def calculate(n, k, arr):
    j = 0
    s = 0
    sums = []
    for i in range(n):
        if i > j:
            s = 0
            j = i

        while (j < n) and (arr[j] == 0):
            j = j + 1
        s = j - i
        sums.append(s)
        s = s - i
    print(sums)


def reverse(n):
    if n == 1:
        return 0
    else:
        return 1


calculate(n, k, arr)
