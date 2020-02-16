n = int(input())
S = input().split(" ")
arr = [int(s) for s in S]
def calculate(n,arr):
    ans = 0
    for i in range(len(arr)):
        if i == 0:
            ans += arr[i]
        else:
            if arr[i] > arr[i-1]:
                ans += (arr[i] - arr[i-1])
    return ans

result = calculate(n,arr)

print(result)
