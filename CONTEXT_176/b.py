N = input()

arr = [int(i) for i in  list(N)]

if sum(arr) % 9 == 0:
    print("Yes")
else:
    print("No")




