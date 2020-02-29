n = int(input())
arr = list(map(int,list(input().split(" "))))

sum = 0
smallest = 1

for i in range(n):

    if i == 0:
        sum += 1
        smallest = arr[i]
    else:
        if arr[i] > smallest:
            continue
        else:
            smallest = arr[i]
            sum += 1

print(sum)


