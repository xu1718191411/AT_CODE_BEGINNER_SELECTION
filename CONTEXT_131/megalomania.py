def calculate(list):
    current = 0
    for item in list:
        current += item[0]
        if current > item[1]:
            return False

    return True

N = int(input())

arr = []
for i in range(N):
    arr.append([int(s) for s in input().split(" ")])

arr2 = sorted(arr,key=lambda x:x[1])

result = calculate(arr2)

if result:
    print("Yes")
else:
    print("No")