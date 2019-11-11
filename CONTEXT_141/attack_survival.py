def calculate(n,k,q,arr):
    result = [k]*n
    for index in range(q):
        result[arr[index] - 1] = result[arr[index] - 1] + 1

    for index in range(len(result)):
        if (result[index] - q) > 0:
            print("Yes")
        else:
            print("No")

N,K,Q = input().split(' ')
N = int(N)
K = int(K)
Q = int(Q)

arr = []
for i in range(Q):
    arr.append(int(input()))

calculate(N,K,Q,arr)