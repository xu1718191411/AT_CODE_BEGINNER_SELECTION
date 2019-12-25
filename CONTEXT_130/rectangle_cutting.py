def calculate(w,h,x,y):

    b = 0
    if (x - w/2 == 0) and (y - h/2 == 0):
        b = 1


    arr = [w*h/2,b]
    print(" ".join([str(item) for item in arr]))


arr = input().split(" ")
W = int(arr[0])
H = int(arr[1])
x = int(arr[2])
y = int(arr[3])

calculate(W,H,x,y)