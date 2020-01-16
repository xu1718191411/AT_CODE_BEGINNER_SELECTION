
n = int(input())

arr = []
for i in range(5):
    arr.append(int(input()))

def calculate(arr,n):
    minVal = min(arr)
    return int(((minVal + n - 1) / minVal) + 4)

result = calculate(arr,n)
print(result)