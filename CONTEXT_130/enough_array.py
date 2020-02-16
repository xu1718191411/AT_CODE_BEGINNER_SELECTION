# n = 4
# k = 10
# arr = [6, 1, 2, 7]
#
# n = 3
# k = 5
# arr = [7, 7, 7]

# n = 10
# k = 53462
# arr = [103,35322,232,342,21099,90000,18843,9010,35221,19352]


# S = input().split(" ")
# n = int(S[0])
# k = int(S[1])
#
# S = input().split(" ")
# arr = [int(s) for s in S]

def calculate(n,k,arr):

    ans = 0
    j = 0
    s = 0
    for i in range(n):
        while (j < n) and ((s+arr[j]) < k):
            s = s + arr[j]
            j = j + 1
        ans = ans + j - i
        s = s - arr[i]

    return ans

ans = calculate(n,k,arr)

result = n + (n*(n-1) // 2) - ans

print(result)