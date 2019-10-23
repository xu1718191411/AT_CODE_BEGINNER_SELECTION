def filterDuplicate(arr):
    return len(list(dict.fromkeys(arr)))

n = input()
arr = []
for i in range(int(n)):
    arr.append(int(input()))

print(filterDuplicate(arr))