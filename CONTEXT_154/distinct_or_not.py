# N = 5
# ARR = [2, 6, 1, 4, 5]

# N = 6
# ARR = [4, 1, 3, 1, 6, 2]
#
#
# N = 2
# ARR = [10000000, 10000000]

N = int(input())
ARR = list(map(int,input().split()))

def calculate(n,arr):

    dict = {}
    result = True
    for i in range(n):
        item = arr[i]
        if dict.get(item) == None:
            dict.__setitem__(item,True)
        else:
            result = False
            break
    if result == True:
        print("YES")
    else:
        print("NO")

calculate(N,ARR)
