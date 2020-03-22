S = input().split(" ")
n = int(S[0])
k = int(S[1])
arr = []
for i in range(n):
    arr.append(int(input()))


# n = 5
# k = 3
# arr = [5, 7, 5, 7, 7]

# n = 5
# k = 3
# arr = [10,15,11,14,12]


def calculate(n, k, arr):
    arr.sort()
    drr = []
    for i in range(1, n):
        drr.append(arr[i] - arr[i - 1])

    j = 0
    s = 0
    sums = []

    for i in range(len(drr) - (k - 1) + 1):
        while j < i + (k-1):
            s = s + drr[j]
            j = j + 1
        sums.append(s)
        s = s - drr[i]
    print(min(sums))



calculate(n, k, arr)
