arr = [1, 2, 3, 4, 5, 6]

N = int(input())

for i in range(N % 30):
    start = (i % 5)
    end = (i % 5) + 1
    tmp = arr[end]
    arr[end] = arr[start]
    arr[start] = tmp


print("".join(map(str,arr)))