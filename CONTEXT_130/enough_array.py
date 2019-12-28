def calculate2(arr,k):
    for i in range(len(arr)):
        sumC = sum(arr[0:i+1])
        if sumC >= k:
            return len(arr) - i

    return 0

def calculate(arr,k):
    length = len(arr)

    result = 0
    for i in range(length):

        if sum(arr[i:]) < k:
            break

        ret = calculate2(arr[i:], k)
        result += ret
    return result





S = input().split(" ")
N = int(S[0])
K = int(S[1])

arr = [int(item) for item in input().split(" ")]

ret = calculate(arr,K)

print(ret)




