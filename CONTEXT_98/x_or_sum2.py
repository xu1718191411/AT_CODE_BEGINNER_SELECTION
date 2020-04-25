# N = 4
# ARR = [2, 5, 4, 6]
#
# N = 9
# ARR = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# N = 19
# ARR = [885, 8, 1, 128, 83, 32, 256, 206, 639, 16, 4, 128, 689, 32, 8, 64, 885, 969, 1]
N = int(input())
ARR = list(map(int,input().split()))
def calculate(n,arr):
    right = 0
    sum = arr[0]
    result = 0

    for left in range(0,n):
        while (right + 1 < n) and ( (sum + arr[right+1]) == (sum ^ arr[right+1]) ):
            right = right + 1
            sum = sum + arr[right]

        result = result + right - left + 1
        sum = sum - arr[left]

    print(result)

calculate(N,ARR)